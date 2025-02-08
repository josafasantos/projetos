# Contador de Vogais em um Frase

# Solicita uma frase ao usuário
# Converte para minúsculas para facilitar a comparação
frase = input("Digite uma frase: ").strip().lower() 

# Define as vogais
vogais = "aeiou"

# Inicializa o contador de vogais
contador = 0

# Percore cada caractere da frase
for letra in frase:
  if letra in vogais:
    contador += 1

# Exibe o resultado
print(f"A frase digitada contém {contador} vogais.")