
"""SERIALIZAR UN DICCIONARIO A UN ARCHIVO JSON"""
import json

persona = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 25
}

objeto_json = json.dumps(persona, indent=2, ensure_ascii=False,)

with open("persona.json", "w") as archivo:
    #archivo.write(objeto_json)
    
    json.dump(persona, archivo, indent=2, ensure_ascii=False)
    
    