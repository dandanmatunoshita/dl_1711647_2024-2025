import os
import json
import cv2
import numpy as np

# Diretórios das imagens
dataset_dirs = {
    "cropped_dataset/ColetaAmostra1": 0,
    "cropped_dataset/ColetaAmostra2": 0,
    "cropped_dataset/ColetaAmostra3": 0,
    "cropped_dataset/ColetaAmostra4": 0,
    "cropped_dataset/ColetaAmostra5": 0,
    "cropped_dataset/iron-Fe": 1
}

# Lista para armazenar os dados de todas as imagens
image_data_list = []

# Processar cada diretório
for dataset_dir, result_value in dataset_dirs.items():
    if not os.path.exists(dataset_dir):
        print(f"Pasta não encontrada: {dataset_dir}")
        continue

    # Percorrer todas as imagens na pasta
    for filename in os.listdir(dataset_dir):
        if filename.endswith(".jpg"):
            image_path = os.path.join(dataset_dir, filename)

            # Carregar a imagem
            image = cv2.imread(image_path)

            if image is None:
                print(f"Erro ao carregar imagem: {image_path}")
                continue

            # Obter dimensões
            height, width, _ = image.shape

            # Separar os canais de cor (OpenCV usa BGR por padrão)
            B, G, R = cv2.split(image)

            # Converter para listas de listas
            R = R.tolist()
            G = G.tolist()
            B = B.tolist()

            # Criar estrutura JSON
            image_data = {
                "image_id": filename.split('.')[0],
                "filename": filename,
                "format": "JPG",
                "dimensions": {
                    "width": width,
                    "height": height
                },
                "channels": {
                    "R": R,
                    "G": G,
                    "B": B
                },
                "result": result_value  # Adicionando o campo result
            }

            image_data_list.append(image_data)

# Salvar os dados em um arquivo JSON
output_json_path = "image_data.json"

with open(output_json_path, "w") as json_file:
    json.dump(image_data_list, json_file, indent=4)

print(f"JSON salvo em {output_json_path}")
