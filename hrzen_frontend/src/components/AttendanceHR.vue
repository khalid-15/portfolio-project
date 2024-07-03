<template>
  <v-container>
    <v-card>
      <v-card-title class="d-flex flex-row mb-6">
        Attendance Records
        <v-spacer></v-spacer>
        <v-btn icon @click="downloadAttendance">
          <v-icon color="primary">mdi-download</v-icon>
        </v-btn>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="attendanceRecords"
        class="elevation-1"
        height="400"
      >
        <template v-slot:[`item.actions`]="{ item }">
          <v-icon small color="red" @click="confirmDeleteAttendance(item.id)">mdi-delete</v-icon>
        </template>
      </v-data-table>
    </v-card>

    <v-dialog v-model="confirmDeleteDialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">Delete Attendance</span>
        </v-card-title>
        <v-card-text>Are you sure you want to delete this attendance record?</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red darken-1" text @click="confirmDeleteDialog = false">Cancel</v-btn>
          <v-btn color="green darken-1" text @click="deleteAttendance">Confirm</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toast-notification';

export default {
  name: 'AttendanceHR',
  data() {
    return {
      attendanceRecords: [],
      headers: [
        { text: 'ID', value: 'id', align: 'start', sortable: true },
        { text: 'Employee ID', value: 'employee_id', align: 'start', sortable: true },
        { text: 'Employee Name', value: 'employee_name', align: 'start', sortable: true },
        { text: 'Date', value: 'date', align: 'start', sortable: true },
        { text: 'Status', value: 'status', align: 'start', sortable: true },
        { text: 'Actions', value: 'actions', align: 'center', sortable: false },
      ],
      confirmDeleteDialog: false,
      attendanceToDelete: null,
    };
  },
  created() {
    this.fetchAttendanceRecords();
  },
  methods: {
    fetchAttendanceRecords() {
      const token = localStorage.getItem('token');
      axios.get('http://localhost:5000/api/attendance', {
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
    confirmDeleteAttendance(id) {
      this.attendanceToDelete = id;
      this.confirmDeleteDialog = true;
    },
    deleteAttendance() {
      const toast = useToast();
      const token = localStorage.getItem('token');
      axios.delete(`http://localhost:5000/api/attendance/${this.attendanceToDelete}`, {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(() => {
        this.fetchAttendanceRecords();
        this.confirmDeleteDialog = false;
        toast.success('Attendance record deleted successfully!');
      })
      .catch(error => {
        toast.error('There was an error deleting the attendance record!');
        console.error("There was an error deleting the attendance record!", error);
      });
    },
    downloadAttendance() {
      const token = localStorage.getItem('token');
      axios.get('http://localhost:5000/api/attendance', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      })
      .then(response => {
        const csvContent = this.convertToCSV(response.data);
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement('a');
        const url = URL.createObjectURL(blob);
        link.setAttribute('href', url);
        link.setAttribute('download', 'attendance_records.csv');
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
  background-color: #3F51B5;
  color: white;
}
.v-btn {
  margin-right: 8px;
}
</style>
