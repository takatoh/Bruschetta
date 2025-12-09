const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', redirect: { name: 'books' } },
      {
        path: 'books',
        name: 'books',
        component: () => import('pages/IndexPage.vue'),
        props: (route) => ({ page: Number(route.query.page) }),
      },
      { path: 'categories', name: 'categories', component: () => import('pages/CategoryPage.vue') },
      { path: 'formats', name: 'formats', component: () => import('pages/FormatPage.vue') },
      {
        path: 'bookshelves',
        name: 'bookshelves',
        component: () => import('pages/BookshelfPage.vue'),
      },
      { path: 'book/:bookId', component: () => import('pages/BookDetailPage.vue'), props: true },
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
