<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="8">
        <v-card>
          <v-card-title class="d-flex flex-row mb-6">
            HR Calendar
            <v-spacer></v-spacer>
            <v-btn @click="showAddEventDialog" class="add-event-btn mr-2">Add Event</v-btn>
            <v-btn @click="fetchEvents" class="refresh-event-btn">Refresh Events</v-btn>
          </v-card-title>
          <v-card-text>
            <v-calendar
              v-model="selectedDate"
              @click:date="showEvents"
              :events="events"
            ></v-calendar>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="4">
        <v-card>
          <v-card-title>
            Events on {{ selectedDate.toDateString() }}
          </v-card-title>
          <v-card-text>
            <div v-for="event in filteredEvents" :key="event.id" class="mb-2">
              <div>{{ event.title }}</div>
              <div>{{ event.date }}</div>
              <v-icon small class="mr-2" @click="showEditEventDialog(event)">mdi-pencil</v-icon>
              <v-icon small color="red" @click="confirmDelete(event.id)">mdi-delete</v-icon>
              <v-divider class="my-2"></v-divider>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <AddEventDialog v-model:dialog="addDialog" @event-added="fetchEvents" />
    <EditEventDialog v-model:dialog="editDialog" :event="selectedEvent" @event-updated="fetchEvents" />
    <v-dialog v-model="deleteDialog" max-width="500px">
      <v-card>
        <v-card-title>
          Confirm Delete
        </v-card-title>
        <v-card-text>
          Are you sure you want to delete this event?
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="closeDeleteDialog">Cancel</v-btn>
          <v-btn color="red darken-1" text @click="deleteEvent">Delete</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { ref, computed } from 'vue';
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
    const deleteDialog = ref(false);
    const selectedEvent = ref(null);
    const selectedDate = ref(new Date());
    const events = ref([]);
    const eventIdToDelete = ref(null);
    const toast = useToast();

    // const fetchEvents = async () => {
    //   try {
    //     const response = await axios.get('http://localhost:5000/api/events');
    //     events.value = response.data;
    //   } catch (error) {
    //     toast.error('Failed to fetch events');
    //   }
    // };

    const fetchEvents = async () => {
      const token = localStorage.getItem('token');
      try {
        const response = await axios.get('http://localhost:5000/api/events', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        events.value = response.data;
      } catch (error) {
        toast.error('Failed to fetch events');
      }
    };

    const showAddEventDialog = () => {
      addDialog.value = true;
    };

    const showEditEventDialog = (event) => {
      selectedEvent.value = { ...event };
      editDialog.value = true;
    };

    const confirmDelete = (id) => {
      eventIdToDelete.value = id;
      deleteDialog.value = true;
    };

    const deleteEvent = async () => {
      const token = localStorage.getItem('token');
      try {
        await axios.delete(`http://localhost:5000/api/events/${eventIdToDelete.value}`, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        toast.success('Event deleted successfully');
        fetchEvents();
        closeDeleteDialog();
      } catch (error) {
        toast.error('Failed to delete event');
      }
    };

    // const deleteEvent = async () => {
    //   try {
    //     await axios.delete(`http://localhost:5000/api/events/${eventIdToDelete.value}`);
    //     toast.success('Event deleted successfully');
    //     fetchEvents();
    //     closeDeleteDialog();
    //   } catch (error) {
    //     toast.error('Failed to delete event');
    //   }
    // };

    const closeDeleteDialog = () => {
      deleteDialog.value = false;
    };

    const showEvents = (date) => {
      selectedDate.value = date;
    };

    const filteredEvents = computed(() => {
      return events.value.filter(event => event.date === selectedDate.value.toISOString().split('T')[0]);
    });

    fetchEvents();

    return {
      addDialog,
      editDialog,
      deleteDialog,
      selectedEvent,
      selectedDate,
      events,
      fetchEvents,
      showAddEventDialog,
      showEditEventDialog,
      confirmDelete,
      deleteEvent,
      closeDeleteDialog,
      showEvents,
      filteredEvents
    };
  }
};
</script>

<style scoped>
.v-card-title {
  background-color: #415A77;
  color: white;
}
.add-event-btn {
  background-color: #778DA9 !important;
  color: white !important;
}
.refresh-event-btn {
  background-color: #E0E1DD !important;
  color: #415A77 !important;
}
.cancel-btn {
  background-color: #E0E1DD !important;
  color: #415A77 !important;
}
.delete-btn {
  background-color: red !important;
  color: white !important;
}
.mr-2 {
  margin-right: 8px;
  color: #1B263B;
}
.my-2 {
  margin-top: 8px;
  margin-bottom: 8px;
}
</style>
