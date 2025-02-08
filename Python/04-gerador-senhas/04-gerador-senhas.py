# importando as bibliotecas
import random
import string

# Função para gerar senha

def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_especiais):
    caracteres = string.ascii_lowercase # Começa com letras minúsculas

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation

    # Gera a senha aleatória com base nos caracteres permitidos
    # Join concatena as letras
    # random.choice() escolhe um caractere aleatório da string
    # for _ in range() repete random do tamnho que foi passado no range

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Interface para o usuário
print("Gerador de Senhas Aleatórias")

tamanho = int(input("Digite o tamanho da senha desejada: "))
usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
usar_numeros = input("Incluir números? (s/n): ").strip().lower() == "s"
usar_especiais = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'

# Gerando a senha
senha_gerada = gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_especiais)

print(f"\nSua senha gerada é: {senha_gerada}")