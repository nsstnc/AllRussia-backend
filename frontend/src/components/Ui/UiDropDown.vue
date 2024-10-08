<script setup>
import { defineProps } from 'vue'

defineProps({
	options: Array
})
</script>

<template>
	<div class="drop-down" v-if="options.length">
		<div v-for="option in options" :key="option">
			<p class="drop-down__text">{{ option }}</p>
		</div>
	</div>
</template>

<style scoped>
.drop-down {
	display: flex;
	align-items: center;
	background-color: #222222;
	flex-direction: column;
	justify-content: center;
	text-wrap: nowrap;
	row-gap: 24px;
	position: absolute;
	padding: 8px 18px;
}

.drop-down__text {
	margin: 0;
	color: white;
}
</style>
