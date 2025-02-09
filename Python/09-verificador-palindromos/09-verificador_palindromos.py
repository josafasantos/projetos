# Verificador de Palíndromos

# Solicita uma palavra ou frase ao usuário
frase = input("Digite uma palavra ou frase: ").strip().lower()

# Remove espaços e caracteres especiais
frase_formatada = "".join(caractere for caractere in frase if caractere.isalnum())

# Verifica se é um palíndromo
if frase_formatada == frase_formatada[::-1]:
    print("✅ É um palíndromo!")
else:
  print("❌ Não é um palíndromo.")