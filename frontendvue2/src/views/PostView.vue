<template>
  <div class="home">
    <PostCard v-for="post in posts" :key="post.id" :post="post" />
  </div>
</template>

<script>
import axios from 'axios';
import PostCard from '../components/PostCard.vue';


export default {
  name: 'PostView',
  components: {
    PostCard
  },
  data() {
    return {
      posts: [],
    };
  },
  mounted() {
    this.getPosts();
  },
  methods: {
    getPosts() {
      axios.get('/api/v1/post/')
        .then((response) => {
          this.posts = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
