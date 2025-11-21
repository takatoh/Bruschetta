<template>
  <q-page padding>
    <!-- content -->
    <h5 class="text-teal-10">Categories</h5>

    <div class="q-pa-md">
      <q-table
        :rows="categories"
        :columns="categoryColumns"
        row-key="id"
        :rows-per-page-options="[0]"
        bordered
        dense
      ></q-table>

      <div>
        <q-btn label="Add a new category" color="teal" outline @click="openDialog"></q-btn>
      </div>
    </div>

    <adding-dialog
      v-model="dialogOpen"
      label="Adding a New Category"
      @submit="addCategory"
      @cancel="cancel"
    >
      <q-input name="name" v-model="categoryNew" label="Name" color="teal"></q-input>
    </adding-dialog>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { apiRoot } from 'boot/ezglobals'
import AddingDialog from 'src/components/AddingDialog.vue'

const categories = ref([])
const dialogOpen = ref(false)
const categoryNew = ref(null)

const categoryColumns = [
  { name: 'id', label: 'ID', align: 'left', field: (row) => row['id'], format: (val) => `${val}` },
  { name: 'name', label: 'Name', align: 'left', field: 'name' },
]

const getCategories = async () => {
  const url = `${apiRoot}/categories`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => (categories.value = result.categories))
}

const openDialog = () => {
  dialogOpen.value = !dialogOpen.value
}

const addCategory = async () => {
  console.log(`Add a new category: ${categoryNew.value}`)
  const url = `${apiRoot}/categories`
  await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name: categoryNew.value }),
  })
    .then((response) => {
      if (response.ok) {
        return response.json()
      } else {
        throw new Error(`Error occured: response status = ${response.status}`)
      }
    })
    .then(() => {
      categoryNew.value = null
      getCategories()
    })
    .catch((error) => console.log(error))
}

const cancel = () => {
  categoryNew.value = null
}

getCategories()
</script>
