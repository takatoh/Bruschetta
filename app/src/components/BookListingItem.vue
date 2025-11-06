<template>
  <q-card flat bordered class="q-pa-sm" style="width: 600px">
    <q-card-section class="q-pa-none col-2">
      {{ props.bookId }}
    </q-card-section>
    <q-card-section class="q-pa-none col-5">
      <router-link :to="'/book/' + bookId">{{ titleWithVolume() }}</router-link>
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
  volume: {
    type: String,
    default: '',
  },
  author: {
    type: String,
    default: '',
  },
})

const titleWithVolume = () => {
  if (props.volume.length > 0) {
    return `${props.title} [${props.volume}]`
  } else {
    return props.title
  }
}
</script>
