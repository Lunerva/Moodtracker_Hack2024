import requests
import json

# Define la URL a la que estás haciendo la petición
url = 'https://fridaplatform.com/generate'  # Reemplaza con la URL de tu API

# Define los datos del JSON
data = {
    "inputs": "give me a plain text (no bolds nor italic) about: recomend only 2 actions for a person who is angry during work",
    "parameters": {
        "max_new_tokens": 200
    },
    "stream": True
}

# Realiza la petición POST
response = requests.post(url, json=data)

# Verifica el código de estado de la respuesta
if response.status_code == 200:
    # Imprime el contenido de la respuesta
    res_jason=response.json()
    gText=res_jason.get('generated_text','')
    print(gText)
else:
    print(f"Error {response.status_code}: {response.text}")
