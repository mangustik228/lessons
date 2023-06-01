<template>
    <button class="btn" :class="color" @click="checkStatus && $emit('action')">{{ title }}</button>
</template>


<script>
export default {
    emets: ['action'],
    props: {
        title:String,
        color:String
    },
    computed: {
        checkStatus () {
            return !(this.color === 'active')
        }
    }
}
</script>
<style lang="sass">
.btn 
    font-size: 2rem
    margin: 12px
    border-radius: 12px
    padding: 5px 15px
    font-family: monospace
    background: grey 
    border: 1px solid grey 
    transition: 0.2s
    text-shadow: 1px 2px 5px rgba(255, 255, 255, 0.2)
    box-shadow: 1px 5px 15px rgba(255, 255, 255, 0.1)
    &:hover
      box-shadow: 1px 5px 15px rgba(255, 255, 255, 0.35)  

.active
    box-shadow: 1px 5px 15px rgba(255, 255, 255, 0.4)
    color: darkgreen  


</style>