<template>
  <v-container>
    <v-card>
      <v-card-title>
        HR Calendar
        <v-spacer></v-spacer>
        <v-btn @click="showAddEventDialog" color="primary">Add Event</v-btn>
        <v-btn @click="fetchEvents" color="secondary">Refresh Events</v-btn>
      </v-card-title>
      <v-card-text>
        <v-calendar
          v-model="selectedDate"
          @click:date="showEvents"
          :events="events"
        ></v-calendar>
      </v-card-text>
    </v-card>
    <AddEventDialog v-model:dialog="addDialog" @event-added="fetchEvents" />
    <EditEventDialog v-model:dialog="editDialog" :event="selectedEvent" @event-updated="fetchEvents" />
  </v-container>
</template>

<script>
import { ref } from 'vue';
import AddEventDialog from './AddEventDialog.vue';
import EditEventDialog from './EditEventDialog.vue';
import axios from 'axios';
import { useToast } from 'vue-toast-notification';

export default {
  components: {
    AddEventDialog,
    EditEventDialog
  },
  setup() {
    const addDialog = ref(false);
    const editDialog = ref(false);
    const selectedEvent = ref(null);
    const selectedDate = ref(new Date());
    const events = ref([]);
    const toast = useToast();

    const fetchEvents = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/events');
        events.value = response.data.map(event => ({
          ...event,
          start: new Date(event.date),
          end: new Date(event.date),
        }));
      } catch (error) {
        toast.error('Failed to fetch events');
      }
    };

    const showAddEventDialog = () => {
      addDialog.value = true;
    };

    const showEvents = (date) => {
      selectedDate.value = date;
      const dayEvents = events.value.filter(event => {
        const eventDate = new Date(event.start).toDateString();
        return eventDate === date.toDateString();
      });

      if (dayEvents.length > 0) {
        selectedEvent.value = dayEvents[0];
        editDialog.value = true;
      } else {
        toast.info('No events for the selected date');
      }
    };

    return {
      addDialog,
      editDialog,
      selectedEvent,
      selectedDate,
      events,
      fetchEvents,
      showAddEventDialog,
      showEvents
    };
  }
};
</script>

<style scoped>
.v-card-title {
  background-color: #3F51B5;
  color: white;
}
</style>
