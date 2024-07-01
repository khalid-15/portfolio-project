<template>
  <v-container class="d-flex justify-center align-center" style="height: 100vh;">
    <v-card>
      <v-card-title>
        <span class="headline">Register</span>
      </v-card-title>
      <v-card-text>
        <v-form @submit.prevent="register">
          <v-text-field v-model="name" label="Name" required></v-text-field>
          <v-text-field v-model="email" label="Email" required></v-text-field>
          <v-select v-model="role" :items="roles" label="Role" required></v-select>
          <v-text-field v-model="password" label="Password" type="password" required></v-text-field>
          <v-card-actions>
            <v-btn type="submit" color="primary">Register</v-btn>
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
.v-container {
  max-width: 400px;
}

.v-card {
  width: 100%;
  padding: 20px;
}

.v-card-title {
  background-color: #E8EAF6;
  color: black;
  text-align: center;
}
</style>
