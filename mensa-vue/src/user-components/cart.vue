<template>
    <div class="whole-wrap">
		<div class ="container">
			<div class="section-top-border"> 
				<h3 class="mb-30">Order Summary</h3>
				<div class="progress-table-wrap">
					<div class="progress-table">
						<div class="table-head" >
							<div class="visit" style="padding-left: 10px;">Meal</div>
							<div class="country">Description</div>
							<div class="serial">Price</div>
							<div class="serial">Calories</div>
							<div class="serial">Quantity</div>
							<div class="serial">Total</div>
						</div>
						<div class="table-row" v-for="(order, index) in orders" track-by="$index" :key="index">
							<div class="visit" style="padding-left: 10px;">{{order.title}}</div>
							<div class="country">{{order.description}}</div>
							<div class="serial">{{order.price}}</div>
							<div class="serial">{{order.calories}}</div>
							<div class="serial">{{order.qty}}</div>
							<div class="serial">{{order.price}}</div>
						</div>
					</div>
				</div>
			</div>
			<div class="section-top-border"> 
				<h3 class="mb-30">Checkout</h3>
				<div class="progress-table-wrap">
					<div class="progress-table">
						<div class="table-head" >
							<div class="country" style="padding-left: 10px;">Order quantity</div>
							<div class="country">Price of total order</div>
							<div class="country">Actual balance</div>
						</div>
						<div class="table-row">
							<div class="country" style="padding-left: 10px;">{{countOrders}}</div>
							<div class="country" style="self-align:center">{{formatPrice(order_total)}}</div>
							<div class="country">{{formatPrice(balance)}}</div>
						</div>
					</div>
				</div>
			</div>
			<div class="section-top-border">
				<div class="meta-bottom d-flex justify-content-between">
					<div>
						<p class="genric-btn primary circle text-uppercase" v-on:click="cleanOrders">Clean orders</p>
					</div>
					<div  style="align-self:right;">
						<p class="genric-btn primary circle text-uppercase" v-on:click="checkout">Continue to checkout</p>				
					</div>
				</div>
				<p>{{msg}}</p>
			</div>
		</div>
	</div>
</template>

<script>
import {mapState, mapGetters, mapMutations, mapActions} from 'vuex'
import api from './api/index.js'

export default {
	data(){
		return{
			formWallet:{
                wallet_number: "64283470177",
                balance: 0,
                customer: 1
			},
			temp:0,
			customOrder:{
				customer: 1,
				menu: []
			},
			msg:'',
			msg_orderStatus:'',
			msg_creditUpdated:'',
		}
	},
	computed:{
		...mapState([
			'orders',
			'balance',
			'order_total',
		]),
		...mapGetters([
			'countOrders',
		]),
	},
  	methods:{	
		...mapActions([
			'cleanOrders'
		]),
		// ######################## Checkout ########################
		checkout:function(){
			if(this.$store.getters.countOrders){
			this.$store.state.orders.forEach(element => {
				this.$store.state.order_total = parseFloat(this.$store.state.order_total) + parseFloat(element.price)
				this.$store.state.balance = this.$store.state.balance - parseFloat(this.$store.state.order_total)
				// New balance for the wallet
				this.formWallet.balance = this.$store.state.balance
				// Savings orders into the order array while in the loop
				this.customOrder.menu.push(element.id) 
				if(this.$store.state.balance<0){
					// code to use the previous balance
					this.temp = 1
					alert("You don't have enough balance."+"\nPlease Recharge")
				}
			});
			if (this.temp == 0){
				alert("Purchase complete")
				// Update balance
				api.fetchWallet('post',null, this.formWallet).then(res => {
                        this.msg_creditUpdated = 'Credit added.'
                    }).catch((e) => {
                        this.msg_creditUpdated = e.response
                        console.log(e)
					},)
				// Order submission
				api.fetchOrders('post',null, this.customOrder).then(res => {
					this.msg_orderStatus = 'Order Submited'
				}).catch((e) => {
					this.msg_orderStatus = e.response
					console.log(e)
				},)
			}
			}else{
				alert('Select a meal from the menu before checkout.')
			}	
		},
		// ######################## Wallet ########################
		fetchWallet(){
			api.fetchWallet('get',null,null).then(res => {
                this.wallets = res.data
                this.wallets.forEach(wallet => {
                    this.$store.state.balance = wallet.balance
            })
			}).catch((e) => {
				console.log(e)
			})
        },
		// ######################## Others ########################
		formatPrice(value) {
            let val = (value/1).toFixed(2).replace('.', '.')
            return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
		},
	  },
	  	mounted(){
			// fetch all notes once component is mounted
			this.fetchWallet()
		}
}
</script>

<style>
</style>
