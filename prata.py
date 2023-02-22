import requests

API_KEY = '2YOUR_KEYl' # Substitua pela sua chave de acesso
SYMBOL = 'XAG' # Símbolo da prata na API

url = f'https://metals-api.com/api/latest?access_key={API_KEY}&base=BRL&symbols={SYMBOL}'

try:
    response = requests.get(url)
    response.raise_for_status() # Verifica se a resposta da API tem status code de sucesso
    data = response.json()
    gold_rate = data['rates'][SYMBOL]
    print(f'Cotação da prata em reais: {gold_rate:.2f}')
except requests.exceptions.RequestException as e:
    print(f'Erro ao obter cotação da prata: {e}')