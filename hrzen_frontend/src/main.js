import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify'; // Make sure you have the vuetify plugin setup

createApp(App)
  .use(router)
  .use(vuetify)
  .mount('#app');
