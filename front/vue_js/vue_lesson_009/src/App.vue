<script setup>
import AppAlert from './components/AppAlert.vue'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <AppAlert 
  :title='"Attention"' 
  :text='"This is very import message"' 
  :type='type '
  :closable='closable'
  @close="closable = !closable"/>
  <header>
    <HelloWorld @show_message='showMessage'/>
  </header>

  <main>
  </main>
</template>

<script>
export default {
  data() {
    return {
      closable: true, 
      option_of_class: ['primary', 'danger', 'warning'],
      type: 'primary'
    }
  },
  methods: {
    showMessage() {
      this.closable = !this.closable
      const randomIndex = Math.floor(Math.random() * this.option_of_class.length);
      this.type = this.option_of_class.slice(randomIndex, randomIndex + 1)[0];
    }
  } 
}
</script>


<style scoped>
</style>
