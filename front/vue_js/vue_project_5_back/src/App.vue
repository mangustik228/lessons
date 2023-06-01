<script setup>
import AppPeople from './components/AppPeople.vue';
import AppAlert from "./components/AppAlert.vue";
</script>

<template>
  <header>
    <h2> {{ title }}</h2>
  </header>


  <main>
    <app-alert 
    :alert='alert' @close='closeAlert'></app-alert>
    <form @submit.prevent="createPerson">
      <div class="form-control">
        <label for="name">Введите ваше имя</label>
        <input type="text" id="name" v-model.trim="name" :placeholder="placeholder">
      </div>
      <button 
      :class='{btn:true, primary:name}' 
      :disabled='!name'
      >Создать человека</button>
    </form>

    <AppPeople 
    :people='people' 
    @loadPeople="downloadPeople" 
    @delPerson="deletePerson"/>
  </main>

</template>


<script>
import axios from 'axios';
export default {
  data() {
    return {
      title: 'Работа с данными', 
      name: '',
      placeholder: 'Имя',
      people: [],
      alert: null 
    }
  },methods: {
    async createPerson(){
      const url = "http://127.0.0.1:8000/user" 
      let response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type" : "application/json" },
        body: JSON.stringify({ "name" : this.name })
      })
      console.log(await response.json())
      this.name = ''
      this.downloadPeople()
    },
    async downloadPeople () {
      const url = "http://127.0.0.1:8000/users"
      const data = await axios.get(url)
      this.people = data.data.slice(0,10)
      if (this.people.length === 0) {
        this.alert = {
          title: "Внимание!", 
          text: "От сервера пришел пустой ответ", 
          type: "danger"
        }
      }
    },
    async deletePerson(person_id){
    try {
      const url = "http://127.0.0.1:8000/user" 
      console.log(url)
      const idx = this.people.findIndex(el => el.id === person_id)
      const response = await fetch(url, {
        method: "DELETE",
        headers: {"Content-Type" : "application/json"},
        body: JSON.stringify(this.people[idx])
      })
      const result = await response.json()
      console.log(result)
      this.downloadPeople()
      return result
    } catch (error) {
      console.error('error:', error)
    }
  }, closeAlert () {
    this.alert = null 
  }
  },mounted() {
    this.downloadPeople()
  }
}
</script>

<style lang="sass">
form 
  padding: 2px
  border-radius: 10px
  padding-top: 15px
  display: flex
  flex-direction: column
  gap: 10px


.btn 
  flex-basis: content
  display: inline-block
  width: auto
  align-self: flex-start
  padding: 5px 10px 
  border-radius: 10px 
  background: white
  box-shadow: 1px 5px 15px rgba(255,255,255,0.3)
  transition: 0.2s
  font-size: 1rem
  font-family: monospace
  border: none
  &:hover 
    box-shadow: 1px 5px 15px rgba(255,255,255,0.05)
    
.primary
  color: darkgreen 
  border: 1px solid green 
  box-shadow: 1px 5px 15px rgba(0,100,0,2)

h2 
  font-size: 1.8rem
  margin-bottom: 15px
.form-control
  padding: 0
  margin: 0
  display: flex
  flex-direction: column
  & label 
    color: white
    font-size: 1rem
  & input 
    max-width: 460px
    outline: none
    padding: 7px
    border: none 
    border-radius: 8px
    box-shadow: 1px 5px 15px rgba(255,255,255,0.2)
    transition: 0.4s
    &:focus
      box-shadow: 1px 5px 15px rgba(255,255,255,0.5)
      outline: none 
      border: none 
      


</style>