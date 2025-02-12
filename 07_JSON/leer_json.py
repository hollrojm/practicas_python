import json

with open("persona.json", "r") as archivo:
    persona = json.load(archivo)
    
print(type(persona))
print(persona)