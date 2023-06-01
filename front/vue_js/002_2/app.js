const App = {
    data() { // Создание данных для работы с vue
        return {
            title: 'Список заметок',
            placeholder: 'Введите название заметки', 
            inputValue: '',
            notes: ['Заметка 1', 'Заметка 2']
        }
    },
    methods: {
        // inputChangeHandler(event){
        //     this.inputValue = event.target.value // Обращение к записи
        // },
        addNewNote(event){
            if (this.inputValue){
                this.notes.push(this.inputValue),
                this.inputValue = ''
            }
        },
        toUpperCase(item){
            return item.toUpperCase()
        },
        deleteNote(index){
            this.notes.splice(index, 1)
        }

    },
    computed: {
        doubleCountComputed() {
            console.log('computed double')            
            return this.notes.length * 2 
        }
    },
    watch: {
        inputValue(value) { // Должно совпадать с именем переменной за которой следит
            if (value.length > 10) {
                this.inputValue = ''
            }
            console.log('input value changed')
        }
    }
}


const app = Vue.createApp(App) 

app.mount('#app') // Передаю тот объект, который будет наблюдаться vue.js





// Вариант короче
// Vue.createApp(App).mount('#app')
