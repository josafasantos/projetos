# importa bibliotecas
import random

# O computador escolhe um número aleatório entre 1 e 100
numero_secreto = random.randint(1,100)
tentativas = 0

print("Bem-vindo ao Jogo de Adivinhação")
print("Tente adivinhar o número entre 1 e 100.")

# Loop do Jogo
while True:
  # Solicita um palpite ao jogador
  palpite = int(input("Digite seu palpite: "))
  tentativas += 1

  # Verifica se acertou ou dá um dica
  if palpite > numero_secreto:
    print('🔻 Tente um número menor!')
  elif palpite < numero_secreto:
    print("🔺 Tente um número maior!")
  else:
    print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
    break # Sai do loop