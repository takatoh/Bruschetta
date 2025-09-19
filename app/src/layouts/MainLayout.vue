<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated>
      <div>
        <q-toolbar>
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

<script setup></script>
