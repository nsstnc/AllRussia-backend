<template>
  <div>
    <div class="header">
      <div class="item item_1">
        <button class="header__btn" @click="showSideBar = !showSideBar">
          <div class="menu-icon" :class="{'open': showSideBar}">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </button >
      </div>
      <div class="wrapper">
        <div class="menu__container">
          <div class="header__logo">ALLRUSSIA</div>
          <div class="vertical__line"></div>
          <div class="header__items">ВСЯРОССИЯ</div>
          <div class="header__items">РФ</div>
          <div class="header__items">СНГ</div>
          <div class="header__items">АРАБСКИЙ МИР</div>
          <div class="header__items">ШКОЛА РУССКОГО ЯЗЫКА РКИ+</div>
          <div class="vertical__line"></div>
          <div class="header__items"><img class="img" src="@/assets/yarussski.png" alt=""></div>
        </div>
      </div>
    </div>

    <div class="divider"></div>

    <HeaderHelp/>
    <Transition>
      <SideBar v-if="showSideBar"/>
    </Transition>


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

.v-enter-active,
.v-leave-active {
  transition: opacity .2s ease-in;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}

.header {
  display: flex;
  align-items: center;
  font-family: "Roboto Condensed";
  font-weight: bold;
  background-color: #222222;
  color: #FFFFFF;
  height: 70px;
  position: fixed;
  width: 100%;
  z-index: 1000;
}

.menu__container {
  width: 1440px;
  margin: auto;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}

.vertical__line {
  border: 2px solid white;
  height: 40px;
}

.menu-icon > span {
  display: block;
  width: 35px;
  margin-bottom: 5px;
  border: 2px solid white;
  transition: all 0.3s ease-in-out;
}

.menu-icon > span:last-child {
  margin-bottom: 0;
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
  cursor: default;
  font-size: 36px;
}

.header__items {
  cursor: pointer;
  font-size: 24px;
}

.header__list {
  display: flex;
  align-items: center;
  margin: 0 auto;
  list-style: none;
  padding: 0;
  font-size: 16px;
}

.divider {
  height: 71px; /* Толщина линии */
  background-color: #FFFFFF; /* Цвет линии */
}

.header__btn {
  margin-left: 40px;
  border: none;
  cursor: pointer;
  background-color: transparent;
  padding: 0;
}

.image-button img {
  width: 50px;
  height: auto;
  display: block;
}

.content {
  transition: transform 0.3s ease-out;
}

</style>
