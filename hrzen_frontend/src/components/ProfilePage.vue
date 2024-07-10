<template>
    <v-container>
      <v-card>
        <v-card-title>
          <span class="headline">Profile</span>
        </v-card-title>
        <v-card-text>
          <v-form @submit.prevent="changePassword">
            <v-text-field v-model="currentPassword" label="Current Password" type="password" required></v-text-field>
            <v-text-field v-model="newPassword" label="New Password" type="password" required></v-text-field>
            <v-card-actions>
              <v-btn type="submit" color="primary">Change Password</v-btn>
            </v-card-actions>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';
  import { useToast } from 'vue-toast-notification';
  
  export default {
    name: 'ProfilePage',
    data() {
      return {
        currentPassword: '',
        newPassword: ''
      };
    },
    methods: {
      changePassword() {
        const toast = useToast();
        const token = localStorage.getItem('token');
        axios.post('https://hr-system-wcp8.onrender.com/change-password', {
          token: token,
          current_password: this.currentPassword,
          new_password: this.newPassword
        })
        .then(() => {
          toast.success('Password changed successfully!');
          this.currentPassword = '';
          this.newPassword = '';
        })
        .catch(error => {
          toast.error('Failed to change password!');
          console.error('Error changing password:', error);
        });
      }
    }
  };
  </script>
  