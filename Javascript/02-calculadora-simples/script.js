function calcular(operacao) {
  //Pegando os valores dos inputs
  let num1 = parseFloat(document.getElementById("num1").value);
  let num2 = parseFloat(document.getElementById("num2").value);
  let resultado = 0;

  // Verifica se os valores são números válidos
  if (isNaN(num1) || isNaN(num2)) {
    alert("Por favor, insira números válidos.");
    return;
  }

  // Realizando as operações
  switch (operacao) {
    case "+":
      resultado = num1 + num2;
      break;
    case "-":
      resultado = num1 - num2;
      break;
    case "*":
      resultado = num1 * num2;
      break;
    case "/":
      if (num2 == 0) {
        alert("Erro! Divisão por zero.");
        return;
      }
      resultado = num1 / num2;
      break;
    default:
      alert("Operação Inválida!");
  }

  // Exibir o resultado
  document.getElementById("resultado").textContent = resultado;
}
