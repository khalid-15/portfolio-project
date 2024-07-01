<template>
    <v-container>
      <v-card>
        <v-card-title class="d-flex flex-row mb-6">
          My Attendance Records
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="checkIn">Check In</v-btn>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="attendanceRecords"
          height="400"
          class="elevation-1"
        >
        </v-data-table>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';
  import { useToast } from 'vue-toast-notification';
  
  export default {
    name: 'AttendanceEmployee',
    data() {
      return {
        attendanceRecords: [],
        headers: [
          { text: 'Date', value: 'date', align: 'start', sortable: true },
          { text: 'Status', value: 'status', align: 'start', sortable: true },
        ],
        employeeId: 1,
      };
    },
    created() {
      this.fetchAttendanceRecords();
    },
    methods: {
      fetchAttendanceRecords() {
        axios.get(`http://localhost:5000/api/attendance?employee_id=${this.employeeId}`)
          .then(response => {
            this.attendanceRecords = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the attendance records!", error);
          });
      },
      checkIn() {
        const toast = useToast();
        const date = new Date().toISOString().split('T')[0];
        const status = 'Present';
  
        axios.post('http://localhost:5000/api/attendance', { employee_id: this.employeeId, date, status })
          .then(() => {
            this.fetchAttendanceRecords();
            toast.success('Checked in successfully!');
          })
          .catch(error => {
            toast.error('There was an error checking in!');
            console.error("There was an error checking in!", error);
          });
      }
    }
  };
  </script>
  
  <style scoped>
  .v-btn {
    margin-right: 8px;
  }
  
  .v-card-title {
    background-color: #E8EAF6;
    color: black;
  }
  </style>
  