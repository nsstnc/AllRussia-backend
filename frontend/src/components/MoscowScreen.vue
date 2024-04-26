<template>
  <div class="main">
    <div class="wrapper">
      <div class="headding">
        <img class="headding__logo" src="@/assets/gerb.svg" alt="Герб">
        <p class="headding__text">Москва</p>
      </div>
      <div class="box">
        <p class="box__text">Население:  12 330 126 человек</p>
        <p class="box__text">Площадь: 2,561 тыс.км²  </p>
      </div>
      <div class="box box-borderbottom">
        <p class="box__text">Часовой пояс:  MSK (UTC+3) </p>
        <p class="box__text">Статус: Город Федерального значения, Столица Российской Федерации </p>
        <p class="box__text">Автомобильный код: 77, 177, 777; 97, 197, 797; 99, 199, 799  </p>
        <p class="box__text">Официальные сайты: Правительство Москвы, Московская городская Дума </p>
        <p class="box__text">Мэр города: Московская городская Дума </p>
        <p class="box__text">Экономический район: Центральный</p>
      </div>
      <div class="list">
        <div class="list__card card vis1100px">
          <p class="card__text">Москва́ — столица России, город федерального значения, административный центр Центрального федерального округа и центр Московской области, в состав которой не входит. Мегаполис; крупнейший по численности населения город России и её субъект — 13 104 177 человек (2023), самый населённый из городов, полностью расположенных в Европе, занимает 22-е место среди городов мира по численности населения. Центр Московской городской агломерации. Самый крупный город Европы по площади.</p>
          <img src="@/assets/hram.png" alt="Храм" class="card__img">
        </div>
        <div class="list__card card invis1100px bordertop">
          <img src="@/assets/hram.png" alt="Храм" class="card__img">
          <p class="card__text">Москва́ — столица России, город федерального значения, административный центр Центрального федерального округа и центр Московской области, в состав которой не входит. Мегаполис; крупнейший по численности населения город России и её субъект — 13 104 177 человек (2023), самый населённый из городов, полностью расположенных в Европе, занимает 22-е место среди городов мира по численности населения. Центр Московской городской агломерации. Самый крупный город Европы по площади.</p>
        </div>
        <div class="list__card card">
          <img src="@/assets/town.png" alt="Здание" class="card__img">
          <p class="card__text">Археологические данные свидетельствуют о существовании городского поселения в районе будущего Кремля с XI века. Первое письменное упоминание о Москве относится к 1147 году: история города насчитывает, по меньшей мере, 876 лет. Москва — историческая столица Великого княжества Московского, Русского царства, Российской империи (в 1728—1732 годах), Советской России и СССР. Город-герой. В Москве находятся федеральные органы государственной власти Российской Федерации (за исключением Конституционного суда), посольства иностранных государств, штаб-квартиры большинства крупнейших российских коммерческих организаций и общественных объединений.</p>
        </div>
        <div class="list__card card vis1100px">
          <p class="card__text">Расположена на западе России, на реке Москве в центре Восточно-Европейской равнины, в междуречье Оки и Волги. Как субъект федерации, Москва граничит с Московской и Калужской областями. Москва включает 6 городских населённых пунктов, в том числе 4 города и 2 посёлка городского типа, а также большое количество сельских населённых пунктов. Ряд подмосковных городов, посёлков городского типа и сельских населённых пунктов были включены в состав Москвы и утратили свой статус.</p>
          <img src="@/assets/mcity2.png" alt="Город" class="card__img">
        </div>
        <div class="list__card card invis1100px">
          <img src="@/assets/mcity2.png" alt="Город" class="card__img">
          <p class="card__text">Расположена на западе России, на реке Москве в центре Восточно-Европейской равнины, в междуречье Оки и Волги. Как субъект федерации, Москва граничит с Московской и Калужской областями. Москва включает 6 городских населённых пунктов, в том числе 4 города и 2 посёлка городского типа, а также большое количество сельских населённых пунктов. Ряд подмосковных городов, посёлков городского типа и сельских населённых пунктов были включены в состав Москвы и утратили свой статус.</p>
        </div>
        <div class="list__card card">
          <img src="@/assets/mcity2.png" alt="Город" class="card__img">
          <p class="card__text">Москва — популярный туристический центр России. Московский Кремль, Красная площадь, Новодевичий монастырь и Церковь Вознесения в Коломенском входят в список объектов всемирного наследия ЮНЕСКО. Она является важнейшим транспортным узлом: город обслуживают 6 аэропортов, 10 железнодорожных вокзалов, 3 речных порта (имеется речное сообщение с морями бассейнов Атлантического и Северного Ледовитого океанов). С 1935 года в Москве работает метрополитен. Москва — спортивный центр страны. В 1980 году в Москве прошли XXII летние Олимпийские игры, а в 2018 город стал одним из хозяев чемпионата мира по футболу.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MoscowScreen',
}
</script>

<style scoped>

.headding{
  margin-bottom: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.headding__text{
  margin: 0;
  font-family: "Roboto Condensed";
  color: red;
  font-weight: bold;
  font-size: 100px;
  line-height: normal;
  margin-left: 30px;
  text-transform: uppercase;
}

.wrapper{
  max-width: 1200px;
  margin: 0 auto;
}

.box{
  border-top: 1px black solid;
}

.box__text{
  font-size: 24px;
}

.box-borderbottom{
  border-bottom: 1px solid black;
}

.card{
  display: flex;
  margin-top: 30px;
  font-size: 20px;
  justify-content: space-around;
}

.card__text{
  max-width: 500px;
}

.card__img{
  max-height: 320px;
  max-width: 550px;
}

.invis1100px{
  visibility: hidden;
  display: none;
}

@media screen and (max-width: 1100px) {
  .card{
    flex-direction: column;
    align-items: center;
    border-top: 1px solid #000;
    padding-top: 16px;
    margin-top: 10px;
  }

  .bordertop{
    border:none;
  }

  .invis1100px{
    visibility: visible;
    display: flex;
  }

  .vis1100px{
    display: none;
  }

  .box__text{
    font-size: 18px;
  }

}

@media screen and (max-width: 550px){
  .headding__text{
    font-size: 70px;
  }

  .main{
    font-size: 10px;
  }

  .card__text{
    font-size: 10px;
  }

  .card__img{
    width: 75%;
    height: 75%;
  }

  .box__text{
    font-size: 14px;
  }
}

@media screen and (max-width: 380px){
  .headding__text{
    font-size: 50px;
  }

  .headding__logo{
    width: 19%;
  }

  .box__text{
    font-size: 11px;
  }
}

</style>