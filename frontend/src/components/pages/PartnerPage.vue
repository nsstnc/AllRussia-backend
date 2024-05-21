<template>
  <div class="main">
    <div class="wrapper">
      <div class="partners">
        <span class="red-line"></span>
        <div class="partners__title">
          <p class="title__heading">
            Партнеры
          </p>
        </div>

        <div class="partners__list list">
          <div v-for="partner in partners" :key="partner.id" class="list__card card">
            <img :src=" partner.url" :alt="partner.title" class="card__img">
            <p class="card__text">{{ partner.title }}</p>
          </div>
        </div>

      </div>
      <div class="navigate">
        <NavigateBar/>
      </div>
    </div>
  </div>
</template>

<script>
import NavigateBar from "@/components/layouts/NavigateBar.vue";
import axios from 'axios';

export default {
  name: 'MainPage',
  components: {
    NavigateBar,
  },
  data() {
    return {
      partners: {}
    };
  },
  mounted() {
    this.fetchPartners();
  },
  methods: {
    async fetchPartners() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/data_news_politics');
        this.partners = response.data;

        console.log(response.data)
      } catch (error) {
        console.error('Error fetching partners:', error);
      }
    }
  }
}
</script>

<style scoped>

.wrapper{
    display: flex;
    max-width: 1440px;
    margin: 0 auto;
}

.partners{
    width: 1120px;
    border-top: 1px solid black;
    margin-right: 32px;
}
.navigate {

}

.partners__list{
    display: flex;
    justify-content: space-between;
}

.card__img{
    max-width: 180px;
    max-height: 180px;
}


.title__headding{
    font-family: "Roboto Condensed";
    font-size: 24px;
    text-transform: uppercase;
}

.list__card{
    text-align: center;
}

.card__text{
    font-size: 24px;
    max-width: 280px;
}
.horizontal-line {
  height: 1px;
  width: 1440px;
  background-color: #000;
  margin: 0 auto;
}

</style>