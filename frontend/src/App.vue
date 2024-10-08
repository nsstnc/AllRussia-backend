<template>
	<div id="app">
		<HeaderDefault />
		<router-view />
		<FooterDefault />
	</div>
</template>

<script>
import HeaderDefault from './components/layouts/HeaderDefault.vue'
import FooterDefault from './components/layouts/FooterDefault.vue'
export default {
	name: 'App',
	components: {
		FooterDefault,
		HeaderDefault
	}
}
</script>

<style>
@import '@/styles/main.css';

body {
	margin: 0;
}

.wrapper {
	max-width: 1440px;
}

.main {
	margin-top: 20px;
}

.red-line {
	width: 32px;
	height: 8px;
	background-color: red;
}
</style>
