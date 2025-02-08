# Calculadora Simples

#Solicita ao usúario dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza as operações simples
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
potencia = num1 ** num2
resto = num1 % num2

#Evita erro de divisão por zero
if num2 != 0:
  divisao = num1 / num2
else:
  divisao = "Erro: divisão por zero"

opcao = input("Digite a operação (+,-,*,/,** ou %): ")

#Exibe os resultados
print('\nResultados:')
if opcao == '+': 
  print(f"Soma: {soma}")
elif opcao == '-':
  print(f"Subtração: {subtracao}")
elif opcao == '*':
  print(f"Multiplicação: {multiplicacao}")
elif opcao == '/':
  print(f"Divisão: {divisao}")
elif opcao == '**':
  print(f"Potenciação: {potencia}")
elif opcao == '%':
  print(f"Resto: {resto}")
else:
  "Opção invalida"
