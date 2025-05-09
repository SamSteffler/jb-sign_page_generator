<template>
  <div id="plant-detail">
    <div v-if="plant">
      <h1>{{ plant.common_name }}</h1>
      <div v-if="plant.images && plant.images.length">
        <h3>Galeria</h3>
        <div class="image-gallery">
        <img 
          v-for="(image, index) in plant.images" 
          :key="index" 
          :src="`/images/${image}`" 
          :alt="`${plant.common_name} - Image ${index + 1}`" 
          height="400"
          style="margin: 10px;"
          />
        </div>
      </div>
      <p><strong>Nome científico:</strong> <i>{{ plant.scientific_name }}</i></p>
      <p><strong>Tipo:</strong> {{ plant.type }}</p>
      <p><strong>Origem:</strong> {{ plant.origin }}</p>
      <p>{{ plant.description }}</p>
      <p><strong>Coordenadas:</strong> {{ plant.latitude }}, {{ plant.longitude }}</p>
    </div>
    <div v-else>
      <p>Planta não encontrada...</p>
    </div>
  </div>
</template>

<script>
import Papa from 'papaparse';

export default {
  data() {
    return {
      plant: null,
    };
  },
  mounted() {
    const id = this.$route.params.id;
    fetch('/data/plants-new.csv')
      .then(response => response.text())
      .then(csv => {
        Papa.parse(csv, {
          header: false,
          delimiter: ';',
          complete: (results) => {
            const match = results.data.find(p => p[0] === id);
            this.plant = {
              id: match[0],
              scientific_name: match[1],
              common_name: match[2],
              type: match[3],
              origin: match[4],
              latitude: match[5],
              longitude: match[6],
              description: match[7],
                images: match[8] ? match[8].split(',') : [],
            };
            console.log(this.plant);
          }
        });
      });
  }
};
</script>