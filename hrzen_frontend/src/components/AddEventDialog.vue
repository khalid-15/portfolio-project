<template>
  <v-dialog :model-value="localDialog" @update:model-value="updateDialog" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="headline">Add Event</span>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="event.title"
            label="Event Title"
            required
          ></v-text-field>
          <v-date-picker
            v-model="event.date"
            label="Event Date"
            required
          ></v-date-picker>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn class="cancel-btn" text @click="close">Cancel</v-btn>
        <v-btn class="add-btn" text @click="saveEvent">Add</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { ref, watch } from 'vue';
import { useToast } from 'vue-toast-notification';
import axios from 'axios';

export default {
  props: {
    dialog: {
      type: Boolean,
      default: false
    }
  },
  emits: ['update:dialog', 'event-added'],
  setup(props, { emit }) {
    const localDialog = ref(props.dialog);
    const event = ref({
      title: '',
      date: null
    });
    const toast = useToast();

    // const saveEvent = async () => {
    //   if (!event.value.title || !event.value.date) {
    //     toast.error('Please fill in all fields');
    //     return;
    //   }

    //   try {
    //     await axios.post('https://hr-system-wcp8.onrender.com/api/events', {
    //       title: event.value.title,
    //       date: event.value.date.toISOString()
    //     });
    //     toast.success('Event added successfully');
    //     emit('event-added');
    //     close();
    //   } catch (error) {
    //     toast.error('Failed to add event');
    //   }
    // };

    const saveEvent = async () => {
      const token = localStorage.getItem('token');
      if (!event.value.title || !event.value.date) {
        toast.error('Please fill in all fields');
        return;
      }

      try {
        await axios.post('https://hr-system-wcp8.onrender.com/api/events', {
          title: event.value.title,
          date: event.value.date.toISOString()
        }, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        toast.success('Event added successfully');
        emit('event-added');
        close();
      } catch (error) {
        toast.error('Failed to add event');
      }
    };
    
    const close = () => {
      emit('update:dialog', false);
      event.value = { title: '', date: null };
    };

    const updateDialog = (val) => {
      localDialog.value = val;
      emit('update:dialog', val);
    };

    watch(() => props.dialog, (newVal) => {
      localDialog.value = newVal;
      if (!newVal) {
        event.value = { title: '', date: null };
      }
    });

    return {
      localDialog,
      event,
      saveEvent,
      close,
      updateDialog
    };
  }
};
</script>
<style scoped>
.v-card-title {
  background-color: #1B263B;
  color: #E0E1DD;
}
.cancel-btn {
  background-color: #E0E1DD !important;
  color: #415A77 !important;
}
.add-btn {
  background-color: #778DA9 !important;
  color: white !important;
}
</style>