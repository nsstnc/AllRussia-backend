
<template>
  <div class="wrapper">
    <div class="horizontal-line"></div>
    <div class="red-rectangle"></div>
    <h3 >ПОЛИТИКА</h3>
    <div class="wrapper_main">
      <div class="item item_main_1">
        <img src="@/assets/main-politic.png" alt="12">
      </div>
      <div class="item item_main_2">
        <h2 class="main_title">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit,
          sed do eiusmod tempor incididunt ut labore et dolore magna.
        </h2>
        <p class="main_subtitle">Александр Новиков | 4 дня назад</p>
        <p class="main_subtitle-1">Lorem ipsum dolor sit amet, consectetur adipiscing elit,
          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          Volutpat ac tincidunt vitae semper.
          Felis bibendum ut tristique et egestas quis ipsum suspendisse.
          Consequat id porta nibh venenatis. Cursus euismod quis viverra
          nibh cras pulvinar mattis nunc.
        </p>
      </div>
    </div>



    <div class="container">
      <div class="item item_1">
        <img src="@/assets/politic(3).png" alt="12">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit,
          sed do eiusmod tempor incididunt
          ut labore et dolore magna.
        </h2>
        <p class="main_subtitle">Александр Новиков | 2 дня назад</p>
      </div>
      <div class="item item_2">
        <img src="@/assets/politic(2).png" alt="12">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit,
          sed do eiusmod tempor incididunt.
        </h2>
        <p class="main_subtitle">Александр Смит | 43 минуты назад</p>
      </div>
      <div class="item item_3">
        <img src="@/assets/politic(1).png" alt="12">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit.
        </h2>
        <p class="container_subtitle">Александр Смит | Только что</p>
      </div>
      <div class="item item_4">
        <img src="@/assets/politic(4).png" alt="12">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit,
          sed do eiusmod tempor incididunt
          ut labore et dolore magna.
        </h2>
        <p class="container_subtitle">Александр Новиков | 1 день назад</p>
      </div>
    </div>
    <div class="horizontal-line"></div>
    <div class="red-rectangle"></div>
    <h3 >ПОЛИТИКА</h3>

    <div class="news_container">

      <div class="items item_1">
        <img src="@/assets/mainmama.png" alt="mama">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit,
          sed do eiusmod tempor incididunt
          ut labore et dolore magna.
        </h2>
        <p class="main_subtitle">Александр Смит | 43 минуты назад</p>
      </div>
      <div class="items item_2">
        <img src="@/assets/mainmama.png" alt="mama">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit,
          sed do eiusmod tempor incididunt
          ut labore et dolore magna.
        </h2>
        <p class="main_subtitle">Александр Смит | 43 минуты назад</p>
      </div>
      <div class="items item_3">
        <img src="@/assets/mainmama.png" alt="mama">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit,
          sed do eiusmod tempor incididunt
          ut labore et dolore magna.
        </h2>
        <p class="main_subtitle">Александр Смит | 43 минуты назад</p>
      </div>
      <div class="items item_4">
        <img src="@/assets/mainmama.png" alt="mama">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit,
          sed do eiusmod tempor incididunt
          ut labore et dolore magna.
        </h2>
        <p class="main_subtitle">Александр Смит | 43 минуты назад</p>
      </div>
      <div class="items item_5">
        <img src="@/assets/mainmama.png" alt="mama">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit,
          sed do eiusmod tempor incididunt
          ut labore et dolore magna.
        </h2>
        <p class="main_subtitle">Александр Смит | 43 минуты назад</p></div>
      <div class="items item_6">
        <img src="@/assets/mainmama.png" alt="mama">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit,
          sed do eiusmod tempor incididunt
          ut labore et dolore magna.
        </h2>
        <p class="main_subtitle">Александр Смит | 43 минуты назад</p>
      </div>
      <div class="items item_7">
        <img src="@/assets/mainmama.png" alt="mama">
        <h2 class="container_title">
          Lorem ipsum dolor sit amet,
          consectetur adipiscing elit,
          sed do eiusmod tempor incididunt
          ut labore et dolore magna.
        </h2>
        <p class="main_subtitle">Александр Смит | 43 минуты назад</p>
      </div>


    </div>


  </div>
</template>

<script>
export default {
  name: 'PoliticPage',
  components: {

  }
}

</script>

<style scoped>

.wrapper{
  margin-top: 80px;
  max-width: 1440px;
}

.container {
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 345px);
  grid-template-rows: 340px;
  grid-column-gap: 20px;
}
.wrapper_main {
  display: flex;
  justify-content: space-between;
  margin-bottom: 24px;
}


.news_container {
  display: grid;
  grid-template-columns: 953px;
  grid-template-rows: repeat(7, 280px);
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
.main_title {
  font-family: "Roboto Condensed";
  font-weight: bold;
  font-size: 40px;
  margin: 0 0 8px 0;
}
.main_subtitle {
  font-family: "Roboto", sans-serif;
  font-size: 14px;
  margin-bottom: 40px;
}
.main_subtitle-1 {
  font-size: 18px;
  font-family: "Roboto", sans-serif;
}
.item_main_1 {
  margin-right: 20px;
}
.container_title {
  font-family: "Roboto Condensed";
  font-weight: bold;
  font-size: 20px;
  margin-top: 8px;
}
.container_subtitle {
  font-size: 14px;
}


</style>