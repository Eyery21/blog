<template>
  <v-card class="project-card">
    <v-card-title class="title">
      {{ projet.title }}
    </v-card-title>
    <v-card-text>
      {{ projet.description }}
    </v-card-text>
    <v-card-text>
      {{ projet.project_link }}
    </v-card-text>
    <v-card-text>
      <img class="image" :src="`${mediaUrl}${projet.image}`" alt="Project Image" />
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'ProjectCard',
  props: {
    projet: Object
  },
   data() {
    return {
      mediaUrl: 'http://127.0.0.1:8000/'
    }
  }
};
</script>

<style scoped>
.project-card {
  border: 15px solid rgb(128, 128, 128);
  justify-content: center;
  width: 100%;
  height: 100%;
  
}
.title {
  color: blue;
  justify-content: center;
}
.image {
  width: 200px;
  height: 100px;
}
</style>
