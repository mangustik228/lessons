<template>
  <div class="custom-input form__control">
    <label for="name">{{ label }}</label>
    <input type="text"
    id="name"
    :placeholder="placeholder"
    :surname="modelValue"
    @input="onChange"
    v-model.trim="surname"> 
    <small v-if="error">{{ error }}</small>
  </div>
</template>


<script>
export default {
    emits: ['update:modelValue'],
    props: {
        modelValue: String,
        error: Boolean,
        label: String,
        placeholder: String,
    },
    data() {
        return {
            id: "input-" + Math.random(),
            surname: ""
        }
    },methods: {
        onChange(event){
            this.$emit('update:modelValue', event.target.value)
        }
    },
}
</script>


<style lang="sass">

</style>