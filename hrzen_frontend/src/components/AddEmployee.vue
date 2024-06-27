<template>
  <v-dialog v-model="internalDialog" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="headline">Add Employee</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="newEmployee.name" label="Name"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="newEmployee.position" label="Position"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="newEmployee.salary" label="Salary" type="number"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="newEmployee.email" label="Email"></v-text-field>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="internalDialog = false">Cancel</v-btn>
        <v-btn color="blue darken-1" text @click="saveEmployee">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AddEmployee',
  props: {
    dialog: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      internalDialog: this.dialog,
      newEmployee: {
        name: '',
        position: '',
        salary: '',
        email: '',
      },
    };
  },
  watch: {
    dialog(val) {
      this.internalDialog = val;
    },
    internalDialog(val) {
      this.$emit('update:dialog', val);
    },
  },
  methods: {
    saveEmployee() {
      axios.post('http://localhost:5000/api/employees', this.newEmployee)
        .then(() => {
          this.$emit('employee-added');
          this.internalDialog = false;
          this.newEmployee = {
            name: '',
            position: '',
            salary: '',
            email: '',
          };
        })
        .catch(error => {
          console.error(error);
        });
    },
  },
};
</script>

<style scoped>
</style>