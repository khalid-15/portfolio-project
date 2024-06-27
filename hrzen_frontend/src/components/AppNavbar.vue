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
    <v-btn icon>
      <v-icon>mdi-bell</v-icon>
    </v-btn>
  </v-app-bar>
</template>

<script>
export default {
  name: 'AppNavbar',
  data() {
    return {
      search: ''
    };
  }
};
</script>

<style scoped>
</style>