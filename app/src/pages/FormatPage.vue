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
        <q-btn label="Add a new format" color="teal" outline @click="openDialog"></q-btn>
      </div>
    </div>

    <adding-dialog
      v-model="dialogOpen"
      label="Adding a New Format"
      @submit="addFormat"
      @cancel="cancel"
    >
      <q-input name="name" v-model="formatNew" label="Name" color="teal"></q-input>
    </adding-dialog>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { apiRoot } from 'boot/ezglobals'
import AddingDialog from 'src/components/AddingDialog.vue'

const formats = ref([])
const dialogOpen = ref(false)
const formatNew = ref(null)

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

const openDialog = () => {
  dialogOpen.value = !dialogOpen.value
}

const addFormat = async () => {
  console.log(`Add a new format: ${formatNew.value}`)
  const url = `${apiRoot}/formats`
  await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ name: formatNew.value }),
  })
    .then((response) => {
      if (response.ok) {
        return response.json()
      } else {
        throw new Error(`Error occured: response status = ${response.status}`)
      }
    })
    .then(() => {
      formatNew.value = null
      getFormats()
    })
    .catch((error) => console.log(error))
}

const cancel = () => {
  formatNew.value = null
}

getFormats()
</script>
