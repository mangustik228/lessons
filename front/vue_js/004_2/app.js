const h = Vue.h 

console.log('start app')

const app = Vue.createApp({
    data() {
        return {title: "hello world"}
    }, methods: {
        change_title: () => this.title = 'Изменили'
    }, beforeCreate() {
        console.log('hello world from before create')
    }, beforeMount() {
        console.log('hello world from before mount')
    }, mounted() {
        console.log('hello world from mounted')
    }, beforeUnmount() {
        console.log('unmounted')
    }, beforeDestroy() {
        console.log('destroed')
    }, beforeUpdate() {
        console.log('before update')
    }, updated() {
        console.log('updated')
    },
})


console.log('app init, but not mounted')

app.mount('#app')

console.log('finish init')

console.log('start unmounted after 2sec')

setTimeout(app.unmount, 15000)

