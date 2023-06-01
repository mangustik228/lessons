<script>
export default {
    props: {
        item:{
            type:Object,
            validator(value){
                if (value.title.includes('')){
                    console.log('ok')
                    return true
                } else {
                    console.log('false')
                    return false
                }
            }
        }
    }, 
    data() {
        return {
            visible: this.item.visible
        }
    },
    methods: {
        openItem () {
            this.visible = !this.visible
            if (this.visible) {
                this.$emit('open-news') // Метод для возврата родителю 
            }
        }
    },
};
</script>

<template>
    <li class="item">
        <div class="item__wrapper">
            <!-- <strong>{{ item.title }}</strong> -->
            <strong> {{ item.title }}</strong>
            <p v-if="visible"> {{ item.text }} </p>
            <div class="btn__wrapper">
                <button class="btn" v-on:click="openItem">Открыть</button>
            </div> 
        </div>
    </li>
</template>
