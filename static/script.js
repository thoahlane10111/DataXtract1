// script.js

// Function to display a welcome message
function displayWelcomeMessage() {
    alert("Welcome to DataXtract!");
}

// Function to handle form submission
function handleSubmitForm(event) {
    event.preventDefault(); // Prevent default form submission behavior
    // Get form data
    const formData = new FormData(event.target);
    // Perform validation and further processing as needed
    // For example, you can send the form data to the server using AJAX
    console.log("Form submitted:", Object.fromEntries(formData));
}

// Event listener for DOMContentLoaded event
document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to the submit button of the form
    const form = document.querySelector('form');
    form.addEventListener('submit', handleSubmitForm);
});

