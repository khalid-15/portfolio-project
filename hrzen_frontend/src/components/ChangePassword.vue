<template>
    <v-container class="d-flex justify-center align-center login-register-container">
      <v-card class="pa-5" width="400">
        <v-card-title>Change Password</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="changePassword">
            <v-text-field label="New Password" v-model="newPassword" type="password" required></v-text-field>
            <v-btn class="custom-btn mt-4" type="submit">Change Password</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';
  import { useToast } from 'vue-toast-notification';
  
  export default {
    name: 'ChangePassword',
    data() {
      return {
        newPassword: '',
      };
    },
    methods: {
      async changePassword() {
        try {
          const token = localStorage.getItem('token');
          await axios.post('http://localhost:5000/change-password', {
            token: token,
            newPassword: this.newPassword,
          });
          useToast().success('Password changed successfully!');
          this.$router.push({ name: 'HomePage' });
        } catch (error) {
          useToast().error('Password change failed!');
          console.error('Password change failed:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .login-register-container {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .v-card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
  
  .custom-btn {
    width: 100%;
    background-color: #1976D2;
    color: white;
    border-radius: 8px;
    padding: 10px 0;
    transition: background-color 0.3s;
  }
  
  .custom-btn:hover {
    background-color: #1565C0;
  }
  </style>
  