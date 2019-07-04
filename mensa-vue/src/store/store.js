import Vue from 'vue'
import Vuex from 'vuex'
import api from '../user-components/api/index';

Vue.use(Vuex);

export const store = new Vuex.Store({
    state:{
        order:{id:0,title:'',description:'',price:0,calories:0,qty:0},
        orders:[],
        order_total:0,
        balance:'',
        
    },
    getters:{
        countOrders: state => {
			return state.orders.length
        },  
        // Under construction
        checkBalance: state => {
            // return state.balance
            // return Vue.set(state.balance);
        }      
    },
    mutations:{
        cleanOrders: state => {
			while(state.orders.length){
				state.orders.pop()
            }
            return state.order_total = 0
        },
        triggerFunction: (state,payload) => {
            // Vue.set( target, propertyName/index, value )
            Vue.set(state.order, 'id', payload.id);
            Vue.set(state.order, 'title', payload.title);
            Vue.set(state.order, 'description', payload.description);
            Vue.set(state.order, 'price', payload.price);
            Vue.set(state.order, 'calories', payload.calories);
            Vue.set(state.order, 'qty', 1);
            state.orders.push({...state.order});
        },
    },
    actions:{
        cleanOrders: context => {
            context.commit('cleanOrders')
        },
        triggerFunction: (context,payload) => {
            context.commit('triggerFunction',payload)
        },
    },
})