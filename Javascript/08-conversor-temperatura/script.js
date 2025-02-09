function converter() {
  let temperatura = parseFloat(document.getElementById("temperatura").value);
  let tipo = document.getElementById("tipo").value;
  let resultado = 0;

  //verifica se o valor é valido
  if (isNaN(temperatura)) {
    alert("Por favor, insira uma temperatura válida.");
    return;
  }

  //Conversão de Celsius para Fahrenheit ou vice e versa
  if (tipo === "celsius") {
    resultado = (temperatura - 32) * (5 / 9);
    document.getElementById("resultado").textContent =
      resultado.toFixed(2) + "°C";
  } else {
    resultado = (temperatura * 9) / 5 + 32;
    document.getElementById("resultado").textContent =
      resultado.toFixed(2) + "°F";
  }
}
