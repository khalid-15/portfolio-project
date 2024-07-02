<template>
  <v-app>
    <!-- Navbar -->
    <AppNavbar @toggle-drawer="toggleDrawer" />

    <!-- Sidebar -->
    <AppSidebar :drawer="drawer" @update-drawer="updateDrawer" />

    <!-- Main Content -->
    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import AppNavbar from '@/components/AppNavbar.vue';
import AppSidebar from '@/components/AppSidebar.vue';

export default {
  name: 'DefaultLayout',
  components: {
    AppNavbar,
    AppSidebar
  },
  data() {
    return {
      drawer: true,
    };
  },
  methods: {
    toggleDrawer() {
      this.drawer = !this.drawer;
    },
    updateDrawer(value) {
      this.drawer = value;
    }
  }
};
</script>

<style scoped>
.v-main {
  background-color: #f5f5f5;
}
</style>
