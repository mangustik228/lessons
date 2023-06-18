<template>
  <div class="container">
    <button class="btn" @click="$alert('Wow it is working!')">
      Alert
    </button>
    <h2>{{ $i18n("app.title") }}</h2>
    <button class="btn" @click="changeLang">{{ $i18n("app.changeLang") }}</button>
  </div>
</template>


<script>
export default {
  inject: ['changeI18n'], 
  methods: {
    changeLang() {
      this.changeI18n('en')
      this.$forceUpdate()
    }
  },
} 
</script>