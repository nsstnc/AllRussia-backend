<template>
	<div>
		<div class="header">
			<div class="item item_1">
				<button class="header__btn" @click="showSideBar = !showSideBar">
					<div class="menu-icon" :class="{ open: showSideBar }">
						<span></span>
						<span></span>
						<span></span>
					</div>
				</button>
			</div>
			<div class="wrapper">
				<div class="menu__container">
					<div class="header__logo">ALLRUSSIA</div>
					<div class="vertical__line"></div>
					<div
						v-for="navItem in navMenuItems"
						:key="navItem.title"
						class="header__items"
						@click="toggleDropDown(navItem.id)"
					>
						<h3>{{ navItem.title }}</h3>
						<Transition>
							<UiDropDown :options="navItem.options" v-if="dropDown === navItem.id" />
						</Transition>
					</div>
					<div class="vertical__line"></div>
					<div class="header__items"><img class="img" src="@/assets/yarussski.png" alt="" /></div>
				</div>
			</div>
		</div>

		<div class="divider"></div>

		<HeaderHelp />
		<Transition>
			<SideBar v-if="showSideBar" @on-close.stop="showSideBar = false" />
		</Transition>
	</div>
</template>

<script setup>
import HeaderHelp from '@/components/layouts/headerHelp.vue'
import SideBar from '@/components/layouts/sideBar.vue'
import UiDropDown from '@/components/Ui/UiDropDown.vue'

import { ref } from 'vue'

const showSideBar = ref(false)

const navMenuItems = [
	{ id: 1, title: 'ВСЯРОССИЯ', options: ['О ПОРТАЛЕ', 'ПАРТНЕРЫ', 'КОНТАКТЫ', 'ПРОЕКТЫ'] },
	{
		id: 2,
		title: 'РФ',
		options: [
			'ДАЛЬНЕВОСТОЧНЫЙ',
			'ПРИВОЛЖСКИЙ',
			'ЦЕНТРАЛЬНЫЙ',
			'СЕВЕРО-ЗАПАДНЫЙ',
			'УРАЛЬСКИЙ',
			'СИБИРСКИЙ',
			'СЕВЕРО-КАВКАЗСКИЙ',
			'ЮЖНЫЙ'
		]
	},
	{ id: 3, title: 'СНГ', options: ['ВОСТОЧНАЯ ЕВРОПА', 'СРЕДНЯЯ АЗИЯ'] },
	{ id: 4, title: 'АРАБСКИЙ МИР', options: ['СЕВЕРНАЯ АФРИКА', 'БЛИЖНИЙ ВОСТОК'] },
	{ id: 5, title: 'ШКОЛА РУССКОГО ЯЗЫКА РКИ+', options: [] }
]

const dropDown = ref(null)

/** Функция переключения открытия `dropDown` */
const toggleDropDown = (id) => {
	if (dropDown.value === id) {
		dropDown.value = null
	} else {
		dropDown.value = id
	}
}
</script>

<style scoped>
.v-enter-active,
.v-leave-active {
	transition: opacity 0.2s ease-in;
}

.v-enter-from,
.v-leave-to {
	opacity: 0;
}

.header {
	display: flex;
	align-items: center;
	font-family: 'Roboto Condensed';
	font-weight: bold;
	background-color: #222222;
	color: #ffffff;
	height: 70px;
	position: fixed;
	width: 100%;
	z-index: 1000;
}

.menu__container {
	width: 1440px;
	margin: auto;
	display: flex;
	justify-content: space-evenly;
	align-items: center;
}

.vertical__line {
	border: 2px solid white;
	height: 40px;
}

.menu-icon > span {
	display: block;
	width: 35px;
	margin-bottom: 5px;
	border: 2px solid white;
	transition: all 0.3s ease-in-out;
}

.menu-icon > span:last-child {
	margin-bottom: 0;
}

.menu-icon.open span:nth-child(1) {
	transform: rotate(45deg) translate(5px, 5px);
}

.menu-icon.open span:nth-child(2) {
	opacity: 0;
}

.menu-icon.open span:nth-child(3) {
	transform: rotate(-45deg) translate(7px, -8px);
}

.header__logo {
	cursor: default;
	font-size: 36px;
}

.header__items {
	cursor: pointer;
	position: relative;
	font-size: 24px;
}

.header__list {
	display: flex;
	align-items: center;
	margin: 0 auto;
	list-style: none;
	padding: 0;
	font-size: 16px;
}

.divider {
	height: 71px; /* Толщина линии */
	background-color: #ffffff; /* Цвет линии */
}

.header__btn {
	margin-left: 40px;
	border: none;
	cursor: pointer;
	background-color: transparent;
	padding: 0;
}

.image-button img {
	width: 50px;
	height: auto;
	display: block;
}

.content {
	transition: transform 0.3s ease-out;
}
</style>
