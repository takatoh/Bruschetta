<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md col items-start q-gutter-md">
      <q-card flat bordered class="q-pa-sm" style="width: 600px">
        <q-card-section class="q-pa-none col-2">
          {{ books[1].id }}
        </q-card-section>
        <q-card-section class="q-pa-none col-5">
          {{ books[1].title }}
        </q-card-section>
        <q-card-section class="q-pa-none col-5">
          {{ books[1].author }}
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const books = ref([
  { id: 1, title: 'The One', author: 'Andy' },
  { id: 2, title: 'Seconds', author: 'Bill' },
  { id: 3, title: 'The Third Man', author: 'Charlie' },
])
</script>
