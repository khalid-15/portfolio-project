<template>
  <v-navigation-drawer app v-model="drawerInternal" permanent>
    <v-list dense>
      <v-list-item-group v-model="selectedItem" active-class="deep-blue--text text--accent-4">
        <v-list-item
          v-for="(item, index) in menuItems"
          :key="index"
          :to="item.route"
          router
          class="sidebar-item"
        >
          <v-list-item-icon>
            <v-icon color="primary">{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  name: 'AppSidebar',
  props: {
    drawer: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      selectedItem: 0,
      menuItems: [
        { title: 'Home', icon: 'mdi-home', route: '/' },
        { title: 'Employees', icon: 'mdi-account', route: '/employees' },
        { title: 'Attendance', icon: 'mdi-checkbox-marked-circle-outline', route: '/attendance' },
        { title: 'Calendar', icon: 'mdi-calendar', route: '/calendar' },
        { title: 'Payroll', icon: 'mdi-cash', route: '/payroll' },
      ]
    };
  },
  computed: {
    drawerInternal: {
      get() {
        return this.drawer;
      },
      set(value) {
        this.$emit('update-drawer', value);
      }
    }
  },
  watch: {
    $route(to) {
      this.selectedItem = this.menuItems.findIndex(item => item.route === to.path);
    }
  },
  mounted() {
    this.selectedItem = this.menuItems.findIndex(item => item.route === this.$route.path);
  }
};
</script>

<style scoped>
.v-navigation-drawer {
  background-color: #ffffff;
  border-right: 1px solid #e0e0e0;
}

.v-list-item-group .v-list-item {
  margin: 5px 10px;
  border-radius: 8px;
}

.v-list-item--active {
  background-color: #e3f2fd !important;
}

.v-list-item .v-icon {
  font-size: 1.25rem;
}

.sidebar-item {
  margin-bottom: 10px;
}
</style>
