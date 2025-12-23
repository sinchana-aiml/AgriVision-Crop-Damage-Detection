import os
import io
import tensorflow as tf
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ======================
# LOAD CNN MODEL
# ======================
MODEL_PATH = "crop_damage_model.h5"
IMG_SIZE = 128
model = tf.keras.models.load_model(MODEL_PATH)

# ======================
# TEMP DATABASE (DEMO)
# ======================
claims = []

# ======================
# SERVE FRONTEND
# ======================
@app.route("/")
def index():
    return send_file(os.path.join(os.getcwd(), "index.html"))

# ======================
# ANALYZE IMAGE ENDPOINT
# ======================
@app.route("/analyze", methods=["POST"])
def analyze():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    crop = request.form.get("crop", "Unknown")

    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))

    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    healthy_prob = float(prediction[0][0])
    damage_prob = 1 - healthy_prob

    result = "Healthy" if healthy_prob >= 0.5 else "Damaged"
    damage_percentage = round(damage_prob * 100, 2)

    claim = {
        "id": len(claims) + 1,
        "crop": crop,
        "damage": damage_percentage,
        "result": result,
        "location": "Not updated",
        "status": "Pending"
    }

    claims.append(claim)

    return jsonify({
        "claim_id": claim["id"],
        "result": result,
        "damage": damage_percentage
    })

# ======================
# LOCATION ENDPOINT
# ======================
@app.route("/add_location", methods=["POST"])
def add_location():
    data = request.json
    claim_id = data.get("id")
    lat = data.get("latitude")
    lon = data.get("longitude")

    for claim in claims:
        if claim["id"] == claim_id:
            claim["location"] = f"Lat: {lat}, Lon: {lon}"
            return jsonify({"message": "Location updated"})

    return jsonify({"error": "Claim not found"}), 404

# ======================
# DASHBOARD ENDPOINT
# ======================
@app.route("/dashboard", methods=["GET"])
def dashboard():
    return jsonify(claims)

# ======================
# UPDATE STATUS ENDPOINT
# ======================
@app.route("/update_status", methods=["POST"])
def update_status():
    data = request.json
    claim_id = data.get("id")
    status = data.get("status")

    for claim in claims:
        if claim["id"] == claim_id:
            claim["status"] = status
            return jsonify(claim)

    return jsonify({"error": "Claim not found"}), 404

# ======================
# RUN SERVER
# ======================
if __name__ == "__main__":
    app.run(debug=True)
