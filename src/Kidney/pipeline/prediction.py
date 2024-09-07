import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline():
    def __init__(self, filename):
        super().__init__()
        self.filename=filename
    
    def predict(self):
        model = load_model(os.path.join('artifacts','training','model.keras'))
        image_name = self.filename
        test_image = image.load_img(image_name, target_size=(224,244))
        test_image = image.img_to_array(test_image)
        print(test_image.shape)
        test_image = np.expand_dims(test_image, axis=0)
        print(test_image.shape)
        test_image=tf.image.resize(test_image, (224, 224))
        print(test_image.shape)
        result= np.argmax(model.predict(test_image), axis=1)
        if result[0]==1:
            prediction='Tumor'
            return [{'image': prediction}]
        else:
            prediction = 'Normal'
            return [{'image': prediction}]
        