// form.js

// Function to submit the form
function submitForm() {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;

  var userData = {
    name: name,
    email: email,
  };

  // Send a POST request using Axios
  axios
    .post("/add_user", userData, {
      headers: {
        "Content-Type": "application/json", // This should be application/json
      },
    })
    .then(function (response) {
      // Assuming the response contains the ID of the new user
      let newUser = response.data.user;
      let table = document.querySelector(".table tbody");
      let row = table.insertRow();
      let cellId = row.insertCell(0);
      let cellName = row.insertCell(1);
      let cellEmail = row.insertCell(2);
      cellId.textContent = newUser.id;
      cellName.textContent = newUser.name;
      cellEmail.textContent = newUser.email;
      // Refresh the page to show the new user with styles
      location.reload();
    })
    .catch(function (error) {
      // Handle any errors here
      console.error(error);
    });
}

// Attach the submitForm function to the form submit event
document
  .getElementById("userForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission
    submitForm(); // Call the submitForm function to handle the submission
  });
