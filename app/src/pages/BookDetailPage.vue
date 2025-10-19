<template>
  <q-page padding>
    <h5 class="text-teal-10">{{ book.title }}</h5>

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
            <q-item-label>{{ book.category.name }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Format</q-item-label>
            <q-item-label>{{ book.format.name }}</q-item-label>
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
            <q-item-label>{{ book.disk }}</q-item-label>
          </q-item-section>
        </q-item>
        <q-item>
          <q-item-section>
            <q-item-label overline>Bookshelf</q-item-label>
            <q-item-label>{{ book.bookshelf.name }}</q-item-label>
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
  </q-page>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  bookId: {
    type: Number,
    required: true,
  },
})

const book = ref({
  id: 1,
  title: 'The One',
  volume: '',
  series: '',
  seriesVolume: '',
  author: 'Andy',
  translator: '',
  publisher: '',
  category: {
    name: 'novel',
  },
  format: {
    name: 'bunko',
  },
  isbn: '',
  publishedOn: '',
  originalTitle: '',
  note: '',
  keyword: '',
  disk: '',
  bookshelf: {
    name: '',
  },
  createdAt: '',
})
</script>
