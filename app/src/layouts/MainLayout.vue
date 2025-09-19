<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated>
      <div>
        <q-toolbar>
          <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />
          <q-toolbar-title> Bruschetta </q-toolbar-title>
        </q-toolbar>
      </div>
      <div>
        <q-tabs class="q-gutter-lg">
          <q-route-tab flat label="Books" to="/"></q-route-tab>
          <q-route-tab flat label="Add" to="/"></q-route-tab>
          <q-route-tab flat label="Categories" to="/categories"></q-route-tab>
          <q-route-tab flat label="Formats" to="/"></q-route-tab>
          <q-route-tab flat label="Bookshelves" to="/"></q-route-tab>
          <q-route-tab flat label="Disposed" to="/"></q-route-tab>
        </q-tabs>
      </div>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> Essential Links </q-item-label>

        <EssentialLink v-for="link in linksList" :key="link.title" v-bind="link" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer boredered class="text-white">
      <q-toolbar>
        <div>Bruschetta</div>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

const linksList = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev',
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework',
  },
  {
    title: 'Discord Chat Channel',
    caption: 'chat.quasar.dev',
    icon: 'chat',
    link: 'https://chat.quasar.dev',
  },
  {
    title: 'Forum',
    caption: 'forum.quasar.dev',
    icon: 'record_voice_over',
    link: 'https://forum.quasar.dev',
  },
  {
    title: 'Twitter',
    caption: '@quasarframework',
    icon: 'rss_feed',
    link: 'https://twitter.quasar.dev',
  },
  {
    title: 'Facebook',
    caption: '@QuasarFramework',
    icon: 'public',
    link: 'https://facebook.quasar.dev',
  },
  {
    title: 'Quasar Awesome',
    caption: 'Community Quasar projects',
    icon: 'favorite',
    link: 'https://awesome.quasar.dev',
  },
]

const leftDrawerOpen = ref(false)

function toggleLeftDrawer() {
  leftDrawerOpen.value = !leftDrawerOpen.value
}
</script>
