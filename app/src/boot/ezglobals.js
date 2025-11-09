import { defineBoot } from '#q-app/wrappers'

// "async" is optional;
// more info on params: https://v2.quasar.dev/quasar-cli-vite/boot-files
export default defineBoot(async ({ app }) => {
  // something to do
  app.config.globalProperties.$APP_NAME = 'Bruschetta-dev'
  app.config.globalProperties.$PROJECT_NAME = 'Bruschetta'
  app.config.globalProperties.$PROJECT_VERSION = 'develop'
})
