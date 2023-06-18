<template>
    <div>
        <h1> {{  title }}</h1>
        <button class="btn" @click="$emit('show_message')">Show message</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            title: "hello world".toUpperCase()
        }
    },
}
</script>


<style lang="sass">

.btn 
    display: inline-block
    box-sizing: border-box
    font-size: 20px
    line-height: 20px
    padding: 10px 20px
    margin: 0
    border: 2px solid rgba(100, 255, 100, 0.2)
    border-radius: 40px
    background: rgba(235, 255, 235, 1)
    transition: 0.2s
    &:hover
        background: rgba(235, 255, 235, 0.8)
        box-shadow: 1px 5px 15px rgba(200, 255, 200, 0.3)
        

</style>