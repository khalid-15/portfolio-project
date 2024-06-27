<template>
  <v-dialog :value="dialog" @input="updateDialog" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="headline">Edit Employee</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="updatedEmployee.name" label="Name"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="updatedEmployee.position" label="Position"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="updatedEmployee.salary" label="Salary" type="number"></v-text-field>
            </v-col>
            <v-col cols="12" sm="6" md="4">
              <v-text-field v-model="updatedEmployee.email" label="Email"></v-text-field>
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

export default {
  name: 'UpdateEmployee',
  props: {
    dialog: {
      type: Boolean,
      default: false
    },
    employee: {
      type: Object,
      default: () => ({})
    }
  },
  data() {
    return {
      updatedEmployee: {}
    };
  },
  watch: {
    employee: {
      handler(newEmployee) {
        this.updatedEmployee = { ...newEmployee };
      },
      deep: true,
      immediate: true
    }
  },
  methods: {
    updateDialog(value) {
      this.$emit('update:dialog', value);
    },
    closeDialog() {
      this.updateDialog(false);
    },
    saveEmployee() {
      axios.put(`http://localhost:5000/api/employees/${this.updatedEmployee.id}`, this.updatedEmployee)
        .then(response => {
          this.$emit('employee-updated', response.data);
          this.closeDialog();
        })
        .catch(error => {
          console.error("There was an error updating the employee!", error);
        });
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
