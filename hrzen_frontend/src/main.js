import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';
import { loadFonts } from './plugins/webfontloader';
import ToastPlugin from 'vue-toast-notification';
// Import one of the available themes
import 'vue-toast-notification/dist/theme-sugar.css';

loadFonts();

const app = createApp(App);

app.use(router);
app.use(vuetify);
app.use(ToastPlugin);

app.mount('#app');
