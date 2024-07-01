<template>
  <v-container>
    <v-form @submit.prevent="login">
      <v-text-field v-model="email" label="Email" required></v-text-field>
      <v-text-field v-model="password" label="Password" type="password" required></v-text-field>
      <v-btn type="submit" color="primary">Login</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserLogin',
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    login() {
      axios.post('http://localhost:5000/login', {
        email: this.email,
        password: this.password
      })
      .then(response => {
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('role', response.data.role);
        this.$router.push('/dashboard');
      })
      .catch(error => {
        console.error(error);
        alert('Login failed');
      });
    }
  }
};
</script>
