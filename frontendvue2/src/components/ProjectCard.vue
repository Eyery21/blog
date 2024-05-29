<template>
  <div class="project-card">
    <h2>{{ projet.title }}</h2>
    <p>{{ projet.description }}</p>
  </div>
</template>

<script>
export default {
  name: 'ProjectCard',
  props: {
    projet: Object
  }
};
</script>

<style scoped>
.project-card {
  /* Styles pour le composant ProjectCard */
}
</style>
