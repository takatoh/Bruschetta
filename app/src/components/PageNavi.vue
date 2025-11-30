<template>
  <q-pagination
    :model-value="props.currentPage"
    color="teal"
    :max="props.maxPage"
    :max-pages="9"
    @update:model-value="jumpPage"
    boundary-numbers
  ></q-pagination>
</template>
<script setup>
const props = defineProps({
  currentPage: {
    type: Number,
    required: true,
  },
  maxPage: {
    type: Number,
    required: true,
  },
})

const jumpPage = () => {}
</script>
