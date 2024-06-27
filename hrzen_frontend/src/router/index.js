import { createRouter, createWebHistory } from 'vue-router';
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import HomePage from '@/components/HomePage.vue';
import EmployeeList from '@/components/EmployeeList.vue';
import HRCalendar from '@/components/HRCalendar.vue';
import HRPayroll from '@/components/HRPayroll.vue';

const routes = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      {
        path: '',
        name: 'HomePage',
        component: HomePage
      },
      {
        path: 'employees',
        name: 'EmployeeList',
        component: EmployeeList
      },
      {
        path: 'calendar',
        name: 'HRCalendar',
        component: HRCalendar
      },
      {
        path: 'payroll',
        name: 'HRPayroll',
        component: HRPayroll
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;