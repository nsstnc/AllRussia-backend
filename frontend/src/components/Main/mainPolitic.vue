<script>
export default {
  name: 'mainPolitic'
};
</script>

<template>
  <div class="wrapper">
    <div class="horizontal-line"></div>
    <div class="red-rectangle"></div>
    <h3 >ПОЛИТИКА</h3>

      <div class="container">
        <div class="item item_1">
          <img src="../../assets/12%20(1).png" alt="12">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</p>
        </div>
        <div class="item item_2">
          <img src="../../assets/12%20(2).png" alt="12">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</p>
        </div>
        <div class="item item_3">
          <img src="../../assets/12%20(3).png" alt="12">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</p>
        </div>
        <div class="item item_4">
          <img src="../../assets/12%20(4).png" alt="12">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</p>
        </div>
      </div>

  </div>
</template>

<style scoped>


.container {
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 357px;
}

h3 {
  font-size: 24px;
  font-weight: normal;
  margin-top: 16px;
  margin-bottom: 24px;
}

.horizontal-line {
  height: 0.3px;
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

.item > p {
  font-family: "Roboto Condensed";
  font-size: 20px;
  font-weight: bold;
  margin-top: 16px;
}

</style>