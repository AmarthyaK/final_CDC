import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from src.logger import logging

class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename
   
    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts","training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        max_value = max(result[0])
        logging.info(f"{result}")
        result = np.argmax(model.predict(test_image), axis=1)

        if max_value > 0.5:

            if result[0] == 0:
                prediction_disease = 'Coccidiosis'
                return [{ "image" : prediction_disease}]
            elif result[0] == 1:
                prediction_disease = 'Healthy'
                return [{ "image" : prediction_disease}]
            elif result[0] == 2:
                prediction_disease = 'New Castle Disease'
                return [{ "image" : prediction_disease}]
            elif result[0] == 3:
                prediction_disease = 'Salmonella'
                return [{ "image" : prediction_disease}]
        else:
            return [{ "image" : "I dont know what this image is :("}]