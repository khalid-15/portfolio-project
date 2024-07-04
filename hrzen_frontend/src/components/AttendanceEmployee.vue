<template>
  <v-container>
    <v-card>
      <v-card-title class="d-flex flex-row mb-6">
        My Attendance Records
        <v-spacer></v-spacer>
        <v-btn class="checkin-btn" @click="checkIn">Check In</v-btn>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="attendanceRecords"
        height="400"
        class="elevation-1"
      />
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
      employeeId: null,
    };
  },
  created() {
    const token = localStorage.getItem('token');
    const decodedToken = JSON.parse(atob(token.split('.')[1]));
    this.employeeId = decodedToken.id;
    this.fetchAttendanceRecords();
  },
  methods: {
    fetchAttendanceRecords() {
      const token = localStorage.getItem('token');
      axios.get(`http://localhost:5000/api/attendance?employee_id=${this.employeeId}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
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
      const token = localStorage.getItem('token');

      axios.post('http://localhost:5000/api/attendance', { employee_id: this.employeeId, date, status }, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
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
.v-card-title {
  background-color: #415A77;
  color: white;
}
.checkin-btn {
  background-color: #778DA9 !important;
  color: white !important;
}
.custom-table-header .v-data-table-header {
  background-color: #415A77 !important;
  color: white !important;
}
</style>
