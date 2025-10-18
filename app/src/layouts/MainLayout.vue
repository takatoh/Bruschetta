<template>
  <q-layout view="hHh lpR fFf">
    <q-header bordered>
      <div class="bg-teal-9 q-px-xl q-py-sm">
        <q-toolbar>
          <q-toolbar-title class="text-center"> Bruschetta </q-toolbar-title>
        </q-toolbar>
      </div>
      <div>
        <q-tabs class="bg-white text-teal-9 q-px-xl q-py-sm">
          <q-route-tab flat label="Books" to="/"></q-route-tab>
          <q-route-tab flat label="Add" to="/"></q-route-tab>
          <q-route-tab flat label="Categories" to="/categories"></q-route-tab>
          <q-route-tab flat label="Formats" to="/formats"></q-route-tab>
          <q-route-tab flat label="Bookshelves" to="/"></q-route-tab>
          <q-route-tab flat label="Disposed" to="/"></q-route-tab>
        </q-tabs>
      </div>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer bordered class="bg-teal text-white q-px-xl q-py-sm text-center">
      <q-toolbar>
        <q-space></q-space>
        <text-subtitle2 class="q-px-sm">Bruschetta</text-subtitle2>
        <q-badge class="bg-white text-teal q-px-sm">deveop</q-badge>
        <q-space></q-space>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup></script>
