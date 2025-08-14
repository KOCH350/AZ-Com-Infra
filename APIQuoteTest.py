
import requests


api_key = 'Jyc9aQmw+Vl543vq1AJzYw==kpuOkDYJ0u38bH5x'

url = 'https://api.api-ninjas.com/v1/quotes'

headers = {
    'X-Api-Key': api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    quote_data = response.json()[0]
    quote_string = f'"{quote_data["quote"]}" - {quote_data["author"]}'
    print(quote_string)
else:
    print(f'Fehler beim Abrufen des Zitats: {response.status_code}')
