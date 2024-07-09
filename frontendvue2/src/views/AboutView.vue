<template>
  <div>
    <button class="buttonPDF" @click="downloadPDF">Télécharger en PDF</button>

    <div class="flip-box">
      <div class="flip-box-inner">
        <div class="recto">
          <div id="cv" class="containercv">
            <div class="sidebar">
              <div class="contact-info">
                <img src="@/assets/CV.png" alt="CV" />
                <p>Chagny</p>
                <p>0627237610</p>
                <p>guillaury.gv40@gmail.com</p>
                <p>
                  <a href="https://github.com/Eyery21">github.com/Eyery21</a>
                </p>
              </div>
              <div class="skills">
                <h3>Compétences</h3>
                <ul>
                  <li>FRONT-END: Vue.js</li>
                  <li>BACK-END: Nodejs / Django / Symfony</li>
                  <li>Languages: Javascript / Python / PHP / SQL</li>
                  <li>Database: MongoDB / Mysql / Oracle</li>
                </ul>
              </div>
              <div class="skills">
                <h3>soft skills</h3>
                <ul>
                  <li>curiosité</li>
                  <li>adaptabilité</li>
                  <li>travail d'équipe</li>
                  <li>anticipation</li>
                  <li>patience</li>
                </ul>
              </div>
              <div class="interests">
                <h3>Centres d'Intérêt</h3>
                <p>Cinéma, jeux-vidéos</p>
              </div>
            </div>
            <div class="main-content">
              <div class="profile">
                <aside>
                  <h1>guillaume vaury</h1>
                </aside>
                <p>
                  Futur étudiant en Pré-Msc à Epitech en septembre 2024, en
                  recherche d'une alternance
                </p>
              </div>
              <div class="education">
                <h2>Certificats, Formations</h2>
                <p>Développeur Web et Mobile (2022), OpenClassrooms</p>
              </div>

              <div class="projects">
                <h2>Projets Réalisés</h2>
                <ul>
                  <li>
                    <ul>
                      <p>OpenClassrooms</p>
                      <li>- Maquette en html/css</li>
                      <li>- Refonte SEO</li>
                      <li>- Création d'un réseau social d'entreprise</li>
                    </ul>
                  </li>
                  <li>
                    <ul>
                      <p>3W Academy</p>

                      <li>- Site de réservation d'album de musique(PHP)</li>
                    </ul>
                  </li>
                  <li>
                    <ul>
                      <p>Autre</p>

                      <li>- Site de gestion de collections de bandes</li>
                      <li>- Chatbot(Python)</li>
                      <li>- Site web de penses-bête( PHP/Symfony)</li>
                    </ul>
                  </li>
                </ul>
              </div>
              <div class="experience">
                <h2>Parcours Professionnel</h2>
                <p>Cariste, Tempo - Chalon-sur-Saône - Intérim</p>
                <p>Cariste, Leader Intérim - Nantes - CDI</p>
              </div>
            </div>
          </div>
        </div>
        <div class="verso">
          <div class="containercv">
            <p>
             Bonjour, vous lisez actuellement ma lettre de motivation, je ne suis pas favorable des lettres toutes faites, j'ai même une ldm toute prête pour troller ceux qui en exigent une, car pour moi, postuler c'est être motiver.

            </p>
            <p>
              Pour vous parler un peu de moi, j'ai découvert le code informatique il y a 2 ans, et depuis j'ai développer une pation devorante pour cet univers fait de 0 et de 1.

            </p>
            <p>
              Actuellement je fait des projets perso puisque je travail, mais à la rentrée 2024, j'entamerait une pre-MSCavec Epitech pour ensuite éssayer d'entamer une alternance visant un master de 7 au RNCP

            </p>
            <p>
              j'ai comencer par l'html/css, puis mon crane a exploser quans j'ai découvert la programation avec javascript, et s'est amadoué avec vue/nodes, et je me suis intéresser à php, puis à python que j'apprécie particulièrement.

            </p>
            <p>
              Si mon profil vous a intéresser, n'hésitez pas à me contacter et nous pourrons explorer le futur ensemble !
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showRecto: true,
    };
  },
  methods: {
    downloadPDF() {
      const element = document.getElementById("cv");
      const opt = {
        margin: 0,
        filename: "CV.pdf",
        image: { type: "jpeg", quality: 1.0 },
        html2canvas: { scale: 5 },
        jsPDF: { unit: "px", format: [794, 1123], orientation: "portrait" }, // format A4 en pixels
      };
      html2pdf().set(opt).from(element).save();
    },
    toggleDisplay() {
      this.showRecto = !this.showRecto;
    },
  },
};
</script>

