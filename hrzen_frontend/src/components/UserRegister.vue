<template>
  <v-container class="d-flex justify-center align-center login-register-container">
    <v-card class="pa-5" width="400">
      <v-card-title>Register</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="register">
          <v-text-field label="Name" v-model="name" required></v-text-field>
          <v-text-field label="Email" v-model="email" required></v-text-field>
          <v-select v-model="role" :items="roles" label="Role" required></v-select>
          <v-text-field label="Password" v-model="password" type="password" required></v-text-field>
          <v-btn class="custom-btn mt-4" type="submit">Register</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toast-notification';

export default {
  name: 'RegisterForm',
  data() {
    return {
      name: '',
      email: '',
      role: '',
      password: '',
      roles: ['manager', 'employee'],
    };
  },
  methods: {
    register() {
      const toast = useToast();
      axios.post('http://localhost:5000/register', {
        name: this.name,
        email: this.email,
        role: this.role,
        password: this.password,
      })
      .then(() => {
        toast.success('Registration successful!');
        this.$router.push('/login');
      })
      .catch(error => {
        toast.error('Registration failed!');
        console.error('Registration error:', error);
      });
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
