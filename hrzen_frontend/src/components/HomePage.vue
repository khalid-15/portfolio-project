<template>
  <v-container>
    <v-row>
      <v-col>
        <h1>Welcome to HRZen</h1>
        <p>This is the landing page of HRZen. Here are some screenshots of our app and documentation on how to navigate it.</p>
        <v-img src="" aspect-ratio="1.7"></v-img>
        <v-img src="" aspect-ratio="1.7"></v-img>
        <h2>Documentation</h2>
        <p>To navigate through the HRZen app, use the sidebar to access different sections like Employees, Calendar, and Payroll.</p>
        <p>For more detailed information, visit our <a href="https://docs.hrzen.com" target="_blank">documentation</a> page.</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'HomePage'
};
</script>

<style scoped>
h1 {
  margin-bottom: 16px;
}
v-img {
  margin-bottom: 16px;
}
</style>