<template>
    <div class="whole-wrap">       
		<div class="container section-top-border" style="padding-left:100px; padding-right:100px;">
            <div class="row">
            <div class="col-md-6 col-sm-10 section-top-border">
                <h1 class="typo-list">Wallet</h1>
                <div style="padding-top:10px;">
                    <h3 class="mb-20">Balance</h3>
                    <p style="font-size:40px;" v-on:click="fetchWallet">$ {{formatPrice(balance)}}</p>
                    <p>Click your balance to update it.</p>

                    <!-- <p>{{msg}}</p> -->

                </div>
            </div>
            <div class="col-md-6 col-sm-10 section-top-border">
				<h1 class="typo-list">Recharge methods</h1>
                <br>
                <div class="row">
                    <div class="col-md-6 col-sm-6" style="align:center;">
                        <h2>Credit Card</h2>
                        <br>
                        <form>
                            <div class="mt-10 col-md-12" style="padding-top:5px;">
                                <h5 style="padding-bottom:5px;">Recharge amount</h5>
                                <input type="text" name="regarche" placeholder="Ex. 10" required class="single-input" v-model="formWallet.balance">
                            </div>
                            <div class="mt-10 col-md-12" style="padding-top:5px;">
                                <h5 style="padding-bottom:5px;">Card number</h5>
                                <input type="text" name="cc_number" placeholder="Ex. 1111 2222 3333 4444" required class="single-input" v-model="insertedCard.number">
                            </div>
                            <div class="mt-10 col-md-12" style="padding-top:5px;">
                                <h5 style="padding-bottom:5px;">Name on card</h5>
                                <input type="text" name="cc_name" placeholder="Ex. Francisco Susana" required class="single-input" v-model="insertedCard.name">
                            </div>
                            <div class="mt-10 col-md-12" style="padding-top:5px;">
                                <h5 style="padding-bottom:5px;">Expiry date</h5>
                                <input type="text" name="cc_valid_date" placeholder="Ex. 12/22" required class="single-input" v-model="insertedCard.valid_date">
                            </div>
                            <div class="mt-10 col-md-12" style="padding-top:5px;">
                                <h5 style="padding-bottom:5px;">Security code</h5>
                                <input type="text" name="cc_code" placeholder="Ex. 123" required class="single-input" v-model="insertedCard.code">
                            </div>
                        </form>
                        <br>
                        <p class="genric-btn info radius text-uppercase col-md-12" v-on:click="submitCreditcard">Submit</p> 
                    </div>
                    <div class="col-md-6 col-sm-6">
                        <h2>Coupon</h2>
                        <br>
                        <form>
                            <div class="mt-10 col-md-12" style="padding-top:5px;">
                                <h5 style="padding-bottom:5px;">Enter the 10 digits from the coupon</h5>
                                {{this.coupons.number}}
                                <input type="number" name="coupon_number" placeholder="Ex. 1234567890" required class="single-input" v-model="insertedCoupon">
                            </div>
                        </form>
                        <br>
                        <p class="genric-btn info radius text-uppercase col-md-12" v-on:click="submitCoupon">Confirm</p> 
                    </div>
                </div>
		    </div>
            </div>
		</div>
	</div>
</template>

<script>
import api from './api/index.js';
import { mapState, mapActions, mapGetters } from 'vuex';

export default {
    data(){
        return{

            coupons:[],
            creditcards:[],
            msg:'',
            bal:0,

            insertedCoupon:'',
            insertedCard:{
                name:'',
                number:'',
                valid_date:'',
                code:'',
            },
            formWallet:{
                wallet_number: "64283470177",
                balance: 0,
                customer: 1
            },
        }
    },
    methods:{
        // ######################## Coupon ########################
        submitCoupon(){
            this.coupons.forEach(coupon => {
                console.log(coupon.number) 
                if(coupon.number == this.insertedCoupon){
                    alert('Coupon confirmed!'+"\n"+"You've got 10 credits extra")
                    this.insertedCoupon = ''
                    this.formWallet.balance = parseFloat(this.$store.state.balance) + parseFloat(10)
                    console.log(this.formWallet.balance)
                    api.fetchWallet('post',null, this.formWallet).then(res => {
                        this.msg = 'Credit added.'
                        console.log(this.formWallet)
                    }).catch((e) => {
                        this.msg = e.response
                        console.log(e)
                    },)
                }else{
                    alert('Coupon invalid!') 
                }
            });
        },
        fetchCoupon(){
			api.fetchCoupon('get',null,null).then(res => {
                this.coupons = res.data
                // console.log(this.coupons)
			}).catch((e) => {
				console.log(e)
			})
        },
        // ######################## Credit card ########################
        submitCreditcard(){
            this.creditcards.forEach(creditcard => {
               console.log(creditcard.cc_number,creditcard.cc_name,creditcard.cc_valid_date,creditcard.cc_code)       
               if(creditcard.cc_number == this.insertedCard.number && creditcard.cc_name == this.insertedCard.name && creditcard.cc_valid_date == this.insertedCard.valid_date && creditcard.cc_code == this.insertedCard.code){
                   alert('Credit submitted!') 
                   this.insertedCard = ''
                    this.formWallet.balance = parseFloat(this.$store.state.balance) + parseFloat(this.formWallet.balance)
                    console.log(this.formWallet.balance)
                    api.fetchWallet('post',null, this.formWallet).then(res => {
                        this.msg = 'Credit added.'
                        console.log(this.formWallet)
                    }).catch((e) => {
                        this.msg = e.response
                        console.log(e)
                    },)
               }else{
                  alert('Credit card is not valid!') 
               }
            });
        },
        fetchCreditcard(){
			api.fetchCreditcard('get',null,null).then(res => {
                this.creditcards = res.data
                // console.log(this.creditcards)
			}).catch((e) => {
				console.log(e)
			})
        },
        // ######################## Wallet ########################
        fetchWallet(){
			api.fetchWallet('get',null,null).then(res => {
                this.wallets = res.data
                // console.log(this.wallets)
                this.wallets.forEach(wallet => {
                    this.$store.state.balance = wallet.balance
            })
			}).catch((e) => {
				console.log(e)
			})
        },
        submitWallet(){
            api.fetchWallet('post',null, this.formWallet).then(res => {
                this.msg = 'Credit added.'
                console.log(this.formWallet)
            }).catch((e) => {
                this.msg = e.response
                console.log(e)
            },)
        },
        // ######################## Ohters ########################
        formatPrice(value) {
            let val = (value/1).toFixed(2).replace('.', '.')
            return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
        }
        
    },
    computed:{
        ...mapState([
            'balance',
            
        ]),
    },
    mounted(){
        this.fetchCoupon()
        this.fetchCreditcard()
        this.fetchWallet()

    },
}
</script>

<style>

.align-items-center {
    align-items: center !important;
    justify-content: center !important;
}
</style>
