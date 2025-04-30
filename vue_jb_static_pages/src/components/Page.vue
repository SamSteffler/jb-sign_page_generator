<template>
  <div class="catalog" v-if="currentItem">
    <header>
      <h1 class="title">{{ currentItem.commonname }}</h1>
      <h2 class="subtitle">{{ currentItem.sciname }}</h2>
    </header>
    
    <div class="gallery">
      <div class="image-container">
        <img :src="`/images/${currentItem.image}`" :alt="currentItem.commonname" class="gallery-image" />
      </div>
    </div>
    
    <div class="descriptors">
      <p><strong>Latitude:</strong> {{ currentItem.latitude }}</p>
      <p><strong>Longitude:</strong> {{ currentItem.longitude }}</p>
      <p><strong>Origin:</strong> {{ currentItem.origin }}</p>
      <p><strong>Type:</strong> {{ currentItem.type }}</p>
      <p><strong>Description:</strong> {{ currentItem.description }}</p>
    </div>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script>
export default {
  props: ['id'], // Receive the ID from the route
  //created() {
 //   console.log('Received ID:', this.id);
 // },
  data() {
   return {
     items: [],
     currentItem: null,
   };
  },
  created() {
    console.log('Received ID in Page.vue:', this.id); // Log the received ID
  },
  async created() {
   // Fetch the JSON file
   const response = await fetch('/data/list.json');
   this.items = await response.json();
   console.log('Fetched items:', this.items);
   // Find the item with the matching ID
   console.log('Route ID:', this.id);
   this.currentItem = this.items.find(item => item.code === String(this.id));
   console.log('Matched item:', this.currentItem);

  }
};
</script>