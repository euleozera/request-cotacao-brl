import requests

url = 'http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL' # URL da API que fornece a cotação do bitcoin, euro, dólar

response = requests.get(url) # Faz uma requisição GET para a API

if response.status_code == 200: # Verifica se a requisição foi bem-sucedida
    data = response.json() # Converte a resposta da API em um objeto JSON
    print(f"Cotação do bitcoin: {data['BTCBRL']['bid']}") # Imprime a cotação do bitcoin
    print(f"Cotação do dólar: {data['USDBRL']['bid']}")  # Imprime a cotação do dólar
    print(f"Cotação do euro: {data['EURBRL']['bid']}")  # Imprime a cotação do euro
else:
    print("Não foi possível obter a cotação de algum dos ativos")