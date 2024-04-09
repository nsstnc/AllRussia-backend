<script >
 export default {
   name: 'HeaderHelp',
 }
</script>

<template>

  <div class="header__help">
    <p class="header_item">USD 81,95 <span class="item_dang">-0,02  <img src="@/assets/Arrow%201.png"></span></p>
    <p class="header_item">EUR 89,99 <span class="item_acc">+0,41  <img src="@/assets/Arrow%201(1).png"></span></p>
    <p class="header_item">CNY 11,87 <span class="item_acc">+0,02  <img src="@/assets/Arrow%201(1).png"></span></p>
    <p class="header_item">USD 81,95 <span class="item_acc">+0,03  <img src="@/assets/Arrow%201(1).png"></span></p>
  </div>

</template>

<style scoped>

  .header__help {
    font-family: "Roboto Condensed", sans-serif;
    height: 50px;
    background-color: #222222;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header_item {
    font-size: 14px;
    color: #ffffff;
    padding-right: 100px;
    padding-left: 100px;
  }
  .item_dang {
    padding-left: 7px;
    color: #FF3F3F;
  }
  .item_acc{
    padding-left: 7px;
    color: #4BFF68;
  }

  img {
    width: 10px;
    height: 10px;
  }

</style>