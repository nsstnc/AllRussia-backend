<script>
import axios from 'axios';

export default {
  name: 'mainGrid',
  data() {
    return {
      same_as_article: [],
      main_article: {},
    };
  },
  mounted() {
    this.fetchMainArticle();
  },
  methods: {
    async fetchMainArticle() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/data_main_page');
        this.main_article = response.data.main_article[0];
        this.same_as_article = response.data.same_as_main.slice(0, 3);
        console.log(this.same_as_article)
      } catch (error) {
        console.error('Error fetching main article:', error);
      }
    }
  }
};

</script>

<template>

  <div class="container">
    <div class="item item_1">
      <div class="item_1-one">
        <h3 class="item_1-title">
          {{main_article.title}}
        </h3>
        <p class="item_1-subtitle">
          {{main_article.subtitle}}
        </p>
        <div class="vertical-line"></div>
        <p class="item_1-text">Похожие новости</p>
        <ul class="item_1-list">
          <li v-for="article in same_as_article" :key="article.id">
            {{ article.title }}
          </li>
        </ul>
      </div>
      <div class="item_1-two">
        <img class="item_1-img" src="../../assets/comunicacion%20politica%20(1)%201.png" style="height: 400px; width: 600px;" alt="123">
      </div>
    </div>
    <div class="item item_2">
      <div class="horizontal-line"></div>
      <div class="red-rectangle"></div>
      <h3 class="item_2-title">
        Последние новости
      </h3>
      <img src="../../assets/284320788be7027b8bea3f687155b7fb%201.png" alt="asd" style="width: 300px">
      <p class="item_2-subtitle">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
      </p>
      <p class="asd">17 минут назад</p>
      <div class="diviver"></div>
      <p class="item_2-list">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
      </p>
      <div class="diviver"></div>
      <p class="item_2-list">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
      </p>
      <div class="diviver"></div>
      <p class="item_2-list">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
      </p>
      <div class="diviver"></div>
      <p class="item_2-list">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
      </p>
      <div class="diviver"></div>
      <p class="item_2-list">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
      </p>

    </div>
    <div class="item item_3">
      <img src="../../assets/1.png" alt="">
      <p class="dsa">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
    </div>
    <div class="item item_4">
      <img src="../../assets/2.png" alt="">
      <p class="dsa">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
    </div>
    <div class="item item_5">
      <img src="../../assets/3.png" alt="">
      <p class="dsa">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.</p>
    </div>
  </div>


</template>

<style scoped>

.container {
  margin: 0 auto;
  margin-top: 80px;
  width: 1440px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: repeat(2, 400px);
  grid-row-gap: 32px;
  grid-column-gap: 20px;
}
.item_1 {
  display: flex;
  justify-content: space-between;
  grid-column: 1/4;
}
.item_2 {
  max-width: 300px;
  grid-column: 4/4;
  grid-row: 1/3;
}

.horizontal-line {
  height: 1px;
  width: 100%;
  background-color: #000;
  margin: 0 auto;
}

.vertical-line {
  height: 1px; /* Высота линии */
  width: 140px; /* Ширина линии */
  background-color: black; /* Цвет линии */
  opacity: 0.4;
}
.diviver {
  height: 1px;
  width: 100%;
  background-color: black;
}
.item_2-title {
  margin: 8px 0;
  font-weight: normal;
}
.item_2-subtitle {
  font-family: "Roboto Condensed";
  margin: 8px 0;
  font-size: 20px;
  font-weight: bold;
}
.item_2-list {
  font-family: "Roboto";
  font-size: 16px;
  font-weight: normal;
}

.asd {
  margin-top: 0;
  margin-bottom: 12px;
  color: #AA0000;
  font-size: 12px;
}
.dsa {
  font-weight: 600;
  font-size: 18px;
}
.red-rectangle {
  width: 88px;
  height: 8px;
  background-color: #AA0000;
}



.item_1-title {
  margin: 0;
  width: 300px;
  font-size: 20px;
  padding: 0 10px 10px 10px;
}
.item_1-subtitle {
  padding: 0 10px 10px 10px;
  font-size: 16px;
}

.item_1-text {
  padding: 10px 10px 10px 10px;
  font-size: 20px;
  font-weight: 600;
}

.item_1-list {
  padding: 0 30px 30px 40px;
}


</style>