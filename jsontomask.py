import os
import json
import numpy as np
import cv2
from PIL import Image

# Diretórios de entrada e saída
input_dir = 'C:/Users/Siraissi/Documents/GitHub/pjct2/img_anno/anoo_jpg/proc/json'
output_dir = 'C:/Users/Siraissi/Documents/GitHub/pjct2/img_anno/anoo_jpg/proc/mask'

# Cria o diretório de saída se não existir
os.makedirs(output_dir, exist_ok=True)

def convert_json_to_mask(json_file, image_width=1024, image_height=1024):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Cria uma máscara em branco
    mask = np.zeros((image_height, image_width), dtype=np.uint8)
    
    # Mapeamento de rótulos para IDs de classe (ajuste conforme necessário)
    label_to_class_id = {'q1': 1, 'q2': 2, 'q3': 3, 'q4': 4}
    
    for shape in data['shapes']:
        points = np.array(shape['points'], dtype=np.int32)
        class_id = label_to_class_id.get(shape['label'], 0)  # Use 0 para classes desconhecidas
        
        # Verifique se os pontos estão dentro dos limites da imagem
        points = np.clip(points, 0, [image_width - 1, image_height - 1])
        
        # Verifique os pontos e o class_id
        print(f"Pontos para {shape['label']}: {points}")
        print(f"ID da classe: {class_id}")
        
        if len(points) > 0:
            # Preenche a máscara com o valor da classe
            cv2.fillPoly(mask, [points], color=class_id)
        else:
            print(f"Nenhum ponto válido para a forma com label {shape['label']}.")
    
    # Adiciona uma verificação para valores únicos na máscara
    unique_values = np.unique(mask)
    print(f"Valores únicos na máscara: {unique_values}")
    
    return mask

def save_mask_with_palette(mask, mask_file):
    # Cria uma imagem colorida a partir da máscara
    color_mask = np.zeros((mask.shape[0], mask.shape[1], 3), dtype=np.uint8)
    
    # Define uma paleta de cores
    palette = [
        [0, 0, 0],  # 0: Preto (background)
        [255, 0, 0],  # 1: Vermelho
        [0, 255, 0],  # 2: Verde
        [0, 0, 255],  # 3: Azul
        [255, 255, 0]  # 4: Amarelo
    ]
    
    # Aplica a paleta de cores
    for i in range(len(palette)):
        color_mask[mask == i] = palette[i]
    
    # Salva a imagem colorida
    Image.fromarray(color_mask).save(mask_file)
    print(f"Máscara colorida salva como {mask_file}")

# Função de teste para garantir o preenchimento básico
def test_fill_poly():
    image_width, image_height = 1024, 1024
    mask = np.zeros((image_height, image_width), dtype=np.uint8)
    
    # Pontos de teste em uma posição específica
    test_points = np.array([[100, 100], [200, 100], [200, 200], [100, 200]], dtype=np.int32)
    
    # Preenche a máscara com um valor visível
    cv2.fillPoly(mask, [test_points], color=255)
    
    # Verifique os valores únicos na máscara de teste
    unique_values = np.unique(mask)
    print(f"Valores únicos na máscara de teste: {unique_values}")
    
    # Salva a máscara de teste
    mask_file = 'test_filled_mask.png'
    Image.fromarray(mask).save(mask_file)
    print(f"Máscara de teste salva como {mask_file}")

# Executa o teste para verificar o preenchimento
test_fill_poly()

# Itera sobre todos os arquivos JSON e gera as máscaras
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        json_file = os.path.join(input_dir, filename)
        
        # Converte JSON para máscara
        mask = convert_json_to_mask(json_file)
        
        # Adiciona uma verificação para ver o conteúdo da máscara
        unique_values = np.unique(mask)
        print(f"{filename} - Valores únicos na máscara: {unique_values}")
        
        # Salva a máscara com a paleta de cores
        base_name = os.path.splitext(filename)[0]
        mask_file = os.path.join(output_dir, f"{base_name}_mask.png")
        save_mask_with_palette(mask, mask_file)

        print(f"Máscara salva como {mask_file}")
