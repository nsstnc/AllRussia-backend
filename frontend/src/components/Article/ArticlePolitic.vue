<template>
	<div class="article">
		<span class="red-line"></span>
		<h2 class="section-title">Политика</h2>
		<h1 class="article-title">
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
		</h1>
		<p class="byline">
			Александр Новиков | Опубликовано: 21 фев, 2024, 21:08 | Изменено: 21 фев, 2024, 22:31
		</p>
		<img src="../../assets/first.png" alt="" class="article-image" />
		<h3 class="subtitle">
			Volutpat ac tincidunt vitae semper. Felis bibendum ut tristique et egestas quis ipsum
			suspendisse.
		</h3>
		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
			labore et dolore magna aliqua. Volutpat ac tincidunt vitae semper. Felis bibendum ut tristique
			et egestas quis ipsum suspendisse. Consequat id porta nibh venenatis. Cursus euismod quis
			viverra nibh cras pulvinar mattis nunc.
		</p>
		<p>
			Rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque habitant.
			Imperdiet dui accumsan sit amet nulla facilisi morbi.
		</p>
		<p>
			Volutpat ac tincidunt vitae semper. Felis bibendum ut tristique et egestas quis ipsum
			suspendisse. Consequat id porta nibh venenatis. Cursus euismod quis viverra nibh cras pulvinar
			mattis nunc. Id aliquet lectus proin nibh. Donec massa sapien faucibus et molestie.
		</p>
		<h2>Rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque habitant.</h2>
		<p>
			Volutpat ac tincidunt vitae semper. Felis bibendum ut tristique et egestas quis ipsum
			suspendisse. Consequat id porta nibh venenatis. Cursus euismod quis viverra nibh cras pulvinar
			mattis nunc. Id aliquet lectus proin nibh. Donec massa sapien faucibus et molestie.
		</p>
		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
			labore et dolore magna aliqua. Volutpat ac tincidunt vitae semper. Felis bibendum ut tristique
			et egestas quis ipsum suspendisse. Consequat id porta nibh venenatis. Cursus euismod quis
			viverra nibh cras pulvinar mattis nunc.
		</p>
		<img src="../../assets/second.png" alt="" class="article-image" />
		<p>
			Rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque habitant.
			Imperdiet dui accumsan sit amet nulla facilisi morbi.
		</p>
		<p>
			Volutpat ac tincidunt vitae semper. Felis bibendum ut tristique et egestas quis ipsum
			suspendisse.
		</p>
		<p>
			Imperdiet dui accumsan sit amet nulla facilisi morbi. Tempor commodo ullamcorper a lacus
			vestibulum sed. Proin fermentum leo vel orci. In mollis nunc sed id semper risus in hendrerit.
		</p>
		<p>Sed ullamcorper morbi tincidunt ornare massa eget egestas purus viverra.</p>
		<h3 class="author-title">Об авторе</h3>
		<p class="author-name">Александр Новиков</p>
		<p>
			Imperdiet dui accumsan sit amet nulla facilisi morbi. Tempor commodo ullamcorper a lacus
			vestibulum sed. Proin fermentum leo vel orci. In mollis nunc sed id semper risus in
			hendrerit.Sed ullamcorper morbi...
		</p>
	</div>
</template>

<script>
export default {
	name: 'ArticlePolitic'
}
</script>

<style>
.article {
	font-family: 'Roboto';
	line-height: 1.6;
	color: #333;
	max-width: 800px;
	margin-top: 80px;
	margin-left: auto;
	margin-right: auto;
	border-top: 1px solid #000000;
}

.section-title,
.article-title,
.byline,
.subtitle,
.author-title,
.author-name {
	text-align: left;
}
.section-title {
	margin-top: 24px;
	margin-bottom: 0;
	font-family: 'Roboto Condensed';
	font-weight: normal;
	font-size: 24px;
	text-transform: uppercase;
}
.article-title {
	margin-top: 24px;
	margin-bottom: 16px;
	font-family: 'Roboto Condensed';
	color: black;
	font-size: 60px;
	line-height: normal;
}

.byline {
	color: black;
	font-size: 14px;
	margin-bottom: 20px;
}

.article-image {
	max-width: 800px;
	width: 100%;
	height: auto;
	display: block;
	margin: 0 auto;
}

.subtitle,
.author-title {
	color: #444;
	font-size: 20px;
	margin-top: 16px;
}

.author-name {
	font-weight: bold;
	margin: 8px 0;
}

p {
	font-family: 'Roboto';
	font-size: 20px;
	line-height: normal;
}
.author-title {
	margin-bottom: 0;
	font-size: 24px;
}
</style>
