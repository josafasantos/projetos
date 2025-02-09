function atualizarRelogio() {
  let agora = new Date(); // Obtém a data e hora atuais
  let horas = agora.getHours().toString().padStart(2, "0");
  let minutos = agora.getMinutes().toString().padStart(2, "0");
  let segundos = agora.getSeconds().toString().padStart(2, "0");

  let horarioFormatado = `${horas}:${minutos}:${segundos}`;

  document.getElementById("relogio").textContent = horarioFormatado;
}

// Atualiza o relógio a cada segundo
setInterval(atualizarRelogio, 1000);

// Chama a função imediatamente para evitar atraso inicial
atualizarRelogio();
