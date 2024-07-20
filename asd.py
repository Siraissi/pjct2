import os

# Define o caminho da pasta onde os arquivos estão localizados
folder_path = r'C:\Users\Siraissi\Documents\GitHub\pjct2\img_anno\anoo_jpg\dataset2\labels\val'

# Itera sobre todos os arquivos no diretório especificado
for filename in os.listdir(folder_path):
    # Verifica se o nome do arquivo termina com '.jpg'
    if filename.endswith('.jpg.txt'):
        # Cria o novo nome do arquivo removendo a extensão '.jpg' e mantendo '.txt'
        new_filename = filename.replace('.jpg.txt', '.txt')
        # Renomeia o arquivo
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

print("Renomeação concluída.")
