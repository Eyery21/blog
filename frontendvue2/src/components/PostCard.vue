<template>
  <div class="home">
    <div class="post">
      <p class="content">{{ post.id }}</p>
      <h2 class="titre">{{ post.title }}</h2>
      <p class="content">{{ post.created_at }}</p>
      <p class="content">{{ post.content }}</p>
      <p class="content">{{ post.language }}</p>
      <p class="content">{{ post.category }}</p>
    </div>
    <div class="heart">
      <p class="content">{{ post.like }}</p>
      <p class="content">{{ post.dislike }}</p>
    </div>
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
.home {
  display: flex;
}
.post {
  width: 200px;
}
.titre {
  border: 1px solid black;
}
.content {
  border: 2px solid black;
}
.heart {
  display: flex;
}
</style>