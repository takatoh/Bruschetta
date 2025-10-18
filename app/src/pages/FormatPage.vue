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
        <q-btn label="Add a new format" color="tead" outline></q-btn>
      </div>
    </div>
    "
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const formats = ref([
  { id: 1, name: 'bunko' },
  { id: 2, name: 'B6' },
  { id: 3, name: 'A5' },
  { id: 4, name: 'B5' },
  { id: 5, name: 'A4' },
])

const formatColumns = [
  { name: 'id', label: 'ID', align: 'left', field: (row) => row['id'], format: (val) => `${val}` },
  { name: 'name', label: 'Name', align: 'left', field: 'name' },
]
</script>
