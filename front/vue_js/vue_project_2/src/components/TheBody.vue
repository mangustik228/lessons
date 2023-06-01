<script setup>
import NewsItem from './NewsItem.vue'
import MyButton from './MyButton.vue'
</script>


<template>
    <main class="container container__main">
        <MyButton 
        :text="'Text for button'"
        :color="''"
        @action="changeColor"
         />
        <div class="header__news">
            <h2>Актуальные новости {{ now }}</h2>
            <span :class='{
                info: true,
                green: openRate,
                red: !openRate}'><span>{{ openRate }}</span></span>          
        </div>
        
        <hr/>
            <ul>
                <news-item v-for="item in news" :key="item.id" :item="item" v-on:open-news="openRate++"/>
            </ul>
    </main>
</template>

<script>
export default {
    data() {
        return {
            now: new Date().toLocaleDateString('th'),
            openRate: 0,
            colors: ['','red','green','blue','primary','danger'],
            news: [
                {
                    id: 1,
                    title: 'Путин сдох', 
                    text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque dicta ea itaque accusamus quidem ratione aliquid sint tempora, impedit reiciendis fugiat natus nemo odit totam, officia harum cum commodi numquam.',
                    visible: false
                }, 
                {
                    id: 2,
                    title: 'vue 3.3 вышел!', 
                    text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo necessitatibus, enim iure saepe perspiciatis eaque!',
                    visible: false
                }
            ]
        }
    },
    methods: {
        changeColor(){
            if (this.colors)
            console.log('Click on the button')
        }
    }
}
</script>


<style lang="sass">
.header__news 
    display: flex
    justify-content: space-between
.info
    position: relative
    height: 40px
    width: 40px
    border-radius: 50%
    padding-left: 5px
    font-size: 2rem
    display: inline-block
    & span 
        position: relative
        left: 8px
.green 
    border-radius: 50%
    color: green 
    border: 2px solid rgba(100,200,100,0.5)
    background: rgba(100,200,100,0.2)
.red 
    border-radius: 50%
    border: 2px solid rgba(200,100,100,0.5)
    background: rgba(200,100,100,0.2)
    color: red
    
.item 
    display: block
    margin-bottom: 15px
    border-bottom: 1px solid
    &__wrapper
        display: flex
        flex-direction: column
        

.btn
    padding: 7px 22px
    font-family: monospace
    border-radius: 10px 
    box-shadow: 1px 2px 15px grey
    transition: 0.2s
    color: green
    margin: 10px
    
    &:hover 
        box-shadow: 1px 1px 5px grey

ul 
    padding: 0
    margin: 0


h2  
    font-size: 2.4rem
    font-family: monospace       


</style>