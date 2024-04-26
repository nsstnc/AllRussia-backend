<template>
 <div>
   <div class="maps container">
     <div ref="map" style="width: 1000px; height: 500px"></div>
   </div>
 </div>
</template>

<script>
export default {
  mounted() {
    this.loadMap();
  },
  methods: {
    loadMap() {
      const ymaps = window.ymaps;

      ymaps.ready(() => {
        const map = new ymaps.Map(this.$refs.map, {
          center: [55.753215, 37.622504], // Координаты центра карты (Москва)
          zoom: 10, // Уровень масштабирования
        });

        // Добавление маркера на карту
        const marker = new ymaps.Placemark([55.753215, 37.622504], {
          hintContent: 'Москва',
          balloonContent: 'Столица России',
        });

        map.geoObjects.add(marker);
      });
    },
  },
};
</script>

<style scoped>

</style>
