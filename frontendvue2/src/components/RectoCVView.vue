<template>
    <div>
        <div id="pdf-container"></div>
    <div id="text-container"></div>
    </div>
</template>

<script>
import PDFJSViewer from 'pdfjs-viewer';
import axios from 'axios';

export default {
  data() {
    return {
      pdfURL: '', // URL du document PDF
      jsonData: [], // Données JSON provenant de la base de données
      textContent: '', // Contenu textuel traité à partir du JSON
    };
  },
  mounted() {
    // Récupérer les données JSON de la base de données
    axios.get('/api/json-data')
      .then(response => {
        this.jsonData = response.data;
        this.processTextContent(); // Extraire et formater le texte à partir du JSON
      })
      .catch(error => {
        console.error('Erreur lors de la récupération des données JSON :', error);
      });

    // Charger le document PDF
    const pdfContainer = document.getElementById('pdf-container');
    const viewer = new PDFJSViewer({
      container: pdfContainer,
    });
    viewer.load(this.pdfURL); // Remplacer par l'URL du PDF réel
  },
  methods: {
    processTextContent() {
      // Extraire et formater le contenu textuel à partir des données JSON
      // (La logique dépend de la structure de vos données JSON)
      this.textContent = this.jsonData.map(item => item.text).join('\n');
    },
  },
};
</script>


<style>

</style>