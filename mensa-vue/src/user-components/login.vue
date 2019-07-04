<template>
	<div class="container" style="padding-top:50px; padding-bottom:50px;">
         <div class="col-md-12">
             <fieldset class="form-group">
                 <h3 class="border-bottom mb-4">Log in</h3>
                 <div id="div_id_email" class="form-group" style="width:40%;"> <h6 for="id_email" class="col-form-label  requiredField">
                     Email
                     <span class="asteriskField">*</span> </h6> 
                     <div class="">
                         <input type="text" name="email" autofocus="" class="textinput textInput form-control" required="" id="id_email">
                     </div>
                 </div> 
                 <div id="div_id_password" class="form-group" style="width:40%;"> <h6 for="id_password" class="col-form-label  requiredField">
                     Password
                     <span class="asteriskField">*</span> </h6>
                     <div class="">
                         <input type="password" name="password" class="textinput textInput form-control" required="" id="id_password">
                     </div>
                     <small class="text-muted">
                         <label style=" font-weight: 400;display: block;text-align: left; color: #da0833;">
                             <a href="" style="color: #da0833;">Forgot your password?</a>
                         </label>
                     </small> 
                 </div>
             </fieldset>
             <div class="form-group">
                 <input type="submit" class="genric-btn primary radius" name="submit" value="Log in">
             </div>
         </div>
         <div class="col-md-12">
             <div class="border-top pt-3">
                 <small class="text-muted">
                     Need an Account? <a class="ml-2" href="/registration/">Sign Up Now</a>
                 </small>
             </div>
         </div>
	</div>
</template>

<script>

export default {

}
</script>

<style>

</style>
