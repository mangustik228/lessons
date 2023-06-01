const app = Vue.createApp({
    data() {
        return {
            title: 'I\'m title',
            myhtml: '<h1> Hello world <h2>', 
            hello: 'Hello', 
            person: {
                firstName: "Vasya",
                lastName: "Ovchinnikov",
                age: 27
            }, 
            items: ['a','b','c','d','e'], 
            items_num: [1,2,3,4,5,6,7,8]
        }
    },methods: {
        deleteItem(index){
            this.items.splice(index, 1)
        },addItem(event) {
            console.log(event.key)
            console.log(this.$refs.myInput.value)
            this.items.unshift(this.$refs.myInput.value)
            this.$refs.myInput.value = ''
        }
    },computed: {
        eventItems() {
            return this.items_num.filter(i => !(i % 2))
        }
    }
}).mount('#app')