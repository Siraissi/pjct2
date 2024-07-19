import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Carregar o modelo salvo
model = tf.keras.models.load_model('modelo_classificacao_pan.keras')

# Caminho da imagem a ser testada
test_image_path = 'C:/Users/Siraissi/Pictures/Figura-5-Radiografia-periapical-pos-obturacao-dos-dentes-11-e-12-A-e-21-e-22-B.png'

# Carregar e pré-processar a imagem
img_width, img_height = 150, 150  # Deve ser o mesmo tamanho usado no treinamento
img = image.load_img(test_image_path, target_size=(img_width, img_height))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.0  # Normalização

# Fazer a predição
prediction = model.predict(img_array)
probability = prediction[0][0] * 100
print(f"Probabilidade de a imagem pertencer à classe 'pan': {probability:.2f}%")

# Interpretação do resultado
if prediction[0] > 0.5:
    print("A imagem pertence à classe 'pan'.")
else:
    print("A imagem não pertence à classe 'pan'.")
