<script>
export default {
	name: 'mainTheme'
}
</script>

<template>
	<div>
		<div class="themes__bg" />
		<div class="wrapper">
			<div class="horizontal-line"></div>
			<div class="red-rectangle"></div>
			<h3>ТЕМЫ</h3>
			<div class="container">
				<div class="item item_1">
					<h2 class="theme__title">СПОРТ</h2>
					<img src="../../assets/rapper.png" alt="12" />
					<p class="item_2-subtitle">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
				</div>
				<div class="item item_2">
					<h2 class="theme__title">ТУРИЗМ</h2>
					<img src="../../assets/brige.png" alt="12" />
					<p class="item_2-subtitle">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
				</div>
				<div class="item item_3">
					<h2 class="theme__title">ПАРТНЕРЫ</h2>
					<img src="../../assets/islam.png" alt="12" />
					<p class="item_2-subtitle">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
				</div>
				<div class="item item_4">
					<h2 class="theme__title">ПРОЕКТЫ</h2>
					<img src="../../assets/september11.png" alt="12" />
					<p class="item_2-subtitle">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
					<div class="w-[345px] h-[0px] border border-[#aaaaaa] mb-2 mt-2"></div>
					<p class="item_2-list">
						Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do.
					</p>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
.container {
	margin: 0 auto;
	display: grid;
	grid-template-columns: repeat(4, 1fr);
	grid-template-rows: 357px;
	padding-bottom: 200px;
}

.themes__bg {
	width: 100%;
	height: 310px;
	background-color: black;
	position: absolute;
	z-index: -1;
	margin-top: -40px;
}

.theme__title {
	margin-top: 0;
	font-weight: bold;
	font-size: 32px;
	color: white;
}

h3 {
	margin-top: 16px;
	margin-bottom: 32px;
	font-size: 40px;
	font-weight: bold;
	color: white;
}

.horizontal-line {
	height: 0.3px;
	opacity: 1;
	width: 100%;
	background-color: white;
	margin: 0 auto;
}

.red-rectangle {
	width: 88px; /* ширина прямоугольника */
	height: 8px; /* высота прямоугольника */
	background-color: #aa0000; /* цвет фона прямоугольника */
	margin-bottom: 10px;
}
.diviver {
	height: 1px;
	width: 90%;
	margin-left: 5px;
	background-color: black;
}
.item_2-subtitle {
	font-family: 'Roboto Condensed';
	margin: 16px 0;
	font-size: 20px;
	font-weight: bold;
	width: 345px;
}
.item_2-list {
	width: 345px;
}
</style>
