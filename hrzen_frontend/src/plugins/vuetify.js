import '@mdi/font/css/materialdesignicons.css';
import 'vuetify/styles';
import { createVuetify } from 'vuetify';

const vuetify = createVuetify({
  theme: {
    themes: {
      light: {
        primary: '#3F51B5',
        secondary: '#E8EAF6',
        accent: '#FF4081',
        error: '#FF5252',
        info: '#2196F3',
        success: '#4CAF50',
        warning: '#FB8C00',
      },
    },
  },
});

export default vuetify;
