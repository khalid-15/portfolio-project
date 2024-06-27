<template>
  <v-dialog v-model="localDialog" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="headline">Add Employee</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="localEmployee.name" label="Name"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="localEmployee.position" label="Position"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="localEmployee.salary" label="Salary" type="number"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="localEmployee.email" label="Email"></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="closeDialog">Cancel</v-btn>
        <v-btn color="blue darken-1" text @click="saveEmployee">Save</v-btn>
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
        email: ''
      }
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
    saveEmployee() {
      const toast = useToast();
      axios.post('http://localhost:5000/api/employees', this.localEmployee)
        .then(() => {
          this.$emit('employee-added');
          this.closeDialog();
          toast.success('Employee added successfully!');
        })
        .catch(error => {
          toast.error('There was an error adding the employee!');
          console.error("There was an error adding the employee!", error);
        });
    }
  }
};
</script>
