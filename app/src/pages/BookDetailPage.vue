<template>
  <q-page padding>
    <h5 class="text-teal-10">{{ titleWithVolume }}</h5>

    <div v-if="book.coverart.length > 0">
      <img :src="book.coverart" />
    </div>

    <div class="q-pa-md" style="min-width: 600px">
      <q-list>
        <q-item>
          <q-item-section>
            <q-item-label overline>ID</q-item-label>
            <q-item-label>{{ book.id }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Title</q-item-label>
            <q-item-label>{{ book.title }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Volume</q-item-label>
            <q-item-label>{{ book.volume }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Series</q-item-label>
            <q-item-label>{{ book.series }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Series volume</q-item-label>
            <q-item-label>{{ book.seriesVolume }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Author</q-item-label>
            <q-item-label>{{ book.author }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Translator</q-item-label>
            <q-item-label>{{ book.translator }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Publisher</q-item-label>
            <q-item-label>{{ book.publisher }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Category</q-item-label>
            <q-item-label>{{ book.category }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Format</q-item-label>
            <q-item-label>{{ book.format }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>ISBN</q-item-label>
            <q-item-label>{{ book.isbn }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Published on</q-item-label>
            <q-item-label>{{ book.publishedOn }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Original title</q-item-label>
            <q-item-label>{{ book.originalTitle }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Note</q-item-label>
            <q-item-label>{{ book.note }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Keyword</q-item-label>
            <q-item-label>{{ book.keyword }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Disc</q-item-label>
            <q-item-label>{{ book.disc }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Bookshelf</q-item-label>
            <q-item-label>{{ book.bookshelf }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Created at</q-item-label>
            <q-item-label>{{ book.createdAt }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </div>

    <div class="q-pa-md q-gutter-y-md column items-start">
      <q-btn-group outline>
        <q-btn label="Edit" color="teal" outline v-close-popup @click="openEditingDialog"></q-btn>
        <q-separator></q-separator>
        <q-btn label="Upload coverart" color="teal" outline href="/" v-if="!book.coverart"></q-btn>
        <q-btn label="Delete coverart" color="teal" outline href="/" v-else></q-btn>
      </q-btn-group>
    </div>
  </q-page>

  <book-editing-dialog
    v-model="editingDialogOpen"
    label="Editing a Book"
    :book-details="book"
    @submit="updateBook"
    @cancel="cancel"
  ></book-editing-dialog>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { apiRoot } from 'boot/ezglobals'
import BookEditingDialog from 'components/BookEditingDialog.vue'

const props = defineProps({
  bookId: {
    type: String,
    required: true,
  },
})

const book = ref({
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
})

const titleWithVolume = computed(() => {
  if (book.value.volume.length > 0) {
    return book.value.title + ' [' + book.value.volume + ']'
  } else {
    return book.value.title
  }
})

const getBookDetails = async (bookId) => {
  const url = `${apiRoot}/books/${bookId}`
  await fetch(url)
    .then((response) => response.json())
    .then((result) => (book.value = result.books[0]))
}

const editingDialogOpen = ref(false)

const openEditingDialog = () => {
  editingDialogOpen.value = !editingDialogOpen.value
}

const updateBook = async (e) => {
  console.log(e)
  const url = `${apiRoot}/books/${e.id}`
  await fetch(url, {
    method: 'PUT',
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
    .then((result) => {
      book.value = result.books[0]
    })
    .catch((error) => console.log(error))
}

const cancel = () => {}

getBookDetails(props.bookId)

watch(
  () => props.bookId,
  (newBookId) => {
    getBookDetails(newBookId)
  },
)
</script>
