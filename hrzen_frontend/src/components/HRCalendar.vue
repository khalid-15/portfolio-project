<template>
  <v-app>
    <v-container>
      <v-card>
        <v-card-title class="d-flex flex-row mb-6">
          Employees
          <v-spacer></v-spacer>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="employees"
          class="elevation-1"
        ></v-data-table>
      </v-card>
    </v-container>
  </v-app>
</template>

<script>
export default {
  name: 'EmployeeList',
  data() {
    return {
      employees: [
        {
          id: 1,
          name: 'John Doe',
          position: 'Developer',
          salary: 60000,
          email: 'john.doe@example.com',
        },
        {
          id: 2,
          name: 'Jane Smith',
          position: 'Manager',
          salary: 80000,
          email: 'jane.smith@example.com',
        },
      ],
      headers: [
        { text: 'ID', value: 'id' },
        { text: 'Name', value: 'name' },
        { text: 'Position', value: 'position' },
        { text: 'Salary', value: 'salary' },
        { text: 'Email', value: 'email' },
      ],
    };
  },
};
</script>

<style scoped>
.v-btn {
  margin-right: 8px; /* Add some margin between buttons */
}

.v-card-title {
  background-color: #E8EAF6; /* secondary color */
  color: black; /* Ensure the text is readable on the background */
}
</style>

<style scoped>
.v-btn {
  margin-right: 8px; /* Add some margin between buttons */
}

.v-card-title {
  background-color: #E8EAF6; /* secondary color */
  color: black; /* Ensure the text is readable on the background */
}
</style>
