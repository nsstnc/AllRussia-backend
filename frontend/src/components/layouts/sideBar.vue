<script>
  export default {
    name: 'sideBar',
  }
</script>

<template>
  <div class="container">
    <ul>
      <li>
        <img src="@/assets/loop.svg" alt="" class="sideBar-img">
      </li>
    </ul>

    <ul class="sideBar_list-one">
      <li class="sideBar-item"><a href="/about">ПОСЛЕДНИЕ НОВОСТИ</a></li>
      <li class="sideBar-item"><a href="/about">ПОЛИТИКА</a></li>
      <li class="sideBar-item"><a href="/about">ЭКОНОМИКА</a></li>
      <li class="sideBar-item"><a href="/about">НАУКА И ОБРАЗОВАНИЕ</a></li>
      <li class="sideBar-item"><a href="/about">КУЛЬТУРА И ИСТОРИЯ</a></li>
      <li class="sideBar-item"><a href="/about">СПОРТ</a></li>
      <li class="sideBar-item"><a href="/about">ТУРИЗМ</a></li>
    </ul>
    <div class="divider"></div>
    <ul class="sieBar_list-two">
      <li class="sideVar-item-two"><a href="/partner">ПАРТНЕРЫ</a></li>
      <li class="sideVar-item-two"><a href="/about">ПРОЕКТЫ</a></li>
    </ul>
    <div class="divider"></div>
    <ul class="sieBar_list-three">
      <li class="sideVar-item-three"><a href="/">ИНФОРМАЦИЯ</a></li>
      <li class="sideVar-item-three"><a href="/">СВЯЗАТЬСЯ С НАМИ</a></li>
    </ul>
    <ul class="sideBar_logos">
      <li class="sideBar_logos-item">
        <img src="@/assets/facebook.png">
      </li>
      <li class="sideBar_logos-item">
        <img src="@/assets/telegram%201.png">
      </li>
      <li class="sideBar_logos-item">
        <img src="@/assets/youtube-youtube%201.png">
      </li>
      <li class="sideBar_logos-item">
        <img src="@/assets/livejournal-svgrepo-com%201.png">
      </li>
    </ul>
  </div>
</template>

<style scoped>
.container {

}

ul {
  list-style-type: none;
  margin: 0;
}

li a{
  font-family: 'Roboto', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #ffffff;
  text-decoration: none;
}

.logo a{
  color: #ffffff;
  font-size: 20px;
}

li {
  padding-bottom: 20px;
}

.sideBar-img {
}

.container {
  position: fixed; /* Закрепляем сайдбар */
  top: 70px; /* Расположение сверху */
  left: 10px; /* Расположение слева */
  width: 310px;
  height: calc(100% - 150px);
  background-color: #222222;
  color: #FFFFFF;
  z-index: 1000; /* Убедитесь, что сайдбар находится поверх другого контента */
}

.divider {
  margin-bottom: 20px;
  width: 210px;
  margin-left: 40px;
  height: 2px; /* Толщина линии */
  background-color: #FFFFFF; /* Цвет линии */
}
.sideVar-item-three{
  opacity: 0.7;
}
.sideBar_logos {
  display: flex;
}
.sideBar_logos-item {
  padding-right: 10px;
}

</style>