function gerarCorAleatoria() {
  // Gera uma cor hexadecimal aleatória
  let cor = "#" + Math.floor(Math.random() * 16777215).toString(16);

  // Atualiza a cor de fundo da página
  document.body.style.backgroundColor = cor;

  //Exibe a cor atual na tela
  document.getElementById("cor").textContent = cor;
}

// Adiciona o evento de clique ao botão
document.getElementById("botao").addEventListener("click", gerarCorAleatoria);
