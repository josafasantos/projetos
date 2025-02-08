# Conversor de Moedas

# Importando as bibliotecas
import requests

# Cotações fixas 
cotacoes = {
  "USD": 4.95, # 1 Dólar = 4.95 Reais
  "EUR": 5.38, # 1 Euro = 5.38 Reais
  "GBP": 6.23, # Libra = 6.23 Reais
}

def obter_cotacao(moeda):
  url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
  resposta = requests.get(url)
  dados = resposta.json()
  return float(dados[f'{moeda}BRL']['bid'])

# Exibe opção para o usuário
print("Conversor de Moedas")
print("1 - Real para Dolar (USD)")
print("2 - Real para Euro (EUR)")
print("3 - Real para Libra (GBP)")

# Solicita escolha e o valor em reais
opcao = int(input("Digite o número da conversão desejada: "))
valor = float(input("Digite o valor em reais (R$): "))

# Realiza a conversão com base na escolha

if opcao == 1:
  moeda = "USD"
elif opcao == 2:
  moeda = "EUR"
elif opcao == 3:
  moeda = "GBP"
else:
  print("Opção Inválida!")
  exit()

# Pega a contação da API
cotacao_api = obter_cotacao(moeda)

valor_convertido = valor / cotacoes[moeda]
valor_convertido_api = valor / cotacao_api

print(f"\nR$ {valor:.2f} equivale a {moeda} {valor_convertido:.2f}")
print(f"\nAPI: R$ {valor:.2f} equivale a {moeda} {valor_convertido_api:.2f}")