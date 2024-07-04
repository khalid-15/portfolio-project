<template>
  <v-container class="d-flex justify-center align-center login-register-container">
    <v-card class="pa-5" width="400">
      <v-card-title class="headline">Register</v-card-title>
      <v-card-text>
        <v-form @submit.prevent="register">
          <v-text-field label="Name" v-model="name" required></v-text-field>
          <v-text-field label="Email" v-model="email" required></v-text-field>
          <v-select label="Role" v-model="role" :items="roles" required></v-select>
          <v-text-field label="Password" v-model="password" type="password" required></v-text-field>
          <v-btn class="register-btn mt-4" type="submit">Register</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toast-notification';

export default {
  name: 'UserRegister',
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
  background-color: #1B263B;
}

.v-card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.register-btn {
  width: 100%;
  background-color: #778DA9 !important;
  color: white !important;
  border-radius: 8px;
  padding: 10px 0;
  transition: background-color 0.3s;
}

.register-btn:hover {
  background-color: #415A77 !important;
}

.v-card-title {
  color: #1B263B;
}
</style>
