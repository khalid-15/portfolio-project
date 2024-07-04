import '@mdi/font/css/materialdesignicons.css';
import 'vuetify/styles';
import { createVuetify } from 'vuetify';

const vuetify = createVuetify({
  theme: {
    themes: {
      light: {
        primary: '#0D1B2A',
        secondary: '#1B263B',
        accent: '#415A77',
        info: '#778DA9',
        background: '#E0E1DD',
        error: '#FF5252',
        success: '#4CAF50',
        warning: '#FB8C00',
      },
    },
  },
});

export default vuetify;
