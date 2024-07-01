<template>
  <v-app-bar app color="primary" dark>
    <v-btn icon @click="$emit('toggle-drawer')">
      <v-icon>mdi-menu</v-icon>
    </v-btn>
    <v-toolbar-title>HRZen</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-text-field
      v-model="search"
      append-icon="mdi-magnify"
      label="Search"
      single-line
      hide-details
      class="mx-4"
    ></v-text-field>
    <v-btn v-if="!isAuthenticated" text to="/login">Login</v-btn>
    <v-btn v-if="!isAuthenticated" text to="/register">Register</v-btn>
    <v-btn v-if="isAuthenticated" text @click="logout">Logout</v-btn>
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
    isAuthenticated() {
      return !!localStorage.getItem('token');
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token');
      localStorage.removeItem('role');
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
</style>
