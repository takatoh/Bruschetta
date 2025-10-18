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

const bookshelves = ref([
  { id: 1, name: 'Bookshelf 1', description: 'Big.' },
  { id: 2, name: 'Bookshelf 2', description: 'Middle' },
  { id: 3, name: 'Bookshelf 3', description: 'Small.' },
])

const bookshelfColumns = [
  { name: 'id', label: 'ID', align: 'left', field: (row) => row['id'], format: (val) => `${val}` },
  { name: 'name', label: 'Name', align: 'left', field: 'name' },
  { name: 'description', label: 'Description', align: 'left', field: 'description' },
]
</script>
