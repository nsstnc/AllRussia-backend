<script >
 export default {
   name: 'HeaderHelp',
 }
</script>

<template>

  <div class="header__help">
    <ul class="wrapper header__help__container">
      <li class="header_item">USD 81,95 <span class="item_dang">-0,02  <img src="@/assets/Arrow%201.png"></span></li>
      <li class="header_item">EUR 89,99 <span class="item_acc">+0,41  <img src="@/assets/Arrow%201(1).png"></span></li>
      <li class="header_item">CNY 11,87 <span class="item_acc">+0,02  <img src="@/assets/Arrow%201(1).png"></span></li>
      <li class="header_item">USD 81,95 <span class="item_acc">+0,03  <img src="@/assets/Arrow%201(1).png"></span></li>
    </ul>
  </div>

</template>

<style scoped>
  .header__help {
    background-color: #222222;
  }
  .header__help__container {
    padding: 0;
    margin: 0 auto;
    list-style: none;
    height: 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header__help__container > li {
    font-family: "Roboto Condensed";
    font-weight: bold;
    font-size: 20px;
  }
  .header_item {
    font-size: 14px;
    color: #ffffff;
    padding-right: 100px;
    padding-left: 100px;
  }
  .item_dang {
    padding-left: 8px;
    color: #FF3F3F;
  }
  .item_acc{
    padding-left: 8px;
    color: #4BFF68;
  }

  img {
    width: 10px;
    height: 15px;
  }

</style>