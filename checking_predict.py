from src.pipeline.prediction import PredictionPipeline
from src.utils.common import decodeImage
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

imagename = "C:\\Users\\pragn\\Documents\\MLOPS\\final_CDC\\artifacts\\data_ingestion\\Dataset_CDC_category\\Coccidiosis\\cocci.11.jpg"

test_image = image.load_img(imagename, target_size = (224,224))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)

model = load_model(os.path.join("artifacts","training", "model.h5"))
result = np.argmax(model.predict(test_image), axis=1)

if __name__ == "__main__":
    print(result)