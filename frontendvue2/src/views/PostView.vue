<template>
  <div class="home">
    <input type="text" v-model="searchQuery" placeholder="Enter search term" />
    <button @click="searchPost">Search</button>
    <PostCard v-for="post in posts" :key="post.id" :post="post" />
    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ numPages }}</span>
      <button @click="nextPage" :disabled="currentPage === numPages">Next</button>
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
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.pagination {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>