<style>
.containercv {
  width: 794px; /* Largeur A4 en pixels */
  height: 1123px; /* Hauteur A4 en pixels */
  margin-left: auto;
  margin-right: auto;
  font-size: 17px;

}

.flip-box-inner {
  position: relative;
  transform-style: preserve-3d;

  transition: transform 0.6s;
}
.flip-box:hover .flip-box-inner {
  transform: rotateY(180deg);
}
.recto {
  width: 794px; /* Largeur A4 en pixels */
  height: 1123px; /* Hauteur A4 en pixels */
  background-color: blue;
}
.recto,
.verso {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}
.verso {
  transform: rotateY(180deg);
}
#cv {
  display: flex;
  margin: 0 auto;
  box-sizing: border-box;
}
.main-content {
  background-color: rgb(250, 250, 158);
  display: flex;
  gap: 2%;
}
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 4%;
  max-height: 1123px;
  padding: 0 1%;
  border-left: 1px solid black;
  border-top: 1px solid black;
  border-bottom: 1px solid black;
}
h3,
h2 {
  color: rgb(15, 14, 14);
  background-color: rgb(122, 180, 180);
  border-radius: 140px;
  border: 4%;
}
h3, h2 {
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 5%;
  padding: 1% 5%;
}
.windows {
  display: flex;
  justify-content: center; /* Centrage horizontal */
  width: 100%;
  height: 100%;
}
.allprojects {
  display: flex;
  margin: auto;
  width: auto;
  height: auto;
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
}
.projet {
  display: flex;
  flex-direction: column; /* Alignement vertical des éléments internes */
  align-items: center; /* Centrage horizontal des éléments internes */
  border: 1px solid white;
}
.contact-info {
  display: flex;
  flex-direction: column;
}
.contact-info > img {
  width: 90%;
  height: 200px;
  color: aliceblue;
}

.skills {
  margin: 5% 0%;
  
  height: auto;

}
.skills > h3 {
  margin-left: auto;
  margin-right: auto;
  width: 70%;
}
.skills > ul {
  margin-top: 15%;
  
  display: flex;
  flex-direction: column;
}
.skills > ul > li {
  margin: 2% 0%;
  text-align : left;

  list-style-type: none;


}
.main-content {
  display: flex;
  flex-direction: column;
  padding: 1%;
}
.profile,
.education,
.projects {
  border-bottom: 2px solid black;
}
.profile,
.education,
.projects,
.experience {

  padding: 8% 0%;
}
.profile {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.profile > aside {
  display: flex;
  flex-direction: column;
  align-items: start;
  width: auto;
  height: auto;
  text-transform: capitalize; /*transforme toutes les 1ere letrre de chaque mot en Majusqule */
}
.profile > aside > h1 {
  color: rgb(89, 166, 185);
  margin: 10px 0 10px 0;
}
.profile > aside > h2 {
  color: wheat;
  font-size: 0.7em;

  font: bold;
}

.experience {
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;
  margin: 2% 0%;
}

.experience > 
p {
  margin: 20px 0 10px 0;
}

.projects {
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;
}
/* .projects > h2 {
} */
 .projects > ul {
 }
.projects > ul > li > ul > p {
  padding-left: 5px;
  color: red;
  display: flex;
  flex-direction: column;
  align-items: start;
}
.projects > ul > li {
  display: flex;
  list-style-type: none;

}
.projects > ul > li > ul {
  margin: 5% 0%;

  display: flex;
  flex-direction: column;
  align-items: start;
  list-style-type: none;
  font-size: 17px;
}
.projects > ul {
  width: 100%;
  list-style-type: none;
  display: flex;
  flex-direction: column;
  align-items: start;
}
.education {
  display: flex;
  flex-direction: column;
  align-items: start;
}
.buttonPDF {
  border: 10px solid black;
}

@media print {
  .containercv {
    border: none;
  }

  .sidebar,
  .main-content {
    border: none;
  }

  .profile,
  .education,
  .projects,
  .experience {
    border-bottom: none;
  }
}
</style>
