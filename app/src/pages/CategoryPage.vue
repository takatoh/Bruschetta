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
        <q-btn label="Add a new category" color="tead" outline></q-btn>
      </div>
    </div>
    "
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const categories = ref([
  { id: 1, name: 'manga' },
  { id: 2, name: 'novel' },
  { id: 3, name: 'sience' },
])

const categoryColumns = [
  { name: 'id', label: 'ID', align: 'left', field: (row) => row['id'], format: (val) => `${val}` },
  { name: 'name', label: 'Name', align: 'left', field: 'name' },
]
</script>
