import requests

url = 'https://economia.awesomeapi.com.br/json/last/EUR-BRL' # URL da API que fornece a cotação do euro

response = requests.get(url) # Faz uma requisição GET para a API

if response.status_code == 200: # Verifica se a requisição foi bem-sucedida
    data = response.json() # Converte a resposta da API em um objeto JSON
    print(f"Cotação do euro: {data['EURBRL']['bid']}") # Imprime a cotação do euro
else:
    print("Não foi possível obter a cotação do euro")