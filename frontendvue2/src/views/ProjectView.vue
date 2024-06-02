<template>
    <v-container class="home">
      <v-carousel
        height="400"

        show-arrows="hover"
      >
      <template v-slot:prev="{ on, attrs }">
        <v-btn
          class="carousel-btn next-btn"
          color="info"
          v-bind="attrs"
          v-on="on"
        >
        
        prev slide</v-btn>
      </template>
        <template v-slot:next="{ on, attrs }">
          <v-btn
            class="carousel-btn prev-btn"
            color="success"
            v-bind="attrs"
            v-on="on"
          >next slide</v-btn>
        </template>
        <v-carousel-item v-for="(projet, i) in projets" :key="i">
        <ProjectCard :projet="projet" />
      </v-carousel-item>
      </v-carousel>
      
    </v-container>
  </template>
  
  <script>
  import axios from "axios";
  import ProjectCard from "../components/ProjectCard.vue";

  export default {
    name: "ProjectView",
    components: {
    ProjectCard,
  },
    data() {
      return {
        projets: [],
      };
    },
    mounted() {
      this.getProjets();
    },
    methods: {
      getProjets() {
        axios
          .get("/api/v1/projets/")
          .then((response) => {
            this.projets = response.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  .home {
    display: flex;
    background-color: #941717;
    justify-content: center;
    width: 100%;
    height: 100%;
  }
  
  .carousel-btn {
    position: absolute;
    top: 50%;
    z-index: 1;
  }
  
  .prev-btn {
    left: 1240px;
  }
  
  .next-btn {
    right: -200px;
  }
  

  </style>
  