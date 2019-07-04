import axios from 'axios'

export default{
    fetchMenu (method, params, data){
        if(method === 'post'){
            return ajax('http://localhost:8000/menu/menu/', method, {data})
        }else{
            return ajax('http://localhost:8000/menu/menu/', 'get', {})
        }
    },
    fetchCoupon (method, params, data){
        if(method === 'post'){
            return ajax('http://localhost:8000/coupon/coupon/', method, {data})
        }else{
            return ajax('http://localhost:8000/coupon/coupon/', 'get', {})
        }
    },
    fetchCreditcard (method, params, data){
        if(method === 'post'){
            return ajax('http://localhost:8000/creditcard/creditcard/', method, {data})
        }else{
            return ajax('http://localhost:8000/creditcard/creditcard/', 'get', {})
        }
    },
    fetchWallet (method, params, data){
        if(method === 'post'){
            return ajax('http://localhost:8000/wallet/wallet/', method, {data})
        }else{
            return ajax('http://localhost:8000/wallet/wallet/', 'get', {})
        }
    },
    fetchOrders (method, params, data){
        if(method === 'post'){
            return ajax('http://localhost:8000/orders/orders/', method, {data})
        }else{
            return ajax('http://localhost:8000/orders/orders/', 'get', {})
        }
    },
    fetchNotes (method, params, data){
        if(method === 'post'){
            return ajax('http://localhost:8000/notes/notes/', method, {data})
        }else{
            return ajax('http://localhost:8000/notes/notes/', 'get', {})
        }
    }
}

/**
 * @param url
 * @param method
 * @param params
 * @param data
 * @returns
 */


 function ajax(url, method, options){
    if(options !== undefined){
        var {params = {}, data = {}} = options
    }else{
        params = data = {}
    }
    return new Promise((resolve, reject) =>{
        axios({
            url,
            method,
            params,
            data
        }).then(res => {
            resolve(res)
        }, res => {
            reject(res)
        })
    })
 }