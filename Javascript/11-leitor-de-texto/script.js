// Variáveis globais para controle da leitura
let currentUtterance = null;
let words = [];
let currentWordIndex = 0;
// Aproximação: 25 palavras correspondem a cerca de 10 segundos (ajuste conforme necessário)
const palavrasPor10seg = 25;

// Função para iniciar a leitura a partir do índice atual
function speakFromCurrentIndex() {
  if (currentWordIndex >= words.length) return;
  // Junta as palavras restantes em uma string
  const textToSpeak = words.slice(currentWordIndex).join(" ");
  const utterance = new SpeechSynthesisUtterance(textToSpeak);
  currentUtterance = utterance;

  // Atualiza o índice a cada palavra pronunciada
  utterance.onboundary = function (event) {
    if (event.name === "word") {
      currentWordIndex++;
    }
  };

  // Ao terminar, limpa o objeto atual
  utterance.onend = function () {
    currentUtterance = null;
  };

  speechSynthesis.speak(utterance);
}

// Inicia a leitura do início do texto
function startReading() {
  speechSynthesis.cancel();
  currentUtterance = null;
  const textInput = document.getElementById("text").value;
  // Divide o texto em palavras, removendo espaços em branco extras
  words = textInput.split(/\s+/).filter(Boolean);
  currentWordIndex = 0;
  speakFromCurrentIndex();
}

// Para a leitura
function stopReading() {
  speechSynthesis.cancel();
  currentUtterance = null;
}

// Pausa a leitura
function pauseReading() {
  speechSynthesis.pause();
}

// Retoma a leitura pausada
function resumeReading() {
  speechSynthesis.resume();
}

// Avança aproximadamente 10 segundos (25 palavras)
function skipForward() {
  speechSynthesis.cancel();
  currentUtterance = null;
  currentWordIndex += palavrasPor10seg;
  if (currentWordIndex > words.length) {
    currentWordIndex = words.length;
  }
  speakFromCurrentIndex();
}

// Retrocede aproximadamente 10 segundos (25 palavras)
function skipBackward() {
  speechSynthesis.cancel();
  currentUtterance = null;
  currentWordIndex -= palavrasPor10seg;
  if (currentWordIndex < 0) {
    currentWordIndex = 0;
  }
  speakFromCurrentIndex();
}
