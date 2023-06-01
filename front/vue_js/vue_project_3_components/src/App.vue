<script setup>
import AppButton from './components/AppButton.vue'
</script>

<template>
  <div class="container">
    <h1> {{ title }}</h1>
    <AppButton 
    v-for="button in buttons" 
    :key="button" 
    :title="button" 
    :color="button === active ? 'active' : ''" 
    @action="checkAction"></AppButton>
  </div>
</template>


<script>
export default {
  data() {
    return {
      title: "Динамические и асинхронные компоненты",
      buttons: ['one', 'two'],
      active: 'one'
    }
  },methods: {
    checkAction(){
      this.active = (this.active === 'one') ? 'two' : 'one'
    }
  },
}
</script>

<style lang="sass">
</style>