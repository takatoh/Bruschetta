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
        <q-input name="category" v-model="book.category" label="Category"></q-input>
        <q-input name="format" v-model="book.format" label="Format"></q-input>
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
        <q-input name="bookshelf" v-model="book.bookshelf" label="Bookshelf"></q-input>
      </q-card-section>
      <q-card-actions align="right">
        <q-btn outline class="text-teal" label="Cancel" v-close-popup @click="onCancel"></q-btn>
        <q-btn outline class="text-teal" label="Submit" v-close-popup @click="onSubmit"></q-btn>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  label: {
    type: String,
    require: true,
  },
})

const book = ref({
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

const emit = defineEmits(['submit', 'cancel'])

const onCancel = () => {
  emit('cancel')
}

const onSubmit = () => {
  emit('submit')
}
</script>
