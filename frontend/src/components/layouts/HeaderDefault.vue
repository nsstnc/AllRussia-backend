<template>
  <div>
    <header class="header">
      <div class="item item_1">
        <button class="header__btn" @click="showSideBar = !showSideBar">
          <div class="menu-icon" :class="{'open': showSideBar}">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </button >
        <span class="header__logo">ALLRUSSIA</span>
        <div class="vertical-line"></div>
      </div>
      <div class="item item_2">

        <ul class="header__list">
          <li class="header__items">ВСЯРОССИЯ</li>
          <li class="header__items">РФ</li>
          <li class="header__items">СНГ</li>
          <li class="header__items">АРАБСКИЙ МИР</li>
          <li class="header__items">ШКОЛА РУССКОГО ЯЗЫКА РКИ+</li>
          <li class="vertical-line"></li>
        </ul>

      </div>

      <div class="item item_3">
        <img class="img" src="@/assets/yarussski.png" alt="">
      </div>

    </header>

    <div class="divider"></div>

    <HeaderHelp/>
    <div class="content" :class="{'open' :showSideBar}">
      <SideBar v-if="showSideBar"/>
    </div>


  </div>
</template>

<script>
import HeaderHelp from '@/components/layouts/headerHelp.vue';
import SideBar from "@/components/layouts/sideBar.vue";

export default {
  data: () => {
    return {
      showSideBar: false

    }
  },

name: 'HeaderSide',
  components: { HeaderHelp, SideBar }
}
</script>

<style scoped>

.header {
  font-family: "Roboto Condensed";
  font-weight: bold;
  display: grid;
  align-items: center;
  grid-template-columns: 1fr 1.5fr 1fr;
  background-color: #222222;
  color: #FFFFFF;
  height: 70px;
  position: fixed; /* Добавляем это свойство */
  top: 0; /* Устанавливаем заголовок в верхней части страницы */
  left: 0; /* Растягиваем заголовок на всю ширину слева */
  right: 0; /* Растягиваем заголовок на всю ширину справа */
  z-index: 1000; /* Убедитесь, что заголовок находится поверх других элементов */
}
.menu-icon {
  padding-left: 26px;
}
.img {
  padding-right: 70px;
}
.menu-icon span {
  display: block;
  width: 33px;
  height: 4px;
  margin-bottom: 5px;
  background: #FFFFFF;
  transition: all 0.3s ease-in-out;
}

.menu-icon.open span:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}

.menu-icon.open span:nth-child(2) {
  opacity: 0;
}

.menu-icon.open span:nth-child(3) {
  transform: rotate(-45deg) translate(7px, -8px);
}

.header__logo {
  padding-right: 26px;
  font-size: 36px;
}

.item_1 {
  align-items: center;
  display: flex;
  justify-content: space-between;
}

.header__list {
  align-items: center;
  display: flex;
  justify-content: space-between;
  list-style: none;
  font-size: 16px;
}

.item_3{
  display: flex;
  justify-content: center;
  align-items: center;
}

.search-input {
  margin-left: 26px;
  width: 237px;
  height: 33px;
  font-size: 16px;
  padding-left: 40px;
  color: #FFFFFF;
  background-color: #333333;
  border: none;
}

.divider {
  height: 71px; /* Толщина линии */
  background-color: #FFFFFF; /* Цвет линии */
}

.header__btn {
  border: none; /* Убираем стандартные границы кнопки */
  cursor: pointer; /* Добавляем стиль курсора, указывающего на возможность клика */
  background-color: transparent; /* Делаем фон кнопки прозрачным */
  padding: 0; /* Убираем внутренние отступы */
}

.image-button img {
  width: 50px; /* Устанавливаем желаемую ширину изображения */
  height: auto; /* Автоматически рассчитываем высоту, чтобы сохранить пропорции */
  display: block; /* Убираем возможные отступы вокруг изображения */
}

.content {
  transition: transform 0.3s ease-out;
}
.vertical-line {
  height: 36px;
  border-left: 3px solid white; /* задаем стиль и цвет вертикальной линии */
}



</style>
