<template>
  <q-page padding>
    <h5 class="text-teal-10">Books</h5>

    <div class="q-pa-sm">
      <q-input outlined dense v-model="searchText" style="width: 300px">
        <template v-slot:append>
          <q-icon
            v-if="searchText !== ''"
            name="close"
            @click="searchText = ''"
            class="cursor-pointer"
          ></q-icon>
          <q-icon name="search" @click="onSearchEnter" class="cursor-pointer"></q-icon>
        </template>
      </q-input>
    </div>

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

const getBooks = async () => {
  const apiRoot = 'http://localhost:5000/api/v2'
  const url = `${apiRoot}/books`
  console.log(url)
  await fetch(url)
    .then((response) => response.json())
    .then((result) => (books.value = result.books))
}

getBooks()
</script>
