import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load trained model
model = tf.keras.models.load_model("crop_damage_model.h5")

# Image settings
IMG_SIZE = 128

# CHANGE THIS PATH to your test image
IMAGE_PATH = "test_leaf.jpg"

# Load and prepare image
img = image.load_img(IMAGE_PATH, target_size=(IMG_SIZE, IMG_SIZE))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# Predict
prediction = model.predict(img_array)

# Output
confidence = float(prediction[0][0])

if confidence > 0.5:
    result = "HEALTHY CROP"
    confidence_score = confidence * 100
else:
    result = "DAMAGED CROP"
    confidence_score = (1 - confidence) * 100

print(f"🌾 Result: {result}")
print(f"📊 Confidence: {confidence_score:.2f}%")
