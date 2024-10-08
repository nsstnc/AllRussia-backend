<script>
export default {
	name: 'mainSection'
}
</script>

<template>
	<div class="main__section">
		<div class="main__container">
			<h1 class="main__title">ALLRUSSIA</h1>
			<p class="main__subtitle">Мы открываем Россию заново! Вместе с вами!</p>
		</div>
	</div>
</template>

<style scoped>
.main__section {
	display: flex;
	justify-content: center;
	align-items: center;
	width: 100%;
	height: 685px;
	background-image: url('@/assets/main.png');
	background-size: cover;
	background-position: center;
}

.main__title {
	font-family: 'Roboto Condensed';
	font-weight: bold;
	text-align: center;
	color: #ffffff;
	font-size: 200px;
	line-height: 0;
}

.main__subtitle {
	font-family: 'Roboto Condensed';
	font-weight: bold;
	text-align: center;
	color: #ffffff;
	font-size: 36px;
	line-height: 0;
}
</style>
