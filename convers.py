import os
import subprocess

annotation_dir = 'C:/Users/Siraissi/Documents/GitHub/pjct2/img_anno/anno_json'
output_dir = 'C:/Users/Siraissi/Documents/GitHub/pjct2/img_anno/anno_mask'

# Cria o diretório de saída se não existir
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for json_file in os.listdir(annotation_dir):
    if json_file.endswith('.json'):
        json_path = os.path.join(annotation_dir, json_file)
        output_path = os.path.join(output_dir, json_file.replace('.json', '.png'))
        subprocess.run(['labelme_json_to_dataset', json_path], check=True)
        # Move a máscara gerada para o diretório de saída
        mask_path = json_path.replace('.json', '_mask.png')
        if os.path.exists(mask_path):
            os.rename(mask_path, output_path)
