<template>
    <div>
		<section class="menu-area section-gap" id="menu">
			<div class="container">
				<div class="row d-flex justify-content-center">
					<div class="menu-content pb-70 col-lg-8">
						<div class="title text-center">
							<h1 class="mb-10">What kind of Foods we serve for you</h1>
						</div>
					</div>
				</div>	
				<ul class="filter-wrap filters col-lg-12 no-padding">
					<li
						v-for="foodCategory in foodCategories"
						v-on:click="filter=foodCategory"
						:class="{active: foodCategory == filter}"
						:key="foodCategory.id"
					>
						{{foodCategory}}
					</li>
				</ul>
				<div class="row grid autoHeight">
					<div 
						class="col-md-6 all Veg" 
						v-for="(menu, index) in menus" 
						:key="index"
						track-by="$index" 
						v-if="menu.category == filter || filter == 'All Menu'"
					>
						<div class="single-menu">
							<div class="title-wrap d-flex justify-content-between">
								<h4>{{menu.title}}</h4>
								<h4 class="price">${{menu.price_guest}}</h4>
							</div>
							<p>{{menu.description}}</p>
							<br>
							<h5>Calories <b>{{menu.calories}}</b></h5>
							<br>
							<div class="meta-bottom d-flex justify-content-between">
								<div>
								</div>
								<div  style="align-self:right;">
									<p class="genric-btn primary circle text-uppercase" v-on:click="triggerFunction(menu.id,menu.title,menu.description,menu.price_guest,menu.calories)">add to cart</p>
								</div>
							</div>
						</div>					                               
					</div>		
				</div>
			</div>
		</section>
    </div>
</template>

<script>
import api from './api/index.js';

export default {
    data () {
		return {

			menus: [],
			foodKey:"foodCategory",
			foodCategories:["All Menu","Veg","Non-Veg","Salads","Fruits","Desserts","Beverages","Favorites"],
			filter: "All Menu",
		}
  },
	computed:{
		
	},
	methods:{
		// Vuex
		triggerFunction: function(id,title,description,price,calories){
			this.$store.dispatch('triggerFunction', {
				id: id,
				title: title,
				description: description,
				price: price,
				calories: calories
			})
		},
		// Method to call data from Django
		fetchAllMenu(){
			api.fetchMenu('get',null,null).then(res => {
				this.menus = res.data
				// Showing menu from console
				console.log(this.menus)
			}).catch((e) => {
				console.log(e)
			})
		},
	},
	mounted(){
		// fetch all menus once component is mounted
		this.fetchAllMenu()
	},

}
</script>

<style>
.autoHeight{
	height: auto !important;
}
</style>
