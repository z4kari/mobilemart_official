function signUp(){
    username = document.getElementById('name').value
    var p1 = document.getElementById('p1')
    useremail = document.getElementById('email').value
    var p2 = document.getElementById('p2')

    phone = document.getElementById('phone').value
    var p3 = document.getElementById('p3')

    password = document.getElementById('pswd').value
    var p4 = document.getElementById('p4')

    confirmPassword = document.getElementById('cpswd').value
    var p5 = document.getElementById('p5')

    var email_pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    var number_pattern = /^[789]\d{9}$/
    var username_pattern = /^[a-zA-Z\-]+$/

    if (username == "") {

        p1.innerHTML = 'enter your name'
        return false
    }

    if (useremail == "") {
        
        p2.innerHTML = 'Email Field Should not be Empty'

        return false
    }

    if (useremail.match(email_pattern) == null) {
       
        p2.innerHTML = 'Email Is Invalid'

        return false
    }

    if (phone == "") {
       
       p3.innerHTML = 'Phone Field Should Not be Empty'

        return false
    }
    if (phone.match(number_pattern) == null) {
       
       p3.innerHTML = 'Not a Valid Number'

        return false
    }
    
    if(password == ""){
     
       p4.innerHTML = 'Enter a Password'

        return false
    }

    if(password.length<3){
        
        p4.innerHTML = 'Enter at least 3 Charecters'
        return false
    }
    // if(password.match(username_pattern) == null){
    //     p4.innerHTML = 'enter a stromg password'
    //     return false
    // }

    if(confirmPassword ==""){
        
        p5.innerHTML = 'Enter Password'

        return false
    }

    if(confirmPassword != password){
    
        p5.innerHTML = 'Password Does not Match'
        return false
    }
}