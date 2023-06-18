import './assets/main.css'
import translatePlugin from './plugins/translatePlugin'
import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

const ru = {
  app: {
    title: 'Как работают плагины во vue',
    changeLang: 'Поменять язык'
  }
}

const en = {
  app: {
    title: 'How to working plugins in vue',
    changeLang: 'Change lang'
  }
}

app.use(translatePlugin, { ru, en })

app.mount('#app')
