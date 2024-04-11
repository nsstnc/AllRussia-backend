<template>
  <div class="container">
    <nav class="nav">
      <ul class="nav__list">
        <li class="nav__item" :class="{ active: currentPage === 'home' }"><router-link to="/">О ПОРТАЛЕ</router-link></li>
        <li class="nav__item" :class="{ active: currentPage === 'about' }"><router-link to="/about">ПАРТНЕРЫ</router-link></li>
        <li class="nav__item" :class="{ active: currentPage === 'contact' }"><router-link to="/contact">КОНТАКТЫ</router-link></li>
        <li class="nav__item" :class="{ active: currentPage === 'contact' }"><router-link to="/contact">ПРОЕКТЫ</router-link></li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentPage: ''
    };
  },
  watch: {
    '$route'(to) {
      this.currentPage = to.name;
    }
  },
  created() {
    this.currentPage = this.$route.name;
  }
};
</script>

<style scoped>
.active {
  color: red;
}
</style>