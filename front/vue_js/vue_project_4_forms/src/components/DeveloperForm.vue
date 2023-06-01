<script setup>
import AppInput from './AppInput.vue'
</script>


<template>
    <div class="form__container">
        <!-- submit.prevent - для отмены обновления страницы -->
        <form class="form__box" @submit.prevent="submitHandler"> 

            <!-- Имя -->
            <h1> {{ title }}</h1>
            <div class="form__control">
                <label for="name">Имя</label>
                <input type="text" 
                id="name" 
                placeholder="Введите имя" 
                v-model.trim="userData.name">
            <small v-if="userData.errors.name"> {{ userData.errors.name }} </small>
            </div>

            <!-- Кастомный компонент -->
            <AppInput 
            :placeholder="customComponent.placeholder" 
            :error="customComponent.error"
            :label="customComponent.label"
            v-model="userData.surname" />

            <!-- Возраст -->
            <div class="form__control">
                <label for="age">Возраст</label>
                <input type="number" name="age" id="20" v-model.number="userData.age" max="90">
            </div>

            <!-- Город -->
            <div class="form__control">
                <label for="city">Город</label>
                <select id="city" v-model="userData.city">
                    <option v-for="city in cities" 
                    :key="city.value"
                    v-text="city.name"
                    :value="city.value"></option>
                </select>
            </div>

            <!-- Переезд -->
            <div class="form__checkbox">
                <span class="label">Готов к переезду?</span>
                <div class="checkbox">
                    <input type="radio" v-model.number="userData.relocate" value="1" name="trip"/>
                    <label>Да</label>
                </div>
                <div class="checkbox">
                    <input type="radio" v-model.number="userData.relocate" value="0" name="trip"/>
                    <label>Нет</label>
                </div>
            </div>

            <!-- Навыки -->
            <div class="form__checkbox">
                <span class="label">Что знаешь?</span>
                <div class="checkbox" v-for="skill in skills" :key="skill">
                    <input type="checkbox" v-model="userData.skills" :value="skill" name="skills"/>
                    <label>{{ skill }}</label>
                </div>
            </div>

            <!-- Правила -->
            <div class="form__checkbox">
                <span class="label">Согласен ли с правилами?</span>
                <div class="checkbox">
                    <label>Да</label>
                    <input type="checkbox" name="agree" v-model="userData.agree">
                </div>
            </div>
            
            <!-- Кнопка -->
            <button type="submit" class="btn primary">Отправить</button>            
        </form>
    </div>
</template>

<script>

export default {
  components: { AppInput },
    props: ['title'],
    data() {
        return {
            customComponent: {
                error: false,
                label: 'Кастомный компонент',
                placeholder: "Фамилия",
            },
            userData: {
                name:'',
                age:20, 
                surname:'',
                city:'nsk',
                relocate: null,
                skills: [], 
                agree: false,
                errors: {
                    name: false
                }
            },
            cities: [
                {
                    value:'spb',
                    name:'Санкт-Петербург'
                }, 
                {
                    value:'msk',
                    name:'Москва'
                }, 
                {
                    value:'kzn',
                    name:'Казань'
                }, 
                {
                    value:'nsk', 
                    name:'Новосибирск'
                }, 
            ],
            skills: [
                'Vuex', 'Vue ClI', 'Vue Router', 'Python'
            ]
        }
    },methods: {
        submitHandler() {
            if (this.formIsValid()) {
                console.log('name = ', this.userData.name)
                console.log('age = ', this.userData.age)
                console.log('city = ', this.userData.city)
                console.log('relocate = ', this.userData.relocate)
                console.log('skills = ', this.userData.skills)
                console.log('agree = ', this.userData.agree)
                console.log('surname = ', this.userData.surname)
                this.userData = {name:'',age:20,city:'nsk', relocate: null, skills: [], agree: false, errors: {name:false}, surname: ''}
            }
        },
        formIsValid() {
        if (this.userData.name.length) {
            return true
        }
        this.userData.errors.name = 'Имя не может быть пустым'
        return false
    }
    }
}
</script>

<style lang="sass">
small 
    
    color: red
    position: relative
    bottom: -30px
    right: 280px

.checkbox 
    & label 
        padding-left: 7px
    
.form 
    &__container
        padding: 25px
        background: white
    &__control 
        position: relative
        margin-bottom: 25px
        display: flex
        flex-wrap: wrap
        & label 
            min-width: 220px
            text-align: right
            padding-right: 12px
            font-size: 1.1rem
            position: relative 
            top: 2px

        & select, input
            padding: 3px 12px
            border-radius: 7px
            font-size: 1rem
            min-width: 250px
            background: white
        & select 
            min-width: 280px

    &__checkbox
        display: flex
        flex-direction: column
        gap: 7px
        margin-bottom: 15px

.label 
    font-style: italic
    font-weight: bold

.btn 
    font-size: 1.2rem
    padding: 7px 12px
    border-radius: 12px
    box-shadow: 1px 5px 15px rgba(0,100,0,0.3)
    background: white
    transition: 0.2s
    &:hover
        box-shadow: 1px 5px 15px rgba(0,100,0,0.1)


.primary
    border: 1px solid darkgreen 
    color: darkgreen 


</style>

