<script >

export default {
  name: 'mainSection',
}

</script>

<template>
  <div class="main__section ">
    <div class="main__container">
      <div class=" text-center text-white text-[200px] font-bold font-['Roboto Condensed']">ALLRUSSIA</div>
        <div class=" text-center text-white text-4xl font-bold font-['Roboto Condensed']">Мы открываем Россию заново! Вместе с вами!</div>
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
  background-size: cover;
  background-position: center;
}


</style>