<script>
import axios from 'axios'
export default {
	name: 'HeaderHelp',
	data() {
		return {
			loading: true,
			rates: {},
			filteredRates: {},
			apiUrl:
				'https://openexchangerates.org/api/latest.json?app_id=b32cd1fe2c5548c78b31cdd514660010', // замените на свой URL API
			currenciesOfInterest: ['USD', 'EUR', 'CNY', 'BYN'],
			difference: Math.random()
		}
	},
	mounted() {
		this.fetchData()
	},
	methods: {
		fetchData() {
			axios
				.get(this.apiUrl, {
					params: {
						// base: 'EUR'
					}
				})
				.then((response) => {
					this.rates = response.data.rates
					this.filterRates()
					this.loading = false
				})
				.catch((error) => {
					console.error('Ошибка при получении данных:', error)
					this.loading = false
				})
		},

		filterRates() {
			this.filteredRates = {}
			for (const currency of this.currenciesOfInterest) {
				if (Object.prototype.hasOwnProperty.call(this.rates, currency)) {
					this.filteredRates[currency] = this.rates[currency]
				}
			}
		}
	}
}
</script>

<template>
	<div class="header__help">
		<ul
			class="wrapper header__help__container"
			v-for="(rate, currency) in filteredRates"
			:key="currency"
		>
			<li class="header_item">
				{{ currency }} {{ rate }}
				<span class="item_acc"
					>{{ this.difference.toFixed(2) }}<img src="@/assets/Arrow%201(1).png"
				/></span>
			</li>
		</ul>
	</div>
</template>

<style scoped>
.header__help {
	display: flex;
	justify-content: space-between;
	background-color: #222222;
}
.header__help__container {
	display: flex;
	align-items: center;
	padding: 0;
	margin: 0 auto;
	list-style: none;
	height: 50px;
}
.header__help__container > li {
	font-family: 'Roboto Condensed';
	font-weight: bold;
	font-size: 20px;
}
.header_item {
	font-size: 14px;
	color: #ffffff;
}
.item_dang {
	padding-left: 8px;
	color: #ff3f3f;
}
.item_acc {
	padding-left: 8px;
	color: #4bff68;
}

img {
	width: 10px;
	height: 15px;
}
</style>
