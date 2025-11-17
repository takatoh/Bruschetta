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
          :volume="book.volume"
          :author="book.author"
        ></book-listing-item>
      </q-list>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import BookListingItem from 'components/BookListingItem.vue'
import { apiRoot } from 'boot/ezglobals'

console.log(apiRoot)

const books = ref([])

const getBooks = async () => {
  //  const apiRoot = 'http://localhost:5000/api/v2'
  //  const apiRoot = process.env.VUE_APP_API_ROOT
  const params = new URLSearchParams()
  params.append('reverse', 'true')
  const url = `${apiRoot}/books?${params}`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => (books.value = result.books))
}

getBooks()
</script>
