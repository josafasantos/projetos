// Inicializa o contador
let contador = 0;

// captura os elementos DOM
const contadorElemento = document.getElementById("contador");
const botaoAumentar = document.getElementById("aumentar");
const botaoDiminuir = document.getElementById("diminuir");

// Função para atualizar o contador da tela
function atualizarContador() {
  contadorElemento.textContent = contador;
}

// Evento de clique para aumentar
botaoAumentar.addEventListener("click", function () {
  contador++;
  atualizarContador();
});

// Evento de clique para diminuir
botaoDiminuir.addEventListener("click", function () {
  contador--;
  atualizarContador();
});
