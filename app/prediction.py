from PIL import Image
import numpy as np
import os
import tensorflow as tf

model = tf.keras.models.load_model(os.path.join("ml_model","model.h5")) 


class_name = [
    'Alpukat', 'Apel','Bawang Bombai', 'Bawang Merah',
    'Bawang Putih', 'Bayam', 'Beras Merah', 'Beras Putih',
    'Brokoli', 'Buah Naga', 'Buncis', 'Daging Ayam',
    'Daging Sapi', 'Daun Bawang', 'Edamame', 'Ikan Salmon',
    'Ikan Tuna', 'Jagung', 'Kacang Hijau', 'Kacang Kedelai',
    'Kacang Merah', 'Kacang Polong', 'Kentang', 'Labu Putih',
    'Labu Siam', 'Melon', 'Oatmeal', 'Pakcoy', 'Pepaya', 'Pisang',
    'Tauge', 'Telur Ayam', 'Telur Puyuh', 'Tomat', 'Udang', 'Wortel'
]

def predict(image):
    image_resized = image.resize((150, 150))
    image_array = np.array(image_resized) / 255.0

    image_array = np.expand_dims(image_array, axis=0)
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions, axis=1)

    prediction_label = class_name[predicted_class[0]]
    confidence_level = predictions[0][predicted_class[0]]
    return prediction_label, confidence_level
