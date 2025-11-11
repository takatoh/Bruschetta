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
        <q-btn label="Add a new category" color="teal" outline></q-btn>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const categories = ref([])

const categoryColumns = [
  { name: 'id', label: 'ID', align: 'left', field: (row) => row['id'], format: (val) => `${val}` },
  { name: 'name', label: 'Name', align: 'left', field: 'name' },
]

const getCategories = async () => {
  const apiRoot = process.env.VUE_APP_API_ROOT
  const url = `${apiRoot}/categories`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => (categories.value = result.categories))
}

getCategories()
</script>
