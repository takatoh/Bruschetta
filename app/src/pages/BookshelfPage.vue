<template>
  <q-page padding>
    <!-- content -->
    <h5 class="text-teal-10">Booksheves</h5>

    <div class="q-pa-md">
      <q-table
        :rows="bookshelves"
        :columns="bookshelfColumns"
        row-key="id"
        :rows-per-page-options="[0]"
        bordered
        dense
      ></q-table>

      <div>
        <q-btn label="Add a new bookshelf" color="teal" outline @click="openDialog"></q-btn>
      </div>
    </div>

    <adding-dialog
      v-model="dialogOpen"
      label="Adding a New Bookshelf"
      @submit="addBookshelf"
      @cancel="cancel"
    >
      <q-input name="name" v-model="bookshelfNewName" label="Name" color="teal"></q-input>
      <q-input
        name="description"
        v-model="bookshelfNewDescription"
        label="Description"
        color="teal"
      ></q-input>
    </adding-dialog>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { apiRoot } from 'boot/ezglobals'
import AddingDialog from 'src/components/AddingDialog.vue'

const bookshelves = ref([])
const dialogOpen = ref(false)
const bookshelfNewName = ref(null)
const bookshelfNewDescription = ref(null)

const bookshelfColumns = [
  { name: 'id', label: 'ID', align: 'left', field: (row) => row['id'], format: (val) => `${val}` },
  { name: 'name', label: 'Name', align: 'left', field: 'name' },
  { name: 'description', label: 'Description', align: 'left', field: 'description' },
]

const getBookshelves = async () => {
  const url = `${apiRoot}/bookshelves`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => (bookshelves.value = result.bookshelves))
}

const openDialog = () => {
  dialogOpen.value = !dialogOpen.value
}

const addBookshelf = async () => {
  console.log(`Add a new bookshelf: ${bookshelfNewName.value}`)
  const url = `${apiRoot}/bookshelves`
  await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: bookshelfNewName.value,
      description: bookshelfNewDescription.value,
    }),
  })
    .then((response) => {
      if (response.ok) {
        return response.json()
      } else {
        throw new Error(`Error occured: response status = ${response.status}`)
      }
    })
    .then(() => {
      clearBookshelfNew()
      getBookshelves()
    })
    .catch((error) => console.log(error))
}

const cancel = () => {
  clearBookshelfNew()
}

const clearBookshelfNew = () => {
  bookshelfNewName.value = null
  bookshelfNewDescription.value = null
}

getBookshelves()
</script>
