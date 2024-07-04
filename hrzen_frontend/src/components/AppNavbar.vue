<template>
  <v-app-bar app color="primary" dark>
    <v-btn icon @click="$emit('toggle-drawer')">
      <v-icon>mdi-menu</v-icon>
    </v-btn>
    <v-toolbar-title>HRZen</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn class="custom-btn" @click="goToHome">Home</v-btn>
    <v-btn class="custom-btn" @click="goToFeatures">Features</v-btn>
    <v-btn class="custom-btn" @click="goToAbout">About</v-btn>
    <v-btn class="custom-btn" @click="goToLogin" v-if="!isLoggedIn">Login</v-btn>
    <v-btn class="custom-btn" @click="goToRegister" v-if="!isLoggedIn">Register</v-btn>
    <v-btn class="custom-btn" @click="logout" v-if="isLoggedIn">Logout</v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: 'AppNavbar',
  data() {
    return {
      search: ''
    };
  },
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem('token');
    }
  },
  methods: {
    goToHome() {
      this.$router.push({ name: 'HomePage' });
    },
    goToFeatures() {
      this.$router.push({ path: '/', hash: '#features' });
    },
    goToAbout() {
      this.$router.push({ path: '/', hash: '#about' });
    },
    goToLogin() {
      this.$router.push({ name: 'Login' });
    },
    goToRegister() {
      this.$router.push({ name: 'Register' });
    },
    logout() {
      localStorage.removeItem('token');
      localStorage.removeItem('role');
      this.$router.push({ name: 'HomePage' });
    }
  }
};
</script>

<style scoped>
.custom-btn {
  color: #E0E1DD;
}

.v-app-bar {
  background-color: #0D1B2A !important;
}
</style>
