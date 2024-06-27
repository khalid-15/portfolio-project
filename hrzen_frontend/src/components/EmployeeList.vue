<template>
  <v-container>
    <v-card>
      <v-card-title class="d-flex flex-row mb-6">
        Employees
        <v-spacer></v-spacer>
        <v-btn icon class="mr-2" @click="showAddEmployeeDialog">
          <v-icon color="primary">mdi-plus</v-icon>
        </v-btn>
        <v-btn icon @click="downloadEmployees">
          <v-icon color="primary">mdi-download</v-icon>
        </v-btn>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="employees"
        height="400"
        class="elevation-1"
      >
        <template v-slot:[`item.actions`]="{ item }">
          <v-icon small class="mr-2" @click="showEditEmployeeDialog(item)">mdi-pencil</v-icon>
          <v-icon small @click="deleteEmployee(item.id)">mdi-delete</v-icon>
        </template>
      </v-data-table>
    </v-card>
    <AddEmployee v-model:dialog="addDialog" @employee-added="fetchEmployees" />
    <UpdateEmployee v-model:dialog="editDialog" :employee="selectedEmployee" @employee-updated="fetchEmployees" />
  </v-container>
</template>

<script>
import axios from 'axios';
import AddEmployee from '@/components/AddEmployee.vue';
import UpdateEmployee from '@/components/UpdateEmployee.vue';

export default {
  name: 'EmployeeList',
  components: {
    AddEmployee,
    UpdateEmployee
  },
  data() {
    return {
      employees: [],
      headers: [
        { text: 'ID', value: 'id', align: 'start', sortable: true },
        { text: 'Name', value: 'name', align: 'start', sortable: true },
        { text: 'Position', value: 'position', align: 'start', sortable: true },
        { text: 'Salary', value: 'salary', align: 'start', sortable: true },
        { text: 'Email', value: 'email', align: 'start', sortable: true },
        { text: 'Actions', value: 'actions', align: 'center', sortable: false },
      ],
      addDialog: false,
      editDialog: false,
      selectedEmployee: {}
    };
  },
  created() {
    this.fetchEmployees();
  },
  methods: {
    fetchEmployees() {
      axios.get('http://localhost:5000/api/employees')
        .then(response => {
          this.employees = response.data;
          console.log("Employees fetched:", response.data);
          console.log("Employees bound to table:", this.employees);
        })
        .catch(error => {
          console.error("There was an error fetching the employees!", error);
        });
    },
    showAddEmployeeDialog() {
      this.addDialog = true;
    },
    showEditEmployeeDialog(employee) {
      this.selectedEmployee = { ...employee };
      this.editDialog = true;
    },
    deleteEmployee(id) {
      axios.delete(`http://localhost:5000/api/employees/${id}`)
        .then(() => {
          this.fetchEmployees();
        })
        .catch(error => {
          console.error("There was an error deleting the employee!", error);
        });
    },
    downloadEmployees() {
      axios.get('http://localhost:5000/api/employees')
        .then(response => {
          const csvContent = this.convertToCSV(response.data);
          const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
          const link = document.createElement('a');
          const url = URL.createObjectURL(blob);
          link.setAttribute('href', url);
          link.setAttribute('download', 'employees.csv');
          link.style.visibility = 'hidden';
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
        })
        .catch(error => {
          console.error(error);
        });
    },
    convertToCSV(data) {
      const header = Object.keys(data[0]).join(',');
      const rows = data.map(row => Object.values(row).join(',')).join('\n');
      return `${header}\n${rows}`;
    }
  }
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