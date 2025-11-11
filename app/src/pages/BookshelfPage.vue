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
        <q-btn label="Add a new format" color="teal" outline></q-btn>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const bookshelves = ref([])

const bookshelfColumns = [
  { name: 'id', label: 'ID', align: 'left', field: (row) => row['id'], format: (val) => `${val}` },
  { name: 'name', label: 'Name', align: 'left', field: 'name' },
  { name: 'description', label: 'Description', align: 'left', field: 'description' },
]

const getBookshelves = async () => {
  const apiRoot = process.env.VUE_APP_API_ROOT
  const url = `${apiRoot}/bookshelves`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => (bookshelves.value = result.bookshelves))
}

getBookshelves()
</script>
