<template>
  <v-container>
    <v-card>
      <v-card-title class="d-flex flex-row mb-6">
        Employees
        <v-spacer></v-spacer>
        <v-btn @click="showAddEmployeeDialog"  class="add-employee-btn mr-2">Add Employee</v-btn>
        <v-btn @click="downloadEmployees" class="download-employee-btn">Download Employees</v-btn>
      </v-card-title>
      <v-card-text>
        <v-data-table
          :headers="headers"
          :items="employees"
          height="100%"
          class="elevation-1"
        >
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon small color="#1B263B" class="mr-2" @click="showEditEmployeeDialog(item)">mdi-pencil</v-icon>
            <v-icon small color="red" @click="confirmDeleteEmployee(item.id)">mdi-delete</v-icon>
          </template>
        </v-data-table>
      </v-card-text>
    </v-card>
    <AddEmployee v-model:dialog="addDialog" @employee-added="fetchEmployees" />
    <UpdateEmployee v-model:dialog="editDialog" :employee="selectedEmployee" @employee-updated="fetchEmployees" />

    <v-dialog v-model="confirmDeleteDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">Delete Employee</span>
        </v-card-title>
        <v-card-text>Are you sure you want to delete this employee?</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="confirmDeleteDialog = false">Cancel</v-btn>
          <v-btn color="green darken-1" text @click="deleteEmployee">Confirm</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from 'axios';
import AddEmployee from '@/components/AddEmployee.vue';
import UpdateEmployee from '@/components/UpdateEmployee.vue';
import { useToast } from 'vue-toast-notification';

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
      { title: 'Name', value: 'name', align: 'start', sortable: true },
        { title: 'Position', value: 'position', align: 'start', sortable: true },
        { title: 'Salary', value: 'salary', align: 'start', sortable: true },
        { title: 'Email', value: 'email', align: 'start', sortable: true },
        { title: 'Actions', value: 'actions', align: 'center', sortable: false },
      ],
      addDialog: false,
      editDialog: false,
      confirmDeleteDialog: false,
      selectedEmployee: null,
      employeeToDelete: null
    };
  },
  created() {
    this.fetchEmployees();
  },
  methods: {
    // fetchEmployees() {
    //   axios.get('http://localhost:5000/api/employees')
    //     .then(response => {
    //       this.employees = response.data;
    //     })
    //     .catch(error => {
    //       console.error("There was an error fetching the employees!", error);
    //     });
    // },
    fetchEmployees() {
  const token = localStorage.getItem('token');
  axios.get('http://localhost:5000/api/employees', {
    headers: {
      'Authorization': `Bearer ${token}`
      }
    })
    .then(response => {
      this.employees = response.data;
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

    confirmDeleteEmployee(id) {
      this.employeeToDelete = id;
      this.confirmDeleteDialog = true;
    },

    deleteEmployee() {
  const toast = useToast();
  const token = localStorage.getItem('token');
  axios.delete(`http://localhost:5000/api/employees/${this.employeeToDelete}`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
    })
    .then(() => {
      this.fetchEmployees();
      this.confirmDeleteDialog = false;
      toast.success('Employee deleted successfully!');
    })
    .catch(error => {
      toast.error('There was an error deleting the employee!');
      console.error("There was an error deleting the employee!", error);
    });
    },
    // deleteEmployee() {
    //   const toast = useToast();
    //   axios.delete(`http://localhost:5000/api/employees/${this.employeeToDelete}`)
    //     .then(() => {
    //       this.fetchEmployees();
    //       this.confirmDeleteDialog = false;
    //       toast.success('Employee deleted successfully!');
    //     })
    //     .catch(error => {
    //       toast.error('There was an error deleting the employee!');
    //       console.error("There was an error deleting the employee!", error);
    //     });
    // },

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
.v-card-title {
  background-color: #415A77;
  color: white;
}
.mr-2 {
  margin-right: 8px;
}
.add-employee-btn {
  background-color: #778DA9 !important;
  color: white !important;
}
.download-employee-btn {
  background-color: #E0E1DD !important;
  color: #415A77 !important;
}

</style>
