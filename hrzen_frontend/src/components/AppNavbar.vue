<template>
  <v-app-bar app color="primary" dark>
    <v-btn icon @click="$emit('toggle-drawer')">
      <v-icon>mdi-menu</v-icon>
    </v-btn>
    <v-toolbar-title>HRZen</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn class="custom-btn" @click="goToSection('#home')">Home</v-btn>
    <v-btn class="custom-btn" @click="goToSection('#features')">Features</v-btn>
    <v-btn class="custom-btn" @click="goToSection('#about')">About</v-btn>
    <v-btn class="custom-btn" @click="goToLogin">Login</v-btn>
    <v-btn class="custom-btn" @click="goToRegister">Register</v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: 'AppNavbar',
  methods: {
    goToSection(sectionId) {
      this.$router.push({ path: '/', hash: sectionId });
    },
    goToLogin() {
      this.$router.push({ name: 'Login' });
    },
    goToRegister() {
      this.$router.push({ name: 'Register' });
    }
  }
};
</script>

<style scoped>
.custom-btn {
  margin-left: 10px;
  background-color: #1976D2;
  color: white;
  border-radius: 8px;
  padding: 0 16px;
  transition: background-color 0.3s;
}

.custom-btn:hover {
  background-color: #1565C0;
}
</style>
