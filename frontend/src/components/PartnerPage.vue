<template>
    <div class="main">
        <div class="wrapper">
            <div class="partners">
                <span class="red-line"></span>
                <div class="partners__title">
                    <p class="title__headding">
                        Партнеры
                    </p>
                </div>
                <div class="partners__list list">
                    <div class="list__card card">
                        <img src="../assets/vulcan.png" alt="Вулкан камчатки" class="card__img">
                        <p class="card__text">
                            КГБУ Природный парк «Вулканы Камчатки»
                        </p>
                    </div>
                    <div class="list__card card">
                        <img src="../assets/telecomunication.png" alt="Вулкан камчатки" class="card__img">
                        <p class="card__text">
                            Международная академия связи
                        </p>
                    </div>
                    <div class="list__card card">
                        <img src="../assets/icenet.png" alt="Вулкан камчатки" class="card__img">
                        <p class="card__text">
                            ООО «Эйснет»
                        </p>
                    </div>
                </div>
            </div>
            <NavigationBar></NavigationBar>
        </div>
    </div>
</template>

<script>
import NavigationBar from "./NavigationBar.vue"

export default {
  name: 'MainPage',
  components: {
    NavigationBar,
  }
}

</script>

<style scoped>

.wrapper{
    display: flex;
    max-width: 1440px;
    margin: 0 auto;
    justify-content: space-between;
}

.partners{
    width: 1150px;
    border-top: 1px solid black;
}

.partners__list{
    display: flex;
    justify-content: space-between;
}

.card__img{
    max-width: 180px;
    max-height: 180px;
}

.title__headding{
    font-size: 24px;
}

.list__card{
    text-align: center;
}

.card__text{
    font-size: 24px;
    max-width: 280px;
}

</style>