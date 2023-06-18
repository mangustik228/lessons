<script setup>
import {reactive} from 'vue'


const texts = reactive({
    name: "This is texts.name",
})


function changeName () {
    texts.name = "this is new name "
}
</script>

<template>
    <div>
        This is block "HelloWorld"
    </div>
    <ul>
        <li>{{ texts.name }}</li>
    </ul>
    <button @click="changeName">Change 'name'</button>
</template>