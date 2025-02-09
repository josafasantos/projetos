function converter() {
  // Pegando os valores do input e da seleção
  let valorReal = parseFloat(document.getElementById("valor").value);
  let moeda = document.getElementById("moeda").value;
  let taxaCambio = {
    usd: 5.1,
    eur: 5.5,
  };

  //Verifica se o valor é válido
  if (isNaN(valorReal) || valorReal <= 0) {
    alert("Por favor, insira um valor válido em reais.");
    return;
  }

  // Converte o valor
  let valorConvertido = valorReal / taxaCambio[moeda];

  // Atualiza a interface com o resultado formatado
  document.getElementById("resultado").textContent =
    valorConvertido.toLocaleString("pt-BR", {
      style: "currency",
      currency: moeda.toUpperCase(),
    });
}
