<template>
  <div class="home">
    <div class="search">
      <input
        class="input"
        type="text"
        v-model="searchQuery"
        placeholder="saississez votre recherche..."
      />
      <button class="button-search" @click="searchPost">Search</button>
    </div>
    
    <div class="posts">
      <PostCard v-for="post in posts" :key="post.id" :post="post" />
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
      <span :data-current-page="currentPage"> Page {{ currentPage }} of {{ numPages }}</span>
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
import PostCard from "../components/PostCard.vue";

export default {
  name: "PostView",
  components: { PostCard },
  data() {
    return {
      posts: [],
      currentPage: 1,
      numPages: 1,
      searchQuery: "",
    };
  },
  mounted() {
    this.getPosts();
  },
  methods: {
    getPosts() {
      const url = this.searchQuery
        ? `/api/v1/post/?search=${this.searchQuery}&page=${this.currentPage}`
        : `/api/v1/post/?page=${this.currentPage}`;

      axios
        .get(url)
        .then((response) => {
          this.posts = response.data.posts;
          this.numPages = response.data.num_pages;
          this.currentPage = response.data.current_page;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    searchPost() {
      this.currentPage = 1; // Reset to first page on new search
      this.getPosts();
    },
    nextPage() {
      if (this.currentPage < this.numPages) {
        this.currentPage += 1;
        this.getPosts();
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;
        this.getPosts();
      }
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
.posts {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap; /* Permet aux cartes de passer à la ligne suivante si l'espace horizontal est insuffisant */
  width: 70vw;
  height: 55vh;
  gap: 5%;
  border: 10px solid black;
  border-radius: 75px;
}
.pagination {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 20px;
}
.pagination > span {
  background-color: white;
  border-radius: 25px;
  padding: 5px;
  font-size: 15px;
}

.button {
  margin: 0px 10px;
  background-color: white;
  border-radius: 25px;
  padding: 5px;
  font-size: 15px;
}
.search {
  border: 1px solid gray;
  margin: 1%;
  padding: 15px;
  border-radius: 25px;
}
.input {
  background-color: white;
  padding: 5px;
  border: none;
  border-radius: 25px;
}
.input::placeholder {
  color: black;
  font-size: 15px;
  letter-spacing: -0.5px;
  word-spacing: -0.1ch;
}
.input:focus {
  outline: none; /* Supprime l'outline par défaut pour avoir un contrôle complet sur le style */
  border: none; /* Ajoute une bordure plus épaisse et change sa couleur */
}
.button-search {
  background-color: white;
  color: black;
  padding: 5px;
  border: none;
  border-radius: 25px;
  transition: background-color 0.3s ease, transform 0.3s ease; /* Ajout d'animations pour la couleur de fond et la transformation */
}
.button-search:hover {
  transform: scale(1.05); /* Agrandit légèrement le bouton */
}
</style>
