<template>
  <div class="home">
    <div class="tri">
      <ul>
        <li>pagination</li>
        <li>search bar</li>
        <li>crud</li>
        <li></li>
      </ul>
    </div>
    <div>

      <input class="input" type="text" v-model="searchQuery" placeholder="Enter search term" />
      <button class="button-search" @click="searchPost">Search</button>
      <PostCard v-for="post in posts" :key="post.id" :post="post" />
      <div class="pagination">
        <button class="button" @click="prevPage" :disabled="currentPage === 1">page précédente </button>
        <span> Page {{ currentPage }} of {{ numPages }}</span>
        <button class="button" @click="nextPage" :disabled="currentPage === numPages">    page suivante    </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PostCard from '../components/PostCard.vue';

export default {
  name: 'PostView',
  components: { PostCard },
  data() {
    return {
      posts: [],
      currentPage: 1,
      numPages: 1,
      searchQuery: ''
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
        
      axios.get(url)
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
      this.currentPage = 1;  // Reset to first page on new search
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
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.tri {
  background-color: yellow;
  width: 200px;
  height: 700px;
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
