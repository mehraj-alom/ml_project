from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
import os

class PredictionPipeline:
    def __init__(self, filename, model_path):
        self.filename = filename
        self.model_path = model_path
    
    def predict(self):
        model = load_model(self.model_path)
        test_image = load_img(self.filename, target_size=(224, 224))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)

        prediction = "Healthy" if result[0] == 1 else "Coccidiosis"
        return [{"image": prediction}]  
        



