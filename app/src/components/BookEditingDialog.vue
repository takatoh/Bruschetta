<template>
  <q-dialog persistent>
    <q-card style="width: 600px">
      <q-card-section class="bg-teal text-white text-center">
        <span>{{ props.label }}</span>
      </q-card-section>
      <q-card-section>
        <q-input name="title" v-model="book.title" label="Title"></q-input>
        <q-input name="volume" v-model="book.volume" label="Volume"></q-input>
        <q-input name="series" v-model="book.series" label="Series"></q-input>
        <q-input name="series_volume" v-model="book.seriesVolume" label="Series volume"></q-input>
        <q-input name="author" v-model="book.author" label="Author"></q-input>
        <q-input name="translator" v-model="book.translator" label="Translator"></q-input>
        <q-input name="publisher" v-model="book.publisher" label="Publisher"></q-input>
        <q-select
          name="category"
          v-model="book.category"
          :options="categoryOptions"
          label="Category"
        ></q-select>
        <q-select
          name="format"
          v-model="book.format"
          :options="formatOptions"
          label="Format"
        ></q-select>
        <q-input name="isbn" v-model="book.isbn" label="ISBN"></q-input>
        <q-input name="published_on" v-model="book.publishedOn" label="Published on"></q-input>
        <q-input
          name="original_title"
          v-model="book.originalTitle"
          label="Original title"
        ></q-input>
        <q-input name="note" v-model="book.note" label="Note"></q-input>
        <q-input name="keyword" v-model="book.keyword" label="Keyword"></q-input>
        <q-input name="disk" v-model="book.disc" label="Disc"></q-input>
        <q-select
          name="bookshelf"
          v-model="book.bookshelf"
          :options="bookshelfOptions"
          label="Bookshelf"
        ></q-select>
      </q-card-section>
      <q-card-actions align="right">
        <q-btn outline class="text-teal" label="Cancel" v-close-popup @click="onCancel"></q-btn>
        <q-btn outline class="text-teal" label="Submit" v-close-popup @click="onSubmit"></q-btn>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref, watch } from 'vue'
import { apiRoot } from 'boot/ezglobals'

const props = defineProps({
  label: {
    type: String,
    require: true,
  },
  bookDetails: {
    type: Object,
    require: true,
  },
})

const bookInitial = () => {
  return {
    id: 0,
    title: '',
    volume: '',
    series: '',
    seriesVolume: '',
    author: '',
    translator: '',
    publisher: '',
    category: '',
    format: '',
    isbn: '',
    publishedOn: '',
    originalTitle: '',
    note: '',
    keyword: '',
    disc: '',
    bookshelf: '',
    createdAt: '',
    coverart: '',
  }
}

const book = ref(props.bookDetails)

const categoryOptions = ref([])
const formatOptions = ref([])
const bookshelfOptions = ref([])

const getCategories = async () => {
  const url = `${apiRoot}/categories`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => {
      categoryOptions.value = result.categories.map((c) => c['name'])
    })
}

const getFormats = async () => {
  const url = `${apiRoot}/formats`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => {
      formatOptions.value = result.formats.map((c) => c['name'])
    })
}

const getBookshelves = async () => {
  const url = `${apiRoot}/bookshelves`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => {
      bookshelfOptions.value = result.bookshelves.map((bs) => bs['name'])
    })
}

const emit = defineEmits(['submit', 'cancel'])

const onCancel = () => {
  const details = Object.assign({}, props.bookDetails)
  book.value = details
  emit('cancel')
}

const onSubmit = () => {
  const bookInfo = Object.assign({}, book.value)
  book.value = bookInitial()
  emit('submit', bookInfo, props.bookId)
}

getCategories()
getFormats()
getBookshelves()

watch(
  () => props.bookDetails,
  (newBookDetails) => {
    const details = Object.assign({}, newBookDetails)
    book.value = details
  },
)
</script>
