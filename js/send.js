
function sendMail(signupForm) {
    emailjs.send("sign_up", "sign_up", {
        "from_name": signupForm.name.value,
        "from_email": signupForm.emailaddress.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;
}