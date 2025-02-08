# Calculadora Simples

#Solicita ao usúario dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza as operações simples
soma = num1 + num2
subtracao = num1 + num2
multiplicacao = num1 * num2

#Evita erro de divisão por zero
if num2 != 0:
  divisao = num1 / num2
else:
  divisao = "Erro: divisão por zero"

#Exibe os resultados
print('\nResultados:')
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
