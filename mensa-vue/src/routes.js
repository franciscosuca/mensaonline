// D1. Import the component from the user-components folder.

import menu from './user-components/menu.vue'
import index from './user-components/index.vue'
import test_api from './user-components/test_api.vue'
import AppLayout from './user-components/AppLayout.vue'
import cart from './user-components/cart.vue'
import login from './user-components/login.vue'
import singup from './user-components/singup.vue'
import logout from './user-components/logout.vue'
import settings from './user-components/settings.vue'
import contact from './user-components/contact.vue'
import about from './user-components/about.vue'
import wallet from './user-components/wallet.vue'

const routes = [
    // D2. Create the path object which will be used to call the component

    // New routes

    {
        path: '/',
        component: AppLayout,
        redirect:'index',
        children:[
            {name: 'testapi',path:'testapi', component: test_api},
            {
                name:'index',
                path:'index',
                component: index,
                default:true,
                // Use lazyloading to import the components from folders
            },
            {
                name:'menu',
                path:'menu',
                component: menu,
            },
            {
                name:'cart',
                path:'cart',
                component: cart,
            },
            {
                name:'login',
                path:'login',
                component: login,
            },
            {
                name:'singup',
                path:'singup',
                component: singup,
            },
            {
                name:'logout',
                path:'logout',
                component: logout,
            },
            {
                name:'settings',
                path:'settings',
                component: settings,
            },
            {
                name:'contact',
                path:'contact',
                component: contact,
            },
            {
                name:'about',
                path:'about',
                component: about,
            },
            {
                name:'wallet',
                path:'wallet',
                component: wallet,
            },
            
        ]
    }

    // Old routes

    // {path:'/menu', component:menu},
    // {path:'/index', component:index},
    // {path:'/', component:AppLayout},
    // {path:'/test_api', component: test_api},
    
];

// D3. Export the routes as default. This will be used when Vue start to render the DOM.
export default routes;
