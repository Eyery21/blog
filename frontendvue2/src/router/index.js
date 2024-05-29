import Vue from 'vue';
import VueRouter from 'vue-router';
import PostView from '../views/PostView.vue';
import HomeView from '../views/HomeView.vue';
import NoteView from '../views/NoteView.vue';
import ProjectView from '../views/ProjectView.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
  },

  {
    path: '/notes',
    name: 'notes',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: NoteView,
  },
  {
    path: '/posts',
    name: 'posts',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: PostView,
  },
  {
    path: '/projets',
    name: 'projects',
    component: ProjectView,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
