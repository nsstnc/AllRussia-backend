<script >
export default {
  name: 'ProjectPage',
}
</script>

<template>
  <div class="container">
    <div class="list__top top"></div>
    <div class="red-rectangle"></div>
    <div class="wrapper">
      <h2 class="wrapper__title">НАШИ ПРОЕКТЫ</h2>
        <div class="wrapper__container">
          <div class="item item_1">
            <img src="@/assets/1231233(3).png" alt="">
            <h3 class="item__title"> Lorem ipsum dolor sit amet, consectetur adipiscing.</h3>
            <p class="item__subtitle">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.
            </p>
          </div>
          <div class="item item_2">
            <img src="@/assets/1231233(2).png" alt="">
            <h3 class="item__title"> Lorem ipsum dolor sit amet, consectetur adipiscing.</h3>
            <p class="item__subtitle">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.
            </p>
          </div>
          <div class="item item_3">
            <img src="@/assets/1231233(4).png" alt="">
            <h3 class="item__title"> Lorem ipsum dolor sit amet, consectetur adipiscing.</h3>
            <p class="item__subtitle">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.
            </p>
          </div>
        </div>
      <div class="list__top top_1"></div>
      <div class="main__container">
        <div class="card card_1">
          <img src="@/assets/society.png" alt="">
          <h3 class="card__title">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.
          </h3>
            <p class="card__subtitle">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </p>
        </div>
        <div class="card card_2">
          <img src="@/assets/clock.png" alt="">
          <h3 class="card__title">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.
          </h3>
          <p class="card__subtitle">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.
          </p>
        </div>
        <div class="card card_3">
          <img src="@/assets/cityLondon.png" alt="">
          <h3 class="card__title">
            Lorem ipsum dolor sit amet.
          </h3>
          <p class="card__subtitle">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          </p>
        </div>
      </div>

      <div class="list__top top_1"></div>
      <div class="main__container">
        <div class="card card_1">
          <img src="@/assets/photo-project.png" alt="">
          <h3 class="card__title">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.
          </h3>
          <p class="card__subtitle">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          </p>
        </div>
        <div class="card card_2">
          <img src="@/assets/photo-project-1.png" alt="">
          <h3 class="card__title">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.
          </h3>
          <p class="card__subtitle">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod.
          </p>
        </div>
        <div class="card card_3">
          <img src="@/assets/photo-project-2.png" alt="">
          <h3 class="card__title">
            Lorem ipsum dolor sit amet.
          </h3>
          <p class="card__subtitle">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          </p>
        </div>
      </div>
    </div>
    
  </div>
</template>

<style scoped>

.container {
  max-width: 1440px;
  margin: 0 auto;
}

.red-rectangle {
  width: 88px; /* ширина прямоугольника */
  height: 8px; /* высота прямоугольника */
  background-color: #AA0000; /* цвет фона прямоугольника */
  margin-bottom: 10px;
}
.list__top{
  border-top: 1px solid #AAAAAA;
  margin-top: 80px;
}
.top_1 {
  margin-bottom: 32px;
}
.wrapper__container {
  display: grid;
  grid-template-columns: repeat(3, 345px);
  grid-template-rows: 449px;
  grid-column-gap: 41px;
  margin-bottom: 32px;
}

.item__title {
  font-size: 20px;
  margin: 8px 0 0 0;
}
.item__subtitle {
  margin: 8px 0 0 0;
  font-size: 16px;
}
.main__container {
  display: grid;
  grid-template-columns: repeat(3, 438px);
  grid-template-rows: 483px;
  grid-column-gap: 63px;
}



</style>