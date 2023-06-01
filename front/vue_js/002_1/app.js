const App = {
    data() { // Создание данных для работы с vue
        return {
            counter: 0, // Начальное значение переменной
            title: 'Счётчик' 
        }
    }
}


const app = Vue.createApp(App) 

app.mount('#app') // Передаю тот объект, который будет наблюдаться vue.js





// Вариант короче
// Vue.createApp(App).mount('#app')
