<template>
    <div>
      <h1>Employees</h1>
      <ul>
        <li v-for="employee in employees" :key="employee.id" class="employee-item">
          {{ employee.name }} - {{ employee.position }}
          <button @click="deleteEmployee(employee.id)" class="delete-button">Delete</button>
        </li>
      </ul>
      <div class="form-group">
        <input v-model="newEmployee.name" placeholder="Name" class="form-control" />
        <input v-model="newEmployee.position" placeholder="Position" class="form-control" />
        <input v-model="newEmployee.salary" placeholder="Salary" class="form-control" />
        <input v-model="newEmployee.email" placeholder="Email" class="form-control" />
        <button @click="addEmployee" class="add-button">Add Employee</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        employees: [],
        newEmployee: { name: '', position: '', salary: '', email: '' }
      };
    },
    created() {
      this.fetchEmployees();
    },
    methods: {
      fetchEmployees() {
        axios.get('http://localhost:5000/api/employees')
          .then(response => {
            this.employees = response.data;
          });
      },
      addEmployee() {
        axios.post('http://localhost:5000/api/employees', this.newEmployee)
          .then(() => {
            this.fetchEmployees();
            this.newEmployee = { name: '', position: '', salary: '', email: '' };
          });
      },
      deleteEmployee(id) {
        axios.delete(`http://localhost:5000/api/employees/${id}`)
          .then(() => {
            this.fetchEmployees();
          });
      }
    }
  };
  </script>
  
  <style>
  body {
    font-family: Arial, sans-serif;
  }
  
  h1 {
    font-size: 2em;
    margin-bottom: 20px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  .employee-item {
    margin-bottom: 10px;
  }
  
  .delete-button {
    margin-left: 10px;
    color: red;
  }
  
  .form-group {
    margin-top: 20px;
  }
  
  .form-control {
    display: block;
    margin-bottom: 10px;
    padding: 10px;
    width: 200px;
  }
  
  .add-button {
    display: block;
    padding: 10px 20px;
    background-color: green;
    color: white;
    border: none;
    cursor: pointer;
  }
  </style>
  