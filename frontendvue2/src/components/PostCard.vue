<template>
  <div class="post">
    <h2 class="title">{{ post.title }}</h2>
    <p class="content">{{ post.content }}</p>
    <p class="content">{{ post.language }}</p>
    <p class="content">{{ post.category }}</p>
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

<style scoped>
.post {
  display: flex;
  flex-direction: column;
  align-items: center; /* Centre les éléments à l'intérieur de la carte */
  justify-content: space-between; /* Distribue l'espace */
  margin: 10px; /* Marge uniforme pour l'espacement entre les cartes */
  padding: 20px; /* Rembourrage à l'intérieur de la carte */
  background-color: #f9f9f9; /* Couleur de fond plus douce */
  border: 1px solid #ccc; /* Bordure subtile */
  box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Ombre douce pour un effet 3D */
  border-radius: 45px; /* Coins arrondis */
  width: 300px; /* Largeur fixe */
  height: auto; /* Hauteur automatique */
  overflow: hidden; /* Assure qu'il n'y ait pas de débordement */
  text-overflow: ellipsis; /* Empêche le texte de déborder */
  white-space: normal; /* Permet le retour à la ligne du texte */
}

.title {
  margin-top: 0; /* Supprime la marge en haut du titre */
  color: #333; /* Couleur foncée pour le texte pour une meilleure lisibilité */
  font-size: 18px; /* Taille de police légèrement plus grande */
}

.content {
  color: #666; /* Couleur de texte plus claire pour le contenu */
  font-size: 16px; /* Taille de police lisible */
  line-height: 1.5; /* Espacement des lignes amélioré */
}
</style>
