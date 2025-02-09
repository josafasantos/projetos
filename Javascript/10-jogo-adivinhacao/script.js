// Gera um número aleatório entre 1 e 100
let numeroAleatorio = Math.floor(Math.random() * 100) + 1;
let tentativas = 0;

function verificarNumero() {
  let tentativa = parseInt(document.getElementById("tentativa").value);
  let mensagem = document.getElementById("mensagem");

  //verifica se o input é valido
  if (isNaN(tentativa) || tentativa < 1 || tentativa > 100) {
    mensagem.textContent = "Por favor, insira um número entre 1 e 100";
    mensagem.style.color = "red";
    return;
  }

  tentativas++;

  if (tentativa === numeroAleatorio) {
    mensagem.textContent = `Parabéns! Você acertou em ${tentativas} tentativas.`;
    mensagem.style.color = "green";
  } else if (tentativa < numeroAleatorio) {
    mensagem.textContent = "Tente um número maior!";
    mensagem.style.color = "blue";
  } else {
    mensagem.textContent = "Tente um número menor!";
    mensagem.style.color = "blue";
  }
}

function reiniciarJogo() {
  numeroAleatorio = Math.floor(Math.random() * 100) + 1;
  tentativas = 0;
  document.getElementById("tentativa").value = "";
  document.getElementById("mensagem").textContent = "";
}
