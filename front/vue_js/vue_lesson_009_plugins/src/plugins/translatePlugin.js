export default {
  install(app, options) {
    let current_language = 'ru'

    const changeLanguage = (name) => {
      current_language = name
      console.log(`current language = ${current_language}`)
    }

    app.config.globalProperties.$i18n = (key) => {
      return key.split('.').reduce((words, k) => {
        return words[k] || '=== UNKNOWN ==='
      }, options[current_language])
    }

    app.provide('changeI18n', changeLanguage)
  }
}
