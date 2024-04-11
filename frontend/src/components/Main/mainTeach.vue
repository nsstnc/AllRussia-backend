<script>

export default {
  name: 'mainTeach',
}
</script>

<template>
  <div class="wrapper">
    <div class="horizontal-line"></div>
    <div class="red-rectangle"></div>
    <h3>НАУКА И ОБРАЗОВАНИЕ</h3>
      <div class="container">
        <div class="item item_1">
          <img class="item_1-img" src="../../assets/syrikaty-2%201.png" alt="">
          <h3 class="title">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Mollis aliquam ut porttitor leo a diam sollicitudin tempor. Curabitur vitae nunc sed velit dignissim sodales ut eu sem. </p>
        </div>
        <div class="item item_2">
          <img src="../../assets/prem1%20(2).png" alt="">
          <p class="title">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</p>
        </div>
        <div class="item item_3">
          <img src="../../assets/prem1%20(3).png" alt="">
          <p class="title">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</p>
        </div>
        <div class="item item_4">
          <img src="../../assets/prem1%20(4).png" alt="">
          <p class="title">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</p>
        </div>
        <div class="item item_5">
          <img src="../../assets/prem1%20(1).png" alt="">
          <p class="title">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.</p>
        </div>
      </div>
  </div>
</template>

<style scoped>

.wrapper {
  margin-bottom: 60px;
}

.container {
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: repeat(2, 340px);
  grid-row-gap: 32px;
  grid-column-gap: 20px;
}

.item_1{
  grid-column: 1/3;
  grid-row: 1/3;
}

.item_1-img {
  width: 100%;
}

.horizontal-line {
  height: 1px;
  opacity: 0.4;
  width: 100%;
  background-color: #000;
  margin: 0 auto;
}

.red-rectangle {
  width: 88px; /* ширина прямоугольника */
  height: 8px; /* высота прямоугольника */
  background-color: #AA0000; /* цвет фона прямоугольника */
  margin-bottom: 10px;
}

h3 {
  margin-top: 16px;
  margin-bottom: 32px;
  font-size: 24px;
  font-weight: normal;
}

.title {
  font-family: "Roboto Condensed";
  font-size: 20px;
  font-weight: bold;
}

.title:first-child {
  margin-top: 16px;
  margin-bottom: 20px;
}

</style>