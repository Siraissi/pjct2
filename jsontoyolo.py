import json
import os

def convert_labelme_to_yolo(labelme_json_path, output_dir):
    # Abre o arquivo JSON do Labelme
    with open(labelme_json_path, 'r') as f:
        data = json.load(f)

    # Obtém dimensões da imagem
    image_width = data['size']['width']
    image_height = data['size']['height']

    # Cria o caminho para o arquivo de saída YOLO
    base_filename = os.path.splitext(os.path.basename(labelme_json_path))[0]
    output_file = os.path.join(output_dir, f"{base_filename}.txt")

    with open(output_file, 'w') as f:
        for obj in data['objects']:
            label = obj['classTitle']
            bitmap_data = obj['bitmap']['data']
            origin = obj['bitmap']['origin']
            
            # Calcula a caixa delimitadora (bounding box) a partir do bitmap
            # Para simplificação, consideramos um bitmap como uma caixa delimitadora
            # Isso pode precisar de ajustes dependendo da implementação real
            x_min = origin[0]
            y_min = origin[1]
            x_max = x_min + 1  # Você precisa ajustar isso com base nos dados reais do bitmap
            y_max = y_min + 1  # Você precisa ajustar isso com base nos dados reais do bitmap
            
            # Converte coordenadas para o formato YOLO
            x_center = (x_min + x_max) / 2 / image_width
            y_center = (y_min + y_max) / 2 / image_height
            width = (x_max - x_min) / image_width
            height = (y_max - y_min) / image_height

            # Mapeia o rótulo para um índice
            # Aqui você deve criar um mapeamento de rótulos para índices, por exemplo:
            # label_mapping = {"13": 0}
            # label_index = label_mapping.get(label, -1)
            # Use um índice fixo para este exemplo
            label_index = 0  # Ajuste conforme necessário

            # Escreve a anotação no formato YOLO
            f.write(f"{label_index} {x_center} {y_center} {width} {height}\n")

def main():
    # Diretórios de entrada e saída
    labelme_dir = 'C:/Users/Siraissi/Downloads/teeth-segmentation-on-dental-x-ray-images-DatasetNinja/ds/ann'
    output_dir = 'C:/Users/Siraissi/Downloads/teeth-segmentation-on-dental-x-ray-images-DatasetNinja/ds/annyolo'
    
    # Cria o diretório de saída se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Converte todos os arquivos JSON no diretório
    for json_file in os.listdir(labelme_dir):
        if json_file.endswith('.json'):
            json_path = os.path.join(labelme_dir, json_file)
            convert_labelme_to_yolo(json_path, output_dir)

if __name__ == "__main__":
    main()
