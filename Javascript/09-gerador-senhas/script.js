function gerarSenha() {
  let tamanho = document.getElementById("tamanho").value;
  let caracteres =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+[]{}|;:,.<>?";
  let senha = "";

  for (let i = 0; i < tamanho; i++) {
    let randomIndex = Math.floor(Math.random() * caracteres.length);
    senha += caracteres[randomIndex];
  }

  document.getElementById("senha").textContent = senha;
}

function copiarSenha() {
  let senha = document.getElementById("senha").textContent;

  if (senha !== "-") {
    navigator.clipboard
      .writeText(senha)
      .then(() => {
        alert("Senha copiada para a área de transferência!");
      })
      .catch((err) => {
        console.log("Erro ao copiar senha: ", err);
      });
  } else {
    alert("Gere uma senha antes de copiar!");
  }
}
