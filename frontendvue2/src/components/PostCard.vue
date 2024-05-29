<template>
  <div class="home">
    <h2>{{ post.title }}</h2>
    <h2>{{ post.content }}</h2>
  </div>
</template>

<script>
export default {
  name: "PostCard",
  props: {
    post: Object,
  },
};
</script>

</script>

<style scoped>
</style>