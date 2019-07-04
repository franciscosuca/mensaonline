<template>

    <div>
    <cheader></cheader>
    <cbanner></cbanner>
    <router-view></router-view>
    <cfooter></cfooter>
    </div>
    	
</template>

<script>
// Import child user-components
import header from './common/header.vue'
import banner from './common/banner.vue'
import footer from './common/footer.vue'

export default {
	components:{
		'cheader':header,
		'cbanner':banner,
		'cfooter':footer,
    },
}
</script>

<style>

</style>
