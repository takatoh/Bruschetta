<template>
  <q-page padding>
    <h5 class="text-teal-10">Books</h5>

    <div class="row q-pa-sm" style="width: 600px">
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
      <q-space></q-space>
      <q-btn
        outline
        class="text-teal"
        label="Add a New Book"
        v-close-popup
        @click="openAddingDialog"
      ></q-btn>
    </div>

    <div class="q-pa-md flex">
      <page-navi :current-page="currentPage" :max-page="maxPage"></page-navi>
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

    <div class="q-pa-md flex">
      <page-navi :current-page="currentPage" :max-page="maxPage"></page-navi>
    </div>
  </q-page>

  <book-adding-dialog
    v-model="addingDialogOpen"
    label="Add a New Book"
    @submit="addBook"
    @cancel="cancel"
  ></book-adding-dialog>
</template>

<script setup>
import { ref } from 'vue'
import BookListingItem from 'components/BookListingItem.vue'
import BookAddingDialog from 'src/components/BookAddingDialog.vue'
import PageNavi from 'src/components/PageNavi.vue'
import { apiRoot } from 'boot/ezglobals'

const PER_PAGE = 10

const books = ref([])
const addingDialogOpen = ref(false)
const currentPage = ref(6)
const maxPage = ref(27)

const getBooks = async (page = 1) => {
  const limit = PER_PAGE
  const offset = PER_PAGE * (page - 1)
  const params = new URLSearchParams()
  params.append('reverse', 'true')
  params.append('limit', limit)
  params.append('offset', offset)
  const url = `${apiRoot}/books?${params}`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => {books.value = result.books
      currentPage.value = page
      maxPage.value = Math.ceil(result.totalCount / PER_PAGE)
    })
}

const openAddingDialog = () => {
  addingDialogOpen.value = !addingDialogOpen.value
}

const addBook = async (e) => {
  console.log(e)
  const url = `${apiRoot}/books`
  await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(e),
  })
    .then((response) => {
      if (response.ok) {
        return response.json()
      } else {
        throw new Error(`Error occured: response status = ${response.status}`)
      }
    })
    .then(() => {
      getBooks()
    })
    .catch((error) => console.log(error))
}

const cancel = () => {}

getBooks()
</script>
