<template>
    <div>
        <footer class="footer">
          <div class="footer__wrapper wrapper">
            <h2 class="footer__logo logo">
              ALLRUSSIA
            </h2>
            <div class="footer__list list">
              <div class="list__contact contact line-top">
                <p class=" contact__text line-bottom">Связаться с нами</p>
                <p class="contact__text margin-top">allrussia.info@allrussia.info</p>
                <p class="contact__text m0">info@allrussia.info</p>
              </div>
              <div class="list__social social line-top">
                <p class="social__text line-bottom">Социальные сети</p>
                <a class="social__text social__text-margin" src="/">Telegram</a>
                <a class="social__text social__text-margin" src="/">YouTube</a>
                <a class="social__text social__text-margin" src="/">Facebook* RU</a>
                <a class="social__text social__text-margin" src="/">Facebook* AR</a>
                <a class="social__text social__text-margin" src="/">Livejournal</a>
              </div>
            </div>
            <div class="footer__bottom bottom line-top">
              <p class="bottom__text">Свидетельство о регистрации средства массовой информации Эл № ФС77-66038 от 20 июня 2016г</p>
              <p class="bottom__text">Все права защищены. Портал «Вся Россия»</p>
            </div>
          </div>
        </footer>
    </div>
</template>

<script>
export default {
  name: 'FooterSide',
}
</script>

<style scoped>

.wrapper{
  max-width: 1440px;
  margin: 0 auto;
}

p {
  font-size: 14px;
}

a {
  font-size: 14px;
}

.footer{
  font-family: "Roboto", sans-serif;
  margin-top: 40px;
  background-color: #222222;
  color: white;
  padding-top: 29px;
}

.bottom__text {
  margin-top: 8px;
  margin-bottom: 2px;
  opacity: 0.75;
}

.bottom__text:last-child {
  margin: 0;
  margin-bottom: 16px;
}

.logo {
  font-size: 64px;
  margin: 0;
  margin-left: 40px;
}

.footer__wrapper{
  display: flex;
  flex-direction: column;
}

.footer__list{
  display: flex;
  flex-direction: row;
  gap: 26px;
  margin-top: 36px;
}

.list__contact{
  width: 500px;
}

.line-top{
  border-top: 1px solid white;
}

.list__social{
  width: 100%;
}

.line-bottom{
  border-bottom: 1px solid white;
  width: 100%;
  padding-bottom: 16px;
}

.m0{
  margin-top: 0;
}

.contact__text{
  margin-bottom: 0;
}

.footer__bottom{
  margin-top: 9px;
}

.social__text-margin{
  margin-left: 64px;
}

.social__text-margin:first-of-type{
  margin: 0;
}
</style>