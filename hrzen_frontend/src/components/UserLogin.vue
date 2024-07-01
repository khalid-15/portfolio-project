<template>
  <v-container class="d-flex justify-center align-center login-register-container">
    <v-card class="pa-5" width="400">
      <v-card-title>Login</v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field label="Email" v-model="email" required></v-text-field>
          <v-text-field label="Password" v-model="password" type="password" required></v-text-field>
          <v-btn class="custom-btn" @click="login">Login</v-btn>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios';
import { useToast } from 'vue-toast-notification';

export default {
  name: 'UserLogin',
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:5000/login', {
          email: this.email,
          password: this.password
        });
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('role', response.data.role);
        useToast().success('Logged in successfully!');
        if (response.data.first_login) {
          this.$router.push({ name: 'ChangePassword' });
        } else {
          this.$router.push({ name: 'HomePage' });
        }
      } catch (error) {
        useToast().error('Login failed!');
        console.error('Login failed:', error);
      }
    }
  }
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
