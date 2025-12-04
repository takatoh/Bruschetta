<template>
  <q-pagination
    :model-value="props.currentPage"
    :max="props.maxPage"
    :max-pages="9"
    @update:model-value="jumpPage"
    color="teal"
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

const emit = defineEmits(['pageJump'])

const jumpPage = (e) => {
  emit('pageJump', e)
}
</script>
