<script setup>
import {ref} from 'vue'
import HelloWorld from './components/HelloWorld.vue'
import focusDirective from './components/focusDirective.js'
import colorDirective from './components/colorDirective.js'

const title = ref('First title of page')
const colorTitle = ref('darkred')

</script>
<template>
  <div class="container">
    <div class="card">
      <h2 v-color.blink='colorTitle'> {{ title }} </h2>
      <hello-world msg="hello worldl"/>
      <button @click='title="JOPA"' class="btn">Change title of page</button>
      <div class="form-control">
        <label for="forma">Active by default</label>
        <input v-focus type="text" id="forma">
      </div>
    </div>
  </div>
  <button class="btn" @click="colorTitle = 'darkgreen'">make green</button>
</template>


<script>

export default {
  directives: {
    focus: focusDirective,
    color: colorDirective
  }
}
</script>

<style lang="sass">
.btn 
  margin-bottom: 3rem
.form-control
  display: flex
  flex-direction: column
  text-align: center
  & input 
    padding: 5px 
</style>


<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>


