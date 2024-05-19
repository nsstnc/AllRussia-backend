<script >
import NavigateBar from "@/components/layouts/NavigateBar.vue";
export default {
  name: 'ProjectPage',
  components: {
    NavigateBar,
  }
}
</script>

<template>
  <div class="container">
    <div class="justify">
      <div class="wrapper">
        <div class="list__top top"></div>
        <div class="red-rectangle"></div>
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
      </div>
      <div class="navigate">
        <NavigateBar/>
      </div>

    </div>

    </div>
</template>

<style scoped>

.container {
  max-width: 1440px;
  margin: 0 auto;
}
.justify {
  margin-top: 80px;
  display: flex;
  justify-content: space-between;
}

.red-rectangle {
  width: 88px; /* ширина прямоугольника */
  height: 8px; /* высота прямоугольника */
  background-color: #AA0000; /* цвет фона прямоугольника */
  margin-bottom: 10px;
}
.list__top{
  border-top: 1px solid #AAAAAA;
}
.top_1 {
  margin-bottom: 32px;
}
.wrapper__title{
  max-width: 1120px;
}

.wrapper__container {
  display: grid;
  grid-template-columns: repeat(3, 345px);
  grid-template-rows: 449px;
  grid-column-gap: 41px;
  margin-bottom: 32px;
  max-width: 1121px;
}

.item__title {
  font-size: 20px;
  margin: 8px 0 0 0;
}
.item__subtitle {
  margin: 8px 0 0 0;
  font-size: 16px;
}



</style>