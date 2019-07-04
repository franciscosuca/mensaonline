<template>
    <div class="whole-wrap">
	    <div class ="container" style="padding-top:50px; padding-bottom:50px;">
            <h3 class="border-bottom mb-4" >Personal Information</h3>
            <div class="col-lg-8 col-md-8">
                <form  style="padding-top:25px;">
                    <div class="row form-group mb-4">
                        <div class="col-md-12"><h4>Name</h4></div>
                        <div class="col-md-12 mb-3 mb-md-0">
                            <input type="text" class="form-control" id="fullname" value="Francisco">
                        </div>
                    </div>

                    <div class="row form-group mb-4">
                        <div class="col-md-12"><h4>Email Address</h4></div>
                        <div class="col-md-12 mb-3 mb-md-0">
                            <input type="text" class="form-control" value="email@example.com ">
                        </div>
                    </div>
            
                    <div class="row form-group mb-4">
                        <div class="col-md-12"><h4>Mobile Number</h4></div>
                        <div class="col-md-12 mb-3 mb-md-0">
                            <input type="text" class="form-control" value="+7348714097">
                        </div>
                    </div>
            
                    <div class="row form-group">
                        <div class="col-md-12"><h4>Address</h4></div>
                        <div class="col-md-12 mb-3 mb-md-0">
                            <textarea name="" class="form-control" id="" cols="30" rows="5">Friedrich-Heinrich-Allee 25, 47475 Kamp-Lintfort</textarea>
                        </div>
                    </div>
            
                    <div class="row form-group">
                        <div class="col-md-12">
                            <input type="submit" value="Update Profile" class="genric-btn primary radius">
                        </div>
                    </div>
                </form>
            </div>
        </div>
	</div>   
</template>

<script>

export default {
	

}
</script>

<style>
.title{
    color:black;
    font-size: 200%;
}
</style>
