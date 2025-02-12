import requests

response = requests.get('https://api.github.com')
print(response.status_code) # Código de estado de la respuesta
print(response.headers) # Cabeceras de la respuesta
print(response.text) # Convertir la respuesta a texto
print(response.json()) # Convertir la respuesta a un diccionario
print("codificacion ",response.encoding) # Codificación de caracteres de la respuesta
print("url ",response.url) # URL de la respuesta
print("tiempo de respuesta ",response.elapsed) # Tiempo de respuesta
print(response.content) # Contenido de la respuesta en bytes