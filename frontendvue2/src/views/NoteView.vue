<template>
  <div class="home">
    <NoteCard v-for="note in notes" :key="note.id" :note="note" />
  </div>
</template>
  
  <script>
import axios from "axios";
import NoteCard from "../components/NoteCard.vue";

export default {
  name: "NoteView",
  components: {
    NoteCard,
  },
  data() {
    return {
      notes: [],
    };
  },
  mounted() {
    this.getPosts();
  },
  methods: {
    getPosts() {
      axios
        .get("/api/v1/notes/")
        .then((response) => {
          this.notes = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
  