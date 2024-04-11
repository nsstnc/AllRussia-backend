<script>
export default {
  name: 'mainCulture'
};
</script>

<template>
  <div >
    <div class="wrapper">
      <div class="horizontal-line"></div>
      <div class="red-rectangle"></div>
      <h3>КУЛЬТУРА И ИСТОРИЯ</h3>
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

  </div>
</template>

<style scoped>
.wrapper {
  margin-bottom: 90px;
}

.container {
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 357px;
}

.horizontal-line {
  height: 1px;
  width: 1440px;
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
  font-size: 24px;
  font-weight: normal;
}

</style>