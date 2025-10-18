<template>
  <q-page padding>
    <h5 class="text-teal-10">Books</h5>
    <div class="q-pa-sm col items-start">
      <q-list class="q-gutter-md">
        <book-listing-item
          v-for="book in books"
          :key="book.id"
          :book-id="book.id"
          :title="book.title"
          :author="book.author"
        ></book-listing-item>
      </q-list>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import BookListingItem from 'components/BookListingItem.vue'

const books = ref([
  { id: 1, title: 'The One', author: 'Andy' },
  { id: 2, title: 'Seconds', author: 'Bill' },
  { id: 3, title: 'The Third Man', author: 'Charlie' },
])
</script>
