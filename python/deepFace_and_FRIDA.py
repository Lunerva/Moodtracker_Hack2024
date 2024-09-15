
import requests
import json
from deepface import DeepFace

def get_dominant_emotion(img_path):
    try:
        # Analizar la imagen para detectar emociones
        analysis = DeepFace.analyze(img_path=img_path, actions=["emotion"])
        
        # El análisis devuelve una lista de diccionarios, cada uno correspondiente a una imagen analizada
        # Aquí asumimos que hay solo una imagen en el análisis
        emotions = analysis[0]['emotion']
        
        # Obtener la emoción con el valor máximo
        dominant_emotion = max(emotions, key=emotions.get)
        
        return dominant_emotion

    except Exception as e:
        # Manejar errores
        print(f"Error: {e}")
        return None

# Probar la función
img_path = "/Users/luisbarranco/Documents/GitHub/HachMTY2024/ANGRY.jpg"#macos

emotion = get_dominant_emotion(img_path)

print(f"Dominant emotion: {emotion}")



# Define la URL a la que estás haciendo la petición
url = 'https://fridaplatform.com/generate'  # Reemplaza con la URL de tu API

prompt = "give me a plain text (no bolds nor italic) about: recomend only 2 actions for a person who is "+emotion+" during work"
# Define los datos del JSON
data = {
    "inputs": prompt,
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


# La variable gText es el resultado a compartir que debera llegar a android

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get-string', methods=['GET'])
def get_string():
    # Define la variable string que quieres compartir
    return jsonify({"message": gText})

if __name__ == '__main__':
    app.run(debug=True)
