function validateForm() {
    const dobInput = document.getElementById("dob").value;
    const dobError = document.getElementById("dobError");
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    if(password !== confirmPassword) {
        alert("Passwords don't match");
        return false;
    }

    if(!dobInput) {
        dobError.textContent = "Please enter a valid date of birth";
        return false;
    }

    const dob = new Date(dobInput);
    const today = new Date();

    let age = today.getFullYear() - dob.getFullYear();
    const monthDiff = today.getMonth() - dob.getMonth();

    if(monthDiff < 0 || (monthDiff == 0 && monthDiff <= 1)) {
        age--;
    }

    if(age < 18) {
        dobError.textContent = "Please enter a valid date of birth";
        return false;
    }

    dobError.textContent = " " ;
    alert("Form validated successfully");
    return true;
}