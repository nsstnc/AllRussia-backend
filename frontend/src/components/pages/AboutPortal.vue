<template>
  <div class="main-container">
  <mainSection/>
  <div class="wrapper">
    <div class="space-block">
      <div class="main-content">
        <div class="block">
          <span class="red-line"></span>
          <h2 class="block-title">МИССИЯ И ЗАДАЧИ ПОРТАЛА</h2>
          <p class="block-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut tellus elementum sagittis vitae et leo duis. Nulla porttitor massa id neque aliquam vestibulum morbi blandit. Sollicitudin nibh sit amet commodo nulla. Phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet enim. Id semper risus in hendrerit gravida rutrum quisque non tellus. Gravida arcu ac tortor dignissim convallis aenean et. Adipiscing diam donec adipiscing tristique risus nec feugiat. Fames ac turpis egestas maecenas pharetra.
            <br>
            <br>

            Enim neque volutpat ac tincidunt vitae semper quis lectus. Consequat ac felis donec et. Vel elit scelerisque mauris pellentesque pulvinar. Ut morbi tincidunt augue interdum velit euismod in. Sit amet dictum sit amet. Et tortor at risus viverra adipiscing at in. Eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus. Massa id neque aliquam vestibulum morbi blandit. In hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Non consectetur a erat nam at. Eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis orci. Ipsum consequat nisl vel pretium lectus.
          </p>
          </div>

        <div class="block">
          <span class="red-line"></span>
          <h2 class="block-title">УНИКАЛЬНОСТЬ ПРОЕКТА «Вся Россия»</h2>
          <p class="block-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut tellus elementum sagittis vitae et leo duis. Nulla porttitor massa id neque aliquam vestibulum morbi blandit. Sollicitudin nibh sit amet commodo nulla. Phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet enim. Id semper risus in hendrerit gravida rutrum quisque non tellus. Gravida arcu ac tortor dignissim convallis aenean et. Adipiscing diam donec adipiscing tristique risus nec feugiat. Fames ac turpis egestas maecenas pharetra.
            <br>
            <br>
            Enim neque volutpat ac tincidunt vitae semper quis lectus. Consequat ac felis donec et. Vel elit scelerisque mauris pellentesque pulvinar. Ut morbi tincidunt augue interdum velit euismod in. Sit amet dictum sit amet. Et tortor at risus viverra adipiscing at in. Eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus. Massa id neque aliquam vestibulum morbi blandit. In hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Non consectetur a erat nam at. Eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis orci. Ipsum consequat nisl vel pretium lectus.
          </p>
        </div>

        <div class="block">
          <span class="red-line"></span>
          <h2 class="block-title">ДЛЯ КОГО НАШ МАТЕРИАЛ</h2>
          <p class="block-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut tellus elementum sagittis vitae et leo duis. Nulla porttitor massa id neque aliquam vestibulum morbi blandit. Sollicitudin nibh sit amet commodo nulla. Phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet enim. Id semper risus in hendrerit gravida rutrum quisque non tellus. Gravida arcu ac tortor dignissim convallis aenean et. Adipiscing diam donec adipiscing tristique risus nec feugiat. Fames ac turpis egestas maecenas pharetra.
            <br>
            <br>
            Enim neque volutpat ac tincidunt vitae semper quis lectus. Consequat ac felis donec et. Vel elit scelerisque mauris pellentesque pulvinar. Ut morbi tincidunt augue interdum velit euismod in. Sit amet dictum sit am
            Enim neque volutpat ac tincidunt vitae semper quis lectus. Consequat ac felis donec et. Vel elit scelerisque mauris pellentesque pulvinar. Ut morbi tincidunt augue interdum velit euismod in. Sit amet dictum sit amet. Et tortor at risus viverra adipiscing at in. Eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus. Massa id neque aliquam vestibulum morbi blandit. In hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Non consectetur a erat nam at. Eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis orci. Ipsum consequat nisl vel pretium lectus.
          </p>
        </div>
      </div>
      <div class="navigate">
        <NavigateBar/>
      </div>
    </div>

  </div>

</div>
</template>

<script>
import mainSection from '../Main/mainSection.vue';
import NavigateBar from "@/components/layouts/NavigateBar.vue";
export default {
  name: 'AboutPortal',
  components: {mainSection, NavigateBar},
}
</script>

<style scoped>
.main-container {
  font-family: "Roboto", sans-serif;
}
.wrapper {
  max-width: 1440px;
  margin:0 auto;
}

.space-block {
  display: flex;
  justify-content: space-around;
  align-items: self-start;
}

.navigate {
  margin-top: 40px;
}

.title {
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: white;
  height: 685px;
  align-items: center;
  background-image:url('@/assets/city.png') ;
  background-repeat: no-repeat;
  background-size: cover;

}
.text {
  font-size: 120px;
}
.sub_title {
  font-size: 36px;
}
.main-content{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top:5rem;
}
.block {
  max-width: 800px;
  align-items: center;
  margin-bottom: 40px;
  border-top: 1px solid #000000;
}
.block-title {
  margin-right: auto;
  margin-bottom: 0px;
}
.block-text {
  font-family: "Roboto";
  font-weight: normal;
  font-size: 20px;
}
.red-line {
  width: 80px;
  height: 13px;
  background-color: #AA0000 ;
  margin-right: auto;
}
</style>