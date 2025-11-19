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

    <q-dialog v-model="dialogOpen" persistent>
      <q-card style="width: 400px">
        <q-card-section style="background-color: teal; color: white">
          <span>Adding a New Cagetory</span>
        </q-card-section>
        <q-card-section>
          <q-input name="name" v-model="categoryNew" label="Name" color="teal"></q-input>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn outline color="teal" label="Cancel" v-close-popup></q-btn>
          <q-btn outline color="teal" label="Submit" v-close-popup></q-btn>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { apiRoot } from 'boot/ezglobals'

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

getCategories()
</script>
