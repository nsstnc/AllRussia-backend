<script >
export default {
  name: 'mainEconomic',
}

</script>

<template>
  <div class="wrapper" style="margin-bottom: 32px">
    <div class="horizontal-line"></div>
    <div class="red-rectangle"></div>
    <h3 >ЭКОНОМИКА</h3>

    <div class="container">
      <div class="item item_1">

        <div class="asd">
          <p class="item_1-txt">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</p>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Mollis aliquam ut porttitor leo a diam sollicitudin tempor. Curabitur vitae nunc sed velit dignissim sodales ut eu sem. </p>
        </div>
        <img src="../../assets/5.png" alt="">
      </div>
      <div class="item item_2">
        <div class="asd">
          <p class="item_1-txt">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</p>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Mollis aliquam ut porttitor leo a diam sollicitudin tempor. Curabitur vitae nunc sed velit dignissim sodales ut eu sem. </p>
        </div>
        <img src="../../assets/6.png" alt="">
      </div>
    </div>
  </div>
</template>

<style scoped>

.container {
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.item_1 {
  display: flex;
  justify-content: space-between;
}
.item_2 {
  display: flex;
  justify-content: space-between;
}
h3 {
  font-weight: normal;
  font-size: 20px;
  margin-top: 16px;
  margin-bottom: 24px;
}
.item_1-txt {
  font-family: "Roboto Condensed";
  font-weight: bold;
  font-size: 20px;
  line-height: 26px;
  margin-bottom: 20px;
  margin-top: 0;
}

.horizontal-line {
  height: 1px;
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

.asd {
  max-width: 223px;
  padding-right: 20px;
}
h3 {
  font-size: 24px;
}

</style>