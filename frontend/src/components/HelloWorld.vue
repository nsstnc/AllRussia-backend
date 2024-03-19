<template>
  <div class="main">
    <div class="banner">
      <h1 class="banner__headding">Центральный федеральный округ</h1>
    </div>
    <div class="list">
      <div class="wrapper">
        <div class="list__top top">
          <span class="top__line-red line-red"></span>
          <p class="top__text text-headdind">
            Столица рф
          </p>
          <div class="top__card card">
            <img class="card__img" src="" alt="">
            <div class="card__box">
              <p class="card__headding">
                Москва
              </p>
              <p class="card__text text-population">
                Население: 12 330 126 человек
              </p>
              <p class="card__text text-square">
                Площадь: 2,561 тыс.км²
              </p>
              <p class="card__text text-time">
                Часовой пояс: MSK (UTC+3)
              </p>
            </div>
          </div>
        </div>
        <div class="list__bottom bottom">
          <span class="bottom__line-red line-red"></span>
          <p class="bottom__text text-headdind">
            Регионы
          </p>
          <div class="bottom__list-cards">
            <div class="bottom__card card">
              <img class="card__img" src="" alt="">
              <div class="card__box">
                <p class="card__headding">
                  Москва
                </p>
                <p class="card__text text-population">
                  Население: 12 330 126 человек
                </p>
                <p class="card__text text-square">
                  Площадь: 2,561 тыс.км²
                </p>
                <p class="card__text text-time">
                  Часовой пояс: MSK (UTC+3)
                </p>
              </div>
            </div>
            <div class="bottom__card card">
              <img class="card__img" src="" alt="">
              <div class="card__box">
                <p class="card__headding">
                  Москва
                </p>
                <p class="card__text text-population">
                  Население: 12 330 126 человек
                </p>
                <p class="card__text text-square">
                  Площадь: 2,561 тыс.км²
                </p>
                <p class="card__text text-time">
                  Часовой пояс: MSK (UTC+3)
                </p>
              </div>
            </div>
            <div class="bottom__card card">
              <img class="card__img" src="" alt="">
              <div class="card__box">
                <p class="card__headding">
                  Москва
                </p>
                <p class="card__text text-population">
                  Население: 12 330 126 человек
                </p>
                <p class="card__text text-square">
                  Площадь: 2,561 тыс.км²
                </p>
                <p class="card__text text-time">
                  Часовой пояс: MSK (UTC+3)
                </p>
              </div>
            </div>
            <div class="bottom__card card">
              <img class="card__img" src="" alt="">
              <div class="card__box">
                <p class="card__headding">
                  Москва
                </p>
                <p class="card__text text-population">
                  Население: 12 330 126 человек
                </p>
                <p class="card__text text-square">
                  Площадь: 2,561 тыс.км²
                </p>
                <p class="card__text text-time">
                  Часовой пояс: MSK (UTC+3)
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
}
</script>

<style scoped>

p{
  margin: 0;
}

.wrapper{
  max-width: 1400px;
  margin: 0 auto;
}

/* banner */
.banner{
  background-repeat: no-repeat;
  background-size: 100% 100%;
  min-height: 340px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.banner__headding{
  font-size: 80px;
  font-weight: bold;
  color: white;
}

/* list */
.list{
  margin-top: 10px;
}

.list__top{
  border-top: 1px solid #AAAAAA;
}

.line-red{
  display: block;
  height: 13px;
  width: 80px;
  background-color: red;
}

.text-headdind{
  margin-top: 24px;
  font-size: 24px;
  text-transform: uppercase;
}

.list__bottom{
  border-top: 1px solid #AAAAAA;
  margin-top: 80px;
}

.bottom__list-cards{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}


/* card */
.card{
  display: flex;
  margin-top: 32px;
}

.card__box{
  display: flex;
  flex-direction: column;
  margin-left: 25px;
  justify-content: space-between;
}

.card__headding{
  font-size: 36px;
  font-weight: bold;
}

.card__text{
  font-size: 24px;
}

/* //////////////////// */

/* media request */

@media screen and (width < 1400px) {
  .bottom__list-cards{
    justify-content:center;
  }

  .top__card{
    justify-content: center;
  }

  .banner__headding{
    font-size: 60px;
  }
}

@media screen and (width < 1000px) {
  .banner__headding{
    font-size: 45px;
  }
}


</style>
