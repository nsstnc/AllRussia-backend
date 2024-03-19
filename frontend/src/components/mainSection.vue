<script >

export default {
  name: 'mainSection',
}

</script>

<template>
  <div class="main__section">
   <div class="main__container">
     <h1 class="main__title">ALLRUSSIA</h1>
     <p class="main__subtitle">Мы открываем Россию заново! Вместе с вами!</p>
   </div>
  </div>
</template>

<style scoped>

.main__section {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 685px;
  background-image: url("@/assets/main.png");
  background-size: cover; /* Убедитесь, что изображение полностью покрывает область */
  background-position: center; /* Центрирует изображение */
}

.main__container {
  text-align: center; /* Центрирует текст внутри контейнера, если он занимает менее 100% ширины */
}



  .main__title {
    text-align: center;
    color: #ffffff;
    font-size: 120px;
    font-weight: 600;
  }

  .main__subtitle {
    text-align: center;
    color: #ffffff;
    font-size: 26px;
    font-weight: 500;
  }

</style>