# Importando as bibliotecas
import time

# Solicita ao usuário o tempo de contagem regressiva
tempo = int(input("Digite o tempo da contagem regressiva em segundos: "))

# Inicia a contagem regressiva
while tempo > 0:
    print(f"Tempo restante: {tempo} segundos")
    # Pausa por 1 segundo
    time.sleep(1)
    tempo -= 1

# Exibe a mensagem final
print("⏰ Tempo esgotado! 🚀")