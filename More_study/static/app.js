document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById('questions-form');
    const formInput = document.querySelector('.form-input')


    form.addEventListener('submit', function(evt){
        evt.preventDefault();

        // Form validation

        const inputs = formInput.setAttribute('required');

        let valid = true;
        inputs.forEach(input => {
            console.log("form is working")
            const value = input.value.trim();

            if (value.length < 3 || value !== value.toLowerCase()) {
                    valid = false;
                    input.style.borderColor = "red";
                } else {
                    input.style.borderColor = "";
                }

        })  
        
        if (!valid) {
                alert("Please fill out all fields with at least 3 characters, all in lowercase.");
                return;
            }
    })
})