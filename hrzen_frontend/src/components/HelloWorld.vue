<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: 'Welcome to HRZen'
    }
  }
}
</script>

<style scoped>
h1 {
  font-size: 2em;
  margin: 20px 0;
}
</style>
