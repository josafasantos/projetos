let segundos = 0;
let minutos = 0;
let horas = 0;
let intervalo;

function atualizarTempo() {
  segundos++;

  if (segundos === 60) {
    segundos = 0;
    minutos++;
  }
  if (minutos === 60) {
    minutos = 0;
    horas++;
  }

  // Formatar a saida com dois dígitos
  let formatoTempo =
    (horas < 10 ? "0" + horas : horas) +
    ":" +
    (minutos, 10 ? "0" + minutos : minutos) +
    ":" +
    (segundos < 10 ? "0" + segundos : segundos);

  document.getElementById("tempo").textContent = formatoTempo;
}

document.getElementById("start").addEventListener("click", function () {
  if (!intervalo) {
    intervalo = setInterval(atualizarTempo, 1000);
  }
});

document.getElementById("pause").addEventListener("click", function () {
  clearInterval(intervalo);
  intervalo = null;
});

document.getElementById("reset").addEventListener("click", function () {
  clearInterval(intervalo);
  intervalo = null;
  segundos = 0;
  minutos = 0;
  horas = 0;
  document.getElementById("tempo").textContent = "00:00:00";
});
