import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/pages/HomePage.vue';
import ArticlePolitic from './components/Article/ArticlePolitic.vue';
import AboutPortal from './components/About/AboutPortal.vue';
import Contact from './components/pages/ContactPage.vue';
import MoscowScreen from './components/MoscowScreen.vue';
import PartnerPage from './components/pages/PartnerPage.vue';
import CenterFO from "@/components/pages/CenterFO.vue";
import ProjectPage from '@/components/pages/ProjectPage.vue'



const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/article',
      name:'ArticlePolitic',
      component: ArticlePolitic
    },
    {
      path: '/about',
      name: 'AboutPortal',
      component: AboutPortal
    },

    {
      path: '/contact',
      name: 'Contact',
      component: Contact
    },

    {
      path: '/moscow',
      name: 'MoscowScreen',
      component: MoscowScreen
    },
    {
      path: '/partner',
      name: 'PartnerPage',
      component: PartnerPage
    },
    {
      path: '/CenterFO',
      name: 'CenterPage',
      component: CenterFO
    },
    {
      path: '/project',
      name: 'ProjectPage',
      component: ProjectPage
    },
  ]
});

export default router;