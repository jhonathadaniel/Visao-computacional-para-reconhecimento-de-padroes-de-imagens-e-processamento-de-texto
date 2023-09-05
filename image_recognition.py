import os
import numpy as np
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenarator
from tensorflow.keras.models import Sequencial
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

#configs
date_dir = './Data'
img_height, img_width = 150, 150
batch_size = 30
num_classes = 2
epochs = 25

# gerador de dados

train_datagem = ImageDataGenerator()



# class ImageRecognitionSystem:
#     def __init__(self, model_path):
#         self.model = cv2.dnn.readNet(model_path)


#     def identify_objects(self, image):
#         # Pré-processamento da imagem se necessário
#         blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(300, 300), swapRB=True)
#         self.model.setInput(blob)
#         output = self.model.forward()

#         # Processar a saída da rede para identificar objetos
#         identified_objects = []  # Lista de objetos identificados
#         return identified_objects