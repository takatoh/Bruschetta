const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: 'categories', component: () => import('pages/CategoryPage.vue') },
      { path: 'formats', component: () => import('pages/FormatPage.vue') },
      { path: 'bookshelves', component: () => import('pages/BookshelfPage.vue') },
      { path: 'book/1', component: () => import('pages/BookDetailPage.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
]

export default routes
