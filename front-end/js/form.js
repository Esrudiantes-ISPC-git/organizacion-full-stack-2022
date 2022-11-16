const nombre = document.getElementById("nombre");
const username = document.getElementById("username");
const password = document.getElementById("password");
const form = document.getElementById("form");
const error = document.getElementById("error");

form.addEventListener("submit", (e) => {
  let mensaje = [];
  const regExText = new RegExp("^[A-Z]+$", "i");

  if (nombre.value.length <= 3) {
    mensaje.push("El nombre debe tener mas de 3 caracteres");
  }

  if (!regExText.test(nombre.value)) {
    mensaje.push("El nombre debe estar compuesto solo por letras");
  }

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
