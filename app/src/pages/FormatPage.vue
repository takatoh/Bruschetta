<template>
  <q-page padding>
    <!-- content -->
    <h5 class="text-teal-10">Formats</h5>

    <div class="q-pa-md">
      <q-table
        :rows="formats"
        :columns="formatColumns"
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
import { apiRoot } from 'boot/ezglobals'

const formats = ref([])

const formatColumns = [
  { name: 'id', label: 'ID', align: 'left', field: (row) => row['id'], format: (val) => `${val}` },
  { name: 'name', label: 'Name', align: 'left', field: 'name' },
]

const getFormats = async () => {
  const url = `${apiRoot}/formats`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => (formats.value = result.formats))
}

getFormats()
</script>
