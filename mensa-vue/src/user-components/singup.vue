<template>
	<div class="container" style="padding-top:50px; padding-bottom:50px;">
        <div class="col-md-12">
            <fieldset class="form-group">
                <h3 class="border-bottom mb-4">Sing up</h3>
                <div id="div_id_userName" class="form-group"> <h6 for="id_userName" class="col-form-label  requiredField">
                    Name
                    <span class="asteriskField">*</span> </h6> 
                    <div class="">
                        <input type="text" name="userName" autofocus="" style="width:40%;" class="textinput textInput form-control" required="" id="id_userName">
                    </div>
                </div> 
                <div id="div_id_email" class="form-group"> <h6 for="id_email" class="col-form-label  requiredField">
                    Email
                    <span class="asteriskField">*</span> </h6> 
                    <div class="">
                        <input type="text" name="email" autofocus="" style="width:40%;" class="textinput textInput form-control" required="" id="id_email">
                    </div>
                </div> 
                <div id="div_id_password" class="form-group"> <h6 for="id_password" class="col-form-label  requiredField">
                    Password
                    <span class="asteriskField">*</span> </h6>
                    <div class="">
                        <input type="password" name="password" style="width:40%;" class="textinput textInput form-control" required="" id="id_password">
                    </div>
                    <small class="text-muted">
                        <label style=" font-weight: 400;display: block;text-align: left;">
                            <ul>
                                <li>- Your password can't be too similar to your other personal information.</li>
                                <li>- Your password must contain at least 8 characters.</li>
                                <li>- Your password can't be a commonly used password.</li>
                                <li>- Your password can't be entirely numeric.</li>
                            </ul>
                        </label>
                    </small> 
                </div>
                <div id="div_id_password" class="form-group"> <h6 for="id_password" class="col-form-label  requiredField">
                    Confirm your password
                    <span class="asteriskField">*</span> </h6>
                    <div class="">
                        <input type="password" name="password" style="width:40%;" class="textinput textInput form-control" required="" id="id_password">
                    </div>
                    <small class="text-muted">
                        <label style=" font-weight: 400;display: block;text-align: left;">
                            Enter the same password as before, for verification.
                        </label>
                    </small> 
                </div>
            </fieldset>
            <div class="form-group">
            <input type="submit" class="genric-btn primary radius" name="submit" value="Sing up">
        </div>
        </div>
        <div class="col-md-12">
            <div class="border-top pt-3" style="align-self:center;">
                <small class="text-muted">
                    Already Have an Account? <a class="ml-2" href="/registration/">Log in</a>
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