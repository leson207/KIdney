import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline():
    def __init__(self, filename):
        super().__init__()
        self.filename=filename
    
    def predict(self):
        model = load_model(os.path.join('artifact','training','model.h5'))
        image_name = self.filename
        test_image = image.load_img(image_name, target_size=(224,244))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        result= np.argmax(model.predict(test_image), axis=1)
        
        if result[0]==1:
            prediction='Tumor'
            return [{'image': prediction}]
        else:
            prediction = 'Normal'
            return [{'image': prediction}]
        