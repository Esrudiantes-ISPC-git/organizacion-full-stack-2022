const username = document.getElementById("username-log");
const password = document.getElementById("password-log");
const form = document.getElementById("form-log");
const error = document.getElementById("error");

form.addEventListener("submit", (e) => {
  let mensaje = [];

  if (username.value.length <= 6) {
    mensaje.push("El nombre de usuario debe tener mas de 6 caracteres");
  }

  if (password.value.length <= 6) {
    mensaje.push("El password debe tener mas de 6 caracteres");
  }

  if (mensaje.length > 0) {
    e.preventDefault();
    error.innerText = mensaje.join(". ");
  }
});
