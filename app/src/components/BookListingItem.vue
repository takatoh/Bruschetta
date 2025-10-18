<template>
  <q-card flat bordered class="q-pa-sm" style="width: 600px">
    <q-card-section class="q-pa-none col-2">
      {{ props.bookId }}
    </q-card-section>
    <q-card-section class="q-pa-none col-5">
      {{ props.title }}
    </q-card-section>
    <q-card-section class="q-pa-none col-5">
      {{ props.author }}
    </q-card-section>
  </q-card>
</template>

<script setup>
const props = defineProps({
  bookId: {
    type: Number,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  author: {
    type: String,
    default: '',
  },
})
</script>
