<template>
    <div>
        <div class="wrapper">
            <span class="red-line"></span>
            <div class="navigation">
                <div class="navigation__title title">
                    <p class="title__text">ALLRUSSIA</p>
                </div>
                <nav class="navigation__bar bar">
                    <ul class="bar__list list">
                        <li class="list__item">
                            <router-link class="list__link" to="/about">О портале</router-link>
                        </li>
                        <li class="list__item">
                            <router-link class="list__link" to="/partner">Партнеры</router-link>
                        </li>
                        <li class="list__item">
                            <router-link class="list__link" to="/contact">Контакты</router-link>
                        </li>
                        <li class="list__item">
                            <router-link class="list__link" to="/">Проекты</router-link>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        
    </div>
</template>

<script>
export default {
  name: 'NavigationBar',
}
</script>

<style scoped>

.navigation{
    border-top: black 1px solid;
    max-width: 288px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

li{
    list-style-type:none;
}

ul{
    padding: 0;
    margin: 0;
}

.navigation__bar{
    width: 100%;
}

.list__item{
    margin-top: 32px;
    border-top: black 1px solid;
    display: flex;
    justify-content: center;
    padding-top: 16px;
}

.list__item:first-child{
    margin-top: 0;
}

.title__text{
    font-size: 36px;
    font-weight: bold;
}

.list__link{
    font-size: 24px;
    color: black;
    text-decoration: none;
}

.list__link:hover{
    color: #AA0000;
}

.red-line{
    width: 32px;
    height: 8px;
    background-color: red;
    position: absolute;
    margin-top: 1px;
}
</style>