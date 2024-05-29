<template>
    <div class="home">
      <ProjectCard v-for="projet in projets" :key="projet.id" :projet="projet" />
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import ProjectCard from '../components/ProjectCard.vue';
  
  export default {
    name: 'ProjectView',
    components: {
      ProjectCard
    },
    data() {
      return {
        projets: []
      };
    },
    mounted() {
      this.getProjets();
    },
    methods: {
      getProjets() {
        axios.get('/api/v1/projets/')
          .then(response => {
            this.projets = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      }
    }
  };
  </script>
  