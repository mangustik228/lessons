<template>
  <div class="alert" :class='type' v-if="closable" @click="$emit('close')">
    <p class="alert__title">{{ title }}</p>
    <p> {{ text }} </p>
  </div>
</template>

<script>
export default {
  emits: ["close"],
  props: {
    title: String, 
    text: String, 
    closable: {
      type: Boolean,
      required: false,
      default: false
    },
    type: {
      type: String,
      default: 'primary',
      required: false, 
      validator(val){
        return ['primary','danger','warning'].includes(val)
      }
    },
  }
}
</script>

<style lang="sass">
.alert 
  background: rgba(255,255,255, 0.05)
  text-align: center
  padding: 15px
  margin: 15px
  border-radius: 15px
  transition: 0.2s
  &:hover
    background: rgba(255,255,255, 0.1)
    cursor: pointer
  &__title 
    font-size: 2rem
    &::after
      content: "!!!"


.warning
  color: red 

.danger
  color: green 

.primary
  color: white
</style>