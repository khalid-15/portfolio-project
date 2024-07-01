<template>
  <v-container>
    <v-form @submit.prevent="register">
      <v-text-field v-model="name" label="Name" required></v-text-field>
      <v-text-field v-model="email" label="Email" required></v-text-field>
      <v-text-field v-model="password" label="Password" type="password" required></v-text-field>
      <v-text-field v-model="role" label="Role" required></v-text-field>
      <v-btn type="submit" color="primary">Register</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserRegister',
  data() {
    return {
      name: '',
      email: '',
      password: '',
      role: ''
    };
  },
  methods: {
    register() {
      axios.post('http://localhost:5000/register', {
        name: this.name,
        email: this.email,
        password: this.password,
        role: this.role
      })
      .then(response => {
        alert(response.data.message);
        this.$router.push('/login');
      })
      .catch(error => {
        console.error(error);
        alert('Registration failed');
      });
    }
  }
};
</script>
