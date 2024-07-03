<template>
  <v-dialog :model-value="localDialog" @update:model-value="updateDialog" max-width="500px">
    <v-card>
      <v-card-title>
        <span class="headline">Edit Event</span>
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field
            v-model="localEvent.title"
            label="Event Title"
            required
          ></v-text-field>
          <v-date-picker
            v-model="localEvent.date"
            label="Event Date"
            required
          ></v-date-picker>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
        <v-btn color="blue darken-1" text @click="updateEvent">Save</v-btn>
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
    },
    event: {
      type: Object,
      required: true
    }
  },
  emits: ['update:dialog', 'event-updated'],
  setup(props, { emit }) {
    const localDialog = ref(props.dialog);
    const localEvent = ref({ ...props.event });
    const toast = useToast();

    const updateEvent = async () => {
      const token = localStorage.getItem('token');
      if (!localEvent.value.title || !localEvent.value.date) {
        toast.error('Please fill in all fields');
        return;
      }

      try {
        await axios.put(`http://localhost:5000/api/events/${localEvent.value.id}`, {
          title: localEvent.value.title,
          date: localEvent.value.date.toISOString().split('T')[0]
        }, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        toast.success('Event updated successfully');
        emit('event-updated');
        close();
      } catch (error) {
        toast.error('Failed to update event');
      }
    };

    const close = () => {
      emit('update:dialog', false);
    };

    const updateDialog = (val) => {
      localDialog.value = val;
      emit('update:dialog', val);
    };

    watch(() => props.dialog, (newVal) => {
      localDialog.value = newVal;
    });

    watch(() => props.event, (newVal) => {
      localEvent.value = { ...newVal };
    });

    return {
      localDialog,
      localEvent,
      updateEvent,
      close,
      updateDialog
    };
  }
};
</script>
