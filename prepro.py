import cv2
import numpy as np
import os

# Diretório contendo as imagens
input_dir = 'C:/Users/Siraissi/Documents/GitHub/pjct2/img_anno/anoo_jpg'
output_dir = 'C:/Users/Siraissi/Documents/GitHub/pjct2/img_anno/anoo_jpg/proc'

# Cria o diretório de saída se não existir
os.makedirs(output_dir, exist_ok=True)

# Tamanho máximo para a largura e altura
max_width = 1024
max_height = 1024

# Processa cada imagem
for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Lê a imagem
        img_path = os.path.join(input_dir, filename)
        img = cv2.imread(img_path)
        
        # Obtém as dimensões da imagem original
        h, w = img.shape[:2]
        
        # Calcula a proporção
        aspect_ratio = w / h
        
        # Redimensiona mantendo a proporção
        if w > h:
            new_width = min(w, max_width)
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = min(h, max_height)
            new_width = int(new_height * aspect_ratio)
        
        # Redimensiona a imagem
        resized_img = cv2.resize(img, (new_width, new_height))
        
        # Cria uma imagem de fundo branca com o tamanho máximo
        final_img = 255 * np.ones((max_height, max_width, 3), dtype=np.uint8)
        
        # Calcula a posição para centralizar a imagem redimensionada
        y_offset = (max_height - new_height) // 2
        x_offset = (max_width - new_width) // 2
        
        # Cola a imagem redimensionada na imagem de fundo
        final_img[y_offset:y_offset+new_height, x_offset:x_offset+new_width] = resized_img
        
        # Salva a imagem pré-processada
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, final_img)