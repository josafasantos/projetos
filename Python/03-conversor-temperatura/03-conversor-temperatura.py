# Conversor de Temperatura

# Exibe ooções para o usuário

print("Escolha a conversão: ")
print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
print("3 - Fahrenheit para Celsius")
print("4 - Fahrenheit para Kelvin")
print("5 - Kelvin para Celsius")
print("6 - Kelvin para Fahrenheit")

# Recebe a opção do usuário
opcao = int(input("Digite o número da opção desejada: "))

# Solicita a temperatura inicial
temperatura = float(input("Digite a temperatura: "))

# Realiza a conversão com base na opção escolhida
if opcao == 1:
  resultado = (temperatura * 9/5) + 32
  print(f"{temperatura}°C é igual a {resultado:.2f}°F")
elif opcao == 2:
  resultado = temperatura + 273.15
  print(f"{temperatura}°C é igual a {resultado:.2f}°K")
elif opcao == 3:
  resultado = (temperatura - 32) * 5/9
  print(f"{temperatura}°F é igual a {resultado:.2f}°C")
elif opcao == 4:
  resultado =  (temperatura - 32) * 5/9 + 273.15
  print(f"{temperatura}°F é igual a {resultado:.2f}°K")
elif opcao == 5:
  resultado = temperatura - 273.15
  print(f"{temperatura}°C é igual a {resultado:.2f}°F")
elif opcao == 6:
  resultado = (temperatura - 273.15) * 9/5 + 32
  print(f"{temperatura}°C é igual a {resultado:.2f}°F")
else:
    print("Opção inválida! Tente novamente")