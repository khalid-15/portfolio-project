import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';
import { loadFonts } from './plugins/webfontloader';
import ToastPlugin from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
import VCalendar from 'v-calendar';
import 'v-calendar/style.css'; 

loadFonts();

const app = createApp(App);

app.use(router);
app.use(vuetify);
app.use(ToastPlugin);
app.use(VCalendar, {}); 

app.mount('#app');
