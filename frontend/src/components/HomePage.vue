<template>
    <div class="home">
      <main-section></main-section>
      <main-grid></main-grid>
      <mainEconomic/>
      <main-politic></main-politic>
      <main-teach></main-teach>
      <main-culture/>
      <main-theme/>
    </div>
</template>

<script>
import mainEconomic from '@/components/mainEconomic.vue';
import MainSection from '@/components/mainSection.vue';
import mainGrid from '@/components/mainGrid.vue';
import mainPolitic from '@/components/mainPolitic.vue';
import mainTeach from '@/components/mainTeach.vue';
import mainCulture from '@/components/mainCulture.vue';
import mainTheme from "@/components/mainTheme.vue";
export default {
  name: 'MainPage',
  components: { MainSection, mainGrid, mainEconomic, mainPolitic, mainTeach, mainCulture, mainTheme },
}
</script>

<style scoped>

.home {
}

</style>