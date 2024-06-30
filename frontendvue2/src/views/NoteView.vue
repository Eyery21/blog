<template>
  <div class="home">
    <input
      class="input"
      type="text"
      v-model="searchQuery"
      placeholder="saississez votre recherche"
    />
    <button class="button-search" @click="searchNote">Search</button>

    <div class="notes">
      <draggable v-model="notes" @end="onEnd" class="draggable-area">
        <div
          v-for="note in notes"
          :key="note.id"
          class="note-card"
          :style="{ gridColumn: note.column, gridRow: note.row}"
        >
          <NoteCard :note="note" />
        </div>
      </draggable>
    </div>

    <div class="pagination">
      <button 
      class="button" 
      @click="prevPage" 
      :disabled="currentPage === 1"
      v-if="currentPage > 1"

      >
        page précédente
      </button>
      <span> Page {{ currentPage }} of {{ numPages }}</span>
      <button
        class="button"
        @click="nextPage"
        :disabled="currentPage === numPages"
        v-if="currentPage < numPages"

      >
        page suivante
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import draggable from "vuedraggable";
import NoteCard from "../components/NoteCard.vue";

export default {
  name: "NoteView",
  components: { NoteCard, draggable },
  data() {
    return {
      notes: [],
      currentPage: 1,
      numPages: 1,
      searchQuery: "",
    };
  },
  mounted() {
    this.getNotes();
  },
  methods: {
    getNotes() {
      const url = this.searchQuery
        ? `/api/v1/notes/?search=${this.searchQuery}&page=${this.currentPage}`
        : `/api/v1/notes/?page=${this.currentPage}`;

      axios
        .get(url)
        .then((response) => {
          this.notes = response.data.notes;
          this.numPages = response.data.num_pages;
          this.currentPage = response.data.current_page;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    searchNote() {
      this.currentPage = 1; // Reset to first page on new search
      this.getNotes();
    },
    nextPage() {
      if (this.currentPage < this.numPages) {
        this.currentPage += 1;
        this.getNotes();
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;
        this.getNotes();
      }
    },
    onEnd(event) {
      // Ici, vous pouvez envoyer l'ordre mis à jour au backend si nécessaire
      console.log("Order updated", this.notes);
    },
  },
};
</script>

<style scoped>
.input {
  border: 1px solid black;
  margin: 5px;
}
.button-search {
  border: 1px solid black;
  margin: 5px;
}
.home {
  background-color: aqua;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.notes {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(5, 1fr);
  gap: 5%;
  width: 60vw;
  height: 65vh;
  border: 1px solid black;
}
.draggable-area {
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: inherit;
  grid-template-rows: inherit;
  gap: inherit;
}
.note-card {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: beige;
  border: 1px solid red;
  padding: 10px;
  cursor: move;
  height: 200px;
}
.pagination {
  display: flex;
  justify-content: center;
  margin: 20px;
}
.button {
  border: 2px solid red;
  margin: 0px 10px;
}
</style>
