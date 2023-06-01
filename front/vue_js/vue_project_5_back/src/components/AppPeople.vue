<template>
    <div class="card__container">
        <div class="card" v-if="people.length === 0">
            <h4>Людей пока нет.</h4>
        </div>
        <button 
        class="btn primary" 
        v-if="people.length === 0"
        @click="$emit('loadPeople')">Загрузить человеков</button>
        <div class="card" v-for="(person, i) in people" :key="i">
            <span>{{ person.id }} - {{ person.name }}</span> 
            <span 
            v-if="person.age" 
            :class="
            {'text-green': person.age > 5, 
            'text-red': person.age <= 5}
            ">
            {{ person.age }} лет.</span>
            <button class="btn danger" @click="$emit('delPerson', person.id)">del</button>

        </div>
    </div>
</template>

<script>
export default {
    emits: ['loadPeople', 'delPerson'],
    props: ['people']
}
</script>

<style lang="sass" scoped>

.card 
    display: flex
    background: white 
    padding: 15px
    font-size: 1.4rem
    color: black 
    border-radius: 18px
    box-shadow: 2px 5px 10px rgba(255,255,255,0.2)
    &__container 
        display: flex
        flex-direction: column
        gap: 25px
        margin-top: 25px

.danger 
    margin-left: auto
    border: 1px solid red 
    color: red 
    border-radius: 15px
    background: rgba(255,100,100,0.1)
    box-shadow: 1px 2px 10px rgba(255,0,0,0.3)
    transition: 0.2s
    &::hover
        box-shadow: none

.text-green 
    margin-left: 15px
    color: darkgreen

.text-red 
    margin-left: 15px
    color: darkred
</style>