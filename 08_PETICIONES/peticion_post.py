import requests

url = "https://webhook.site/88cd82ab-1ef9-4aa5-872e-de916285be64"

payload ={"´plato": "pizza", "cantidad": 2, "precio": 10000}
query_params = {"nombre": "Lucia", "edad": 25}
response = requests.post(url, data=payload, params=query_params)

print(response.status_code) # Código de estado de la respuesta
print(response.text) # Convertir la respuesta a texto