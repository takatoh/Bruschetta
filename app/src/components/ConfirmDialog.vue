<template>
  <q-dialog persistent>
    <q-card style="width: 400px">
      <q-card-section class="bg-teal text-white text-center">
        <span>{{ props.label }}</span>
      </q-card-section>
      <q-card-section>
        <slot></slot>
      </q-card-section>
      <q-card-actions align="center">
        <q-btn outline class="text-teal" label="Cancel" v-close-popup @click="onCancel"></q-btn>
        <q-btn outline class="text-teal" label="Ok" v-close-popup @click="onOk"></q-btn>
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script setup>
const props = defineProps({
  label: {
    type: String,
    require: true,
  },
})

const emit = defineEmits(['ok', 'cancel'])

const onCancel = () => {
  emit('cancel')
}

const onOk = () => {
  emit('ok')
}
</script>
