const contentContainer = document.getElementById("content-container");
const loginForm = document.getElementById("login-form");
const searchForm = document.getElementById("search-form");
const baseEndpoint = "http://localhost:8000/api";
if (loginForm) {
  // handle this login form
  loginForm.addEventListener("submit", handleLogin);
}

function handleLogin(event) {
  const loginEndpoint = `${baseEndpoint}/token/`;
  let loginFormData = new FormData(loginForm);
  let loginObjectData = Object.fromEntries(loginFormData);
  console.log(loginObjectData);
  let bodyStr = JSON.stringify(loginObjectData);
  console.log(bodyStr);
  event.preventDefault();
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: bodyStr,
  };

  fetch(loginEndpoint, options)
    .then((response) => {
      return response.json;
    })
    .catch((err) => {
      console.log("err", err);
    });
}
