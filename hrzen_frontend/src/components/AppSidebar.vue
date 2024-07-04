<template>
  <v-navigation-drawer app v-model="drawerInternal" permanent v-if="isLoggedIn" class="custom-sidebar">
    <v-list dense>
      <v-list-item v-if="isManager" to="/employees" router>
        <v-list-item-icon>
          <v-icon color="white">mdi-account</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="white--text">Employees</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="isManager" to="/attendance/hr" router>
        <v-list-item-icon>
          <v-icon color="white">mdi-checkbox-marked-circle-outline</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="white--text">Attendance (HR)</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="isEmployee" to="/attendance" router>
        <v-list-item-icon>
          <v-icon color="white">mdi-checkbox-marked-circle-outline</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="white--text">My Attendance</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item to="/calendar" router>
        <v-list-item-icon>
          <v-icon color="white">mdi-calendar</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="white--text">Calendar</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-if="isManager" to="/payroll" router>
        <v-list-item-icon>
          <v-icon color="white">mdi-cash</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="white--text">Payroll</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
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
  computed: {
    drawerInternal: {
      get() {
        return this.drawer;
      },
      set(value) {
        this.$emit('update-drawer', value);
      }
    },
    isLoggedIn() {
      return !!localStorage.getItem('token');
    },
    isManager() {
      return localStorage.getItem('role') === 'manager';
    },
    isEmployee() {
      return localStorage.getItem('role') === 'employee';
    }
  }
};
</script>

<style scoped>
.custom-sidebar {
  background-color: #0D1B2A !important;
}
.white--text {
  color: white !important;
}
</style>
