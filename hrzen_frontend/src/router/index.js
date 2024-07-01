import { createRouter, createWebHistory } from 'vue-router';
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import HomePage from '@/components/HomePage.vue';
import EmployeeList from '@/components/EmployeeList.vue';
import HRCalendar from '@/components/HRCalendar.vue';
import HRPayroll from '@/components/HRPayroll.vue';
import AttendanceEmployee from '@/components/AttendanceEmployee.vue';
import AttendanceHR from '@/components/AttendanceHR.vue';
import Login from '@/components/UserLogin.vue';
import Register from '@/components/UserRegister.vue';

const routes = [
  {
    path: '/',
    component: DefaultLayout,
    children: [
      { path: '', name: 'HomePage', component: HomePage },
      { path: 'employees', name: 'EmployeeList', component: EmployeeList, meta: { requiresAuth: true, role: 'manager' } },
      { path: 'attendance', name: 'AttendanceEmployee', component: AttendanceEmployee, meta: { requiresAuth: true, role: 'employee' } },
      { path: 'attendance/hr', name: 'AttendanceHR', component: AttendanceHR, meta: { requiresAuth: true, role: 'manager' } },
      { path: 'calendar', name: 'HRCalendar', component: HRCalendar, meta: { requiresAuth: true } },
      { path: 'payroll', name: 'HRPayroll', component: HRPayroll, meta: { requiresAuth: true, role: 'manager' } },
    ],
  },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token');
  const userRole = localStorage.getItem('role');
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!token) {
      next({ name: 'Login' });
    } else if (to.meta.role && to.meta.role !== userRole) {
      next({ name: 'HomePage' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
