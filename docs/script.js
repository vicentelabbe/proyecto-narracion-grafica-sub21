
document.addEventListener("DOMContentLoaded", function () {

  const boton = document.createElement("button");

  boton.textContent = "Explorar los minutos Sub-21";

  boton.addEventListener("click", function () {
    document.getElementById("visualizacion-02").scrollIntoView({
      behavior: "smooth"
    });
  });

  document.querySelector("header").appendChild(boton);

});
