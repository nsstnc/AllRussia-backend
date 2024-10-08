<template>
	<div>
		<div class="wrapper">
			<div class="main">
				<div class="contact">
					<div class="horizontal-line"></div>
					<span class="red-line"></span>

					<p class="contact__headding">Контакты</p>
					<p class="contact__text">
						Фактический адрес: 121170, г.Москва, Кутузовский проспект 36, стр.7Б, Метро
						"Кутузовская" или "Парк Победы"
					</p>
					<p class="contact__text">
						Адрес для корреспонденции: 121170, г.Москва, Кутузовский пр.,36,стр.7Б (Муса АЖ)
					</p>
					<p class="contact__text contact__text-underline">E-mail: info@allrussia.info</p>
					<p class="contact__text">Телефоны: +7 (495) 784-73-55; +7 (926) 393-40-64</p>
					<MapSection />
				</div>
				<div class="navigate">
					<NavigateBar />
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import MapSection from '@/components/Contact/MapSection.vue'
import NavigateBar from '@/components/layouts/NavigateBar.vue'
import { defineComponent } from 'vue'
export default defineComponent({
	components: { MapSection, NavigateBar }
})
</script>

<style class="scoped">
.wrapper {
	max-width: 1440px;
	margin: 0 auto;
}
.main {
	margin-top: 80px;
	display: flex;
	justify-content: space-between;
}
.navigate {
}

.contact {
	//border-top: 1px solid #aaaaaa;
}

.red-line {
	display: block;
	width: 80px;
	height: 13px;
	background-color: #aa0000;
}

.contact__headding {
	font-family: 'Roboto Condensed';
	font-size: 24px;
	text-transform: uppercase;
}

p {
	font-family: 'Roboto';
	font-size: 20px;
}

.contact__text:last-child {
	margin-bottom: 48px;
}
.horizontal-line {
	height: 0.5px;
	width: 1120px;
	background-color: #000;
}
</style>
