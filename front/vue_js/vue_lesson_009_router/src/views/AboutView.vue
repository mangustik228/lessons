<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button class="btn" @click="goHome">Go Home</button>
    <button class="btn" @click="goBack">Go Back</button>
  </div>
</template>

<script>
export default {
  methods: {
    goHome() {
      this.$router.push('/home')
    },
    goBack() {
      this.$router.back()
    }
  },
}
</script>


<style>
.btn {
  padding: 15px;
  border-radius: 5px;
  box-shadow: 1px 5px 15px rgba(224, 224, 224, 0.2);
  transition: 0.2s;
  margin: 15px; 
}
.btn:hover { 
  box-shadow: 1px 5px 15px rgba(224, 224, 224, 0.3);
}

@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
