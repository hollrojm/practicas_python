import requests

response = requests.get(
    'https://api.github.com/search/repositories', params={'q': 'python'})
print(response.status_code)  # Código de estado de la respuesta
print(response.json())# Convertir la respuesta a un diccionario

data = response.json()
print(data.keys())