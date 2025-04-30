import { createRouter, createWebHistory } from 'vue-router';
import Page from '../components/Page.vue';

const routes = [
  {
    path: '/item/:id',
    name: 'ItemPage',
    component: Page,
    props: route => {
      console.log('Route params:', route.params); // Log the route parameters
      return { id: route.params.id }; // Pass the `id` as a prop
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;