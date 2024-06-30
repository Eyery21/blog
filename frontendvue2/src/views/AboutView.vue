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
                  <h2>developpeur web</h2>
                </aside>
                <h3>Profil Professionnel</h3>
                <p>
                  Futur étudiant en Pré-Msc à Epitech en septembre 2024, en
                  recherche d'une alternance
                </p>
              </div>
              <div class="education">
                <h2>Certificats, Formations</h2>
                <p>Développeur Web et Mobile (2022)</p>
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
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Distinctio aliquid sint quae repellendus ex. Suscipit, neque?
              Cupiditate dolorum, laboriosam non tenetur excepturi ex!
              Voluptatum exercitationem architecto aperiam quas quisquam omnis.
            </p>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Distinctio aliquid sint quae repellendus ex. Suscipit, neque?
              Cupiditate dolorum, laboriosam non tenetur excepturi ex!
              Voluptatum exercitationem architecto aperiam quas quisquam omnis.
            </p>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Distinctio aliquid sint quae repellendus ex. Suscipit, neque?
              Cupiditate dolorum, laboriosam non tenetur excepturi ex!
              Voluptatum exercitationem architecto aperiam quas quisquam omnis.
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
        html2canvas: { scale: 2 },
        jsPDF: { unit: "px", format: [595, 842], orientation: "portrait" }, // format A4 en pixels
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
    background-color: rgb(165, 165, 173);
    width: 595px; /* largeur d'une page A4 */
  height: 842px; /* hauteur d'une page A4 */
        margin-left: auto;
    margin-right: auto;
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
  width: 595px;
  background-color: blue;
  width: 100%;
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
  background-color: yellow;
}
.sidebar {
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
  color: red;
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
  border: 1px solid white;
}
.contact-info > img {
  width: 90%;
  height: 200px;
  color: aliceblue;
}

.skills {
  margin: 1%;
  border: 1px solid white;
  margin: 5% 0%;
  height: auto;
}
.skills > h3 {
  margin: 1%;
}
.skills > ul {
  margin-top: 10px;
  background-color: #941717;
  align-items: end;
}
.skills > ul > li {
  list-style-type: none;
  font-size: small;
}
.main-content {
  display: flex;
  flex-direction: column;
  padding: 2%;
}
.profile,
.experience,
.projects {
  border-bottom: 2px solid black;
}
.profile {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 30%;
  background-color: red;
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
  height: 30%;
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;
}

.experience > h2 {
  /* font-size: 50%; */
}
.experience > h2,
p {
  margin: 10px 0 10px 0;
}

.projects {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: start;
  justify-content: center;
}
/* .projects > h2 {
} */
.projects > ul > li > ul > p {
  padding-left: 5px;
  color: red;
  display: flex;
  flex-direction: column;
  align-items: start;
}
.projects > ul > li {
  border: 1px solid black;
}
.projects > ul > li > ul {
  display: flex;
  flex-direction: column;
  align-items: start;
  background-color: aliceblue;
  list-style-type: none;
  font-size: 90%;
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
</style>
