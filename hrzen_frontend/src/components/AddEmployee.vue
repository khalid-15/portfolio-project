<template>
  <v-dialog v-model="localDialog" max-width="500px">
    <v-card>
      <v-card-title class="card">
        <span class="headline">Add Employee</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="localEmployee.name" label="Name" required></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="localEmployee.position" label="Position"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="localEmployee.salary" label="Salary" type="number"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="localEmployee.email" label="Email" required></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="localEmployee.password" label="Password" type="password" required></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-select v-model="localEmployee.role" :items="roles" label="Role" required></v-select>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn class="cancel-btn" text @click="closeDialog">Cancel</v-btn>
        <v-btn class="save-btn" text @click="saveEmployee">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toast-notification';

export default {
  name: 'AddEmployee',
  props: {
    dialog: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      localDialog: this.dialog,
      localEmployee: {
        name: '',
        position: '',
        salary: '',
        email: '',
        password: '',  // Add the password field here
        role: ''
      },
      roles: ['employee', 'manager']
    };
  },
  watch: {
    dialog(val) {
      this.localDialog = val;
    },
    localDialog(val) {
      this.$emit('update:dialog', val);
    }
  },
  methods: {
    closeDialog() {
      this.localDialog = false;
    },
    // saveEmployee() {
    //   const toast = useToast();
    //   axios.post('http://localhost:5000/api/employees', this.localEmployee)
    //     .then(() => {
    //       this.$emit('employee-added');
    //       this.closeDialog();
    //       toast.success('Employee added successfully!');
    //     })
    //     .catch(error => {
    //       toast.error('There was an error adding the employee!');
    //       console.error("There was an error adding the employee!", error);
    //     });
    // }
  saveEmployee() {
  const toast = useToast();
  const token = localStorage.getItem('token');
  axios.post('http://localhost:5000/api/employees', this.localEmployee, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  })
    .then(() => {
      this.$emit('employee-added');
      this.closeDialog();
      toast.success('Employee added successfully!');
    })
    .catch(error => {
      if (error.response && error.response.status === 400) {
        toast.error('User with this email already exists');
      } else {
        toast.error('There was an error adding the employee!');
      }
      console.error("There was an error adding the employee!", error);
    });
    }
  }
};
</script>
<style scoped>
.cancel-btn {
  background-color: #E0E1DD !important;
  color: #415A77 !important;
}
.save-btn {
  background-color: #778DA9 !important;
  color: white !important;
}
.card{
  background-color: #1B263B;
  color: #E0E1DD;
}
</style>