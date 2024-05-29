<template>
  <div>
    <button class="button" @click="toggleDisplay">Button</button>
    <div v-show="showRecto" class="recto">
      <div class="containercv">
        <div class="sidebar">
          <div class="contact-info">
            <p>Chagny</p>
            <p>0627237610</p>
            <p>guillaury.gv40@gmail.com</p>
            <p><a href="https://github.com/Eyery21">github.com/Eyery21</a></p>
          </div>
          <div class="skills">
            <h3>Compétences</h3>
            <p>FRONT-END: Vue.js</p>
            <p>BACK-END: Nodejs / Django / Symfony</p>
            <p>Languages: Javascript / Python / PHP / SQL</p>
            <p>Database: MongoDB/Mysql</p>
          </div>
          <div class="skills">
            <h3>soft skills</h3>
            <p>curiosité</p>
            <p>adaptabilité</p>
            <p>travail d'équipe</p>
            <p>anticipation</p>
            <p>patience</p>
          </div>
          <div class="interests">
            <h3>Centres d'Intérêt</h3>
            <p>Cinéma, jeux-vidéos</p>
          </div>
        </div>
        <div class="main-content">
          <div class="profile">
            <h1>Profil Professionnel</h1>
            <p>
              Futur étudiant en Pré-Msc à Epitech en septembre 2024, en
              recherche d'une alternance à partir de janvier 2025 pour une durée
              de 32 mois.
            </p>
          </div>
          <div class="experience">
            <h2>Parcours Professionnel</h2>
            <ul>
              <li>Cariste, Tempo - Chalon-sur-Saône - Intérim</li>
              <li>Cariste, Leader Intérim - Nantes - CDI</li>
            </ul>
          </div>
          <div class="projects">
            <h2>Projets Réalisés</h2>
            <p>OpenClassrooms, 3W Academy, Autre</p>
          </div>
          <div class="education">
            <h2>Certificats, Formations</h2>
            <p>Développeur Web et Mobile (2022)</p>
          </div>
        </div>
      </div>
    </div>
    <div v-show="!showRecto" class="verso">
      <div class="containercv">
        <p>rthdtkdtyjsdrthr</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showRecto: true
    };
  },
  methods: {
    toggleDisplay() {
      this.showRecto = !this.showRecto;
    }
  }
};
</script>

<style>
.recto {
  position: absolute;
  z-index: 5;
}
.verso {
  z-index: 1;
}
.containercv {
  background-color: rgb(165, 165, 173);
  display: flex;
  width: 900px;
  height: 800px;
  margin-left: auto;
  margin-right: auto;
  border: 1px solid noir;
}
.main-content {
  background-color: yellow;
  width: 700px;
}
.sidebar {
  width: 300px;
  background-color: gray;
}
.windows {
  display: flex;
  background-color: #941717;
  justify-content: center; /* Centrage horizontal */
  width: 100%;
  height: 100%;
}
.allprojects {
  display: flex;
  margin: auto;
  width: auto;
  height: 200px;
  background-color: rgb(59, 105, 105);
  justify-content: center; /* Centrage vertical des projets */
  align-items: center; /* Centrage horizontal des projets */
  border: 1px solid black;
}
.allprojects > h1 {
  top: 25%;
  bottom: 25%;
  margin-left: 50%;
  margin-right: 50%;
  color: red;
}
.projet {
  display: flex;
  flex-direction: column; /* Alignement vertical des éléments internes */
  align-items: center; /* Centrage horizontal des éléments internes */
  height: 100px;
  width: 200px;
  border: 1px solid white;
}
</style>
