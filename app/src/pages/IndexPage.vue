<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md col items-start q-gutter-md">
      <q-list>
        <template v-for="(book, index) in books" :key="index">
          <q-card flat bordered class="q-pa-sm" style="width: 600px">
            <q-card-section class="q-pa-none col-2">
              {{ book.id }}
            </q-card-section>
            <q-card-section class="q-pa-none col-5">
              {{ book.title }}
            </q-card-section>
            <q-card-section class="q-pa-none col-5">
              {{ book.author }}
            </q-card-section>
          </q-card>
        </template>
      </q-list>
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
