import requests

url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL' # URL da API que fornece a cotação do dólar

response = requests.get(url) # Faz uma requisição GET para a API

if response.status_code == 200: # Verifica se a requisição foi bem-sucedida
    data = response.json() # Converte a resposta da API em um objeto JSON
    print(f"Cotação do dólar: {data['USDBRL']['bid']}") # Imprime a cotação do dólar
else:
    print("Não foi possível obter a cotação do dólar")
