import os
import json

# Diretórios de entrada e saída
input_dir = 'C:/Users/Siraissi/Documents/GitHub/pjct2/img_anno/anoo_jpg/proc/json'
output_dir = 'C:/Users/Siraissi/Documents/GitHub/pjct2/img_anno/anoo_jpg/proc/yolo'

# Cria o diretório de saída se não existir
os.makedirs(output_dir, exist_ok=True)

def convert_json_to_yolo(json_file, image_width, image_height):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    yolo_annotations = []
    
    for shape in data['shapes']:
        points = shape['points']
        label = shape['label']
        class_id = 0  # Ajuste conforme o índice da sua classe
        
        # Calcula a caixa delimitadora
        x_min, y_min = min(p[0] for p in points), min(p[1] for p in points)
        x_max, y_max = max(p[0] for p in points), max(p[1] for p in points)
        
        # Normaliza as coordenadas
        x_center = (x_min + x_max) / (2 * image_width)
        y_center = (y_min + y_max) / (2 * image_height)
        width = (x_max - x_min) / image_width
        height = (y_max - y_min) / image_height
        
        yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}")
    
    return '\n'.join(yolo_annotations)

# Itera sobre todos os arquivos JSON e gera os arquivos YOLO
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        json_file = os.path.join(input_dir, filename)
        
        # Obtemos as dimensões da imagem
        # Substitua com as dimensões reais ou use uma abordagem para ler as dimensões da imagem
        image_width, image_height = 2041, 1024
        
        yolo_annotations = convert_json_to_yolo(json_file, image_width, image_height)
        
        # Salva o arquivo YOLO
        base_name = os.path.splitext(filename)[0]
        yolo_file = os.path.join(output_dir, f"{base_name}.txt")
        with open(yolo_file, 'w') as f:
            f.write(yolo_annotations)
