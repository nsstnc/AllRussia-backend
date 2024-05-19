<script>
export default {
  name: 'NavigateBar',
  data() {
    return {
      links: {
        name: 'О ПОРТАЛЕ',
        name1: 'ПАРТНЕРЫ',
        name2: 'КОНТАКТЫ',
        name3: 'ПРОЕКТЫ',
      },
      currentPage: '',
    }
  },
  methods: {
    setCurrentPage() {
      this.currentPage = this.$route.path.substring(1);
    }
  },
  created() {
    this.setCurrentPage();
  },
  watch: {
    '$route': 'setCurrentPage'
  }
}
</script>

<template>
  <div class="navigate container">
    <div class="horizontal-line"></div>
    <div class="red-rectangle"></div>
    <div class="navigate wrapper">
      <ul class="navigate list">
        <li class="navigate items item_1"><router-link to="/">ALLRUSSIA</router-link></li>
        <div class="horizontal-line"></div>
        <li class="navigate items item_2 " ><router-link to="/about"><span :class="{ 'active': currentPage === 'about' }">{{links.name}}</span></router-link></li>
        <div class="horizontal-line"></div>
        <li class="navigate items item_2"><router-link to="/partner"><span :class="{'active': currentPage ==='partner'}">{{links.name1}}</span></router-link></li>
        <div class="horizontal-line"></div>
        <li class="navigate items item_2"><router-link to="/contact"><span :class="{'active': currentPage === 'contact'}">{{ links.name2 }}</span></router-link></li>
        <div class="horizontal-line"></div>
        <li class="navigate items item_2"><router-link to="/project"><span :class="{'active': currentPage === 'project'}">{{ links.name3 }}</span></router-link></li>
        <div class="horizontal-line"></div>

      </ul>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 288px;
  max-height: 351px;
}
.active {
  color: red;
}

.list {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 0;

}
.items {
  list-style-type: none;
  padding: 17px;
}
a {
  color: black;
  text-decoration: none;
}
.item_1 {
  font-family: "Roboto Condensed";
  font-size: 36px;
  font-weight: bold;
  padding: 24px;
}
.item_2 {
  font-family: "Roboto Condensed";
  font-size: 24px;
}

.horizontal-line {
  height: 1px;
  width: 100%;
  background-color: rgba(0,0,0,0.24);
  margin: 0 auto;
}
.red-rectangle {
  width: 88px; /* ширина прямоугольника */
  height: 13px; /* высота прямоугольника */
  background-color: #AA0000; /* цвет фона прямоугольника */
  margin-bottom: 10px;
}

</style>