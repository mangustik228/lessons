<template lang="">
    <button class="btn" :class="color" @click="$emit('action')">
        {{ text }}
    </button>
</template>
<script>
export default {
    emits: ['action'],
    props: {
        text: String,
        color: {
            type: String,
            required: false,
            default: '',
            validator(value) {
                return ['','red','green','blue','primary','danger'].includes(value)
            }
        }
    },
}
</script>
<style lang="sass" scoped>
.btn
    color: btn
    &__simple
        font-family: monospace

.red
    color: red 
    bg: red 

.blue
    color: white 
    background: blue 

.danger 
    color: darkred 
    font-size: 2rem
</style>


<script>




</script>


