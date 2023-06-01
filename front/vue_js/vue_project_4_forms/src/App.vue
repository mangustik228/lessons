<script setup>
import DeveloperForm from './components/DeveloperForm.vue'
</script>

<template>
  <header class="container">
    <h1> {{ title }}</h1>
    <div class="hello"></div>
  </header>

  <main class="container">
    <DeveloperForm/>
  </main>

  <footer class="container">
    <h2> {{ footer.toUpperCase() }}</h2>
  </footer>
</template>


<script>
export default {
  data() {
    return {
      title: 'header'.toUpperCase(),
      footer: 'footer'
    }
  },
}
</script>

