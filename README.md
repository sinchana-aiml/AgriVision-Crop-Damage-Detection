# 🌾 AgriVision – AI-Based Crop Damage Detection & Insurance Claim System

AgriVision is an AI-powered web application designed to detect crop damage using Deep Learning (CNN) and assist farmers in crop insurance claim processing under schemes like **Pradhan Mantri Fasal Bima Yojana (PMFBY)**.  
The system analyzes uploaded crop images, estimates damage percentage, captures farmer location, and provides a **claim approval/rejection dashboard** for officials.

---

## 🚀 Features

### 👨‍🌾 Farmer Side
- Upload crop image (Wheat, Tomato, Pepper, etc.)
- AI-based crop damage detection
- Damage percentage estimation
- Automatic location capture
- Claim status generation (Pending / Approved / Rejected)

### 🧑‍💼 Officer Dashboard
- View submitted claims
- Crop type & damage percentage
- Auto decision logic:
  - **Approved** → Insurance amount granted
  - **Rejected** → Low damage
- Dummy fund allocation display

---

## 🧠 Technology Stack

| Layer | Technology |
|-----|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| AI Model | CNN (TensorFlow, Keras) |
| Dataset | PlantVillage Crop Disease Dataset |
| Deployment (Local) | Flask Server |
| Tools | VS Code, GitHub |

---

## 🧪 Methodology

1. **Dataset Collection**
   - Healthy and damaged crop images collected
2. **Data Preprocessing**
   - Image resizing (128×128)
   - Normalization
3. **Model Training**
   - CNN architecture
   - Binary classification (Healthy vs Damaged)
4. **Prediction**
   - Damage probability calculation
5. **Business Logic**
   - Damage > 30% → Claim Approved
   - Damage ≤ 30% → Claim Rejected
6. **Dashboard Display**
   - Claim status & fund allocation

---

## 📊 Results

- Accurate classification of crop damage
- Damage percentage visualization
- Real-time claim decision
- Farmer-friendly interface

---

## 📸 Screenshots 

<img width="1600" height="759" alt="image" src="https://github.com/user-attachments/assets/7b53f8ee-9a4d-4ffd-a7a8-8dad564b7027" />

---

## 📁 Project Structure
AgriVision/
│
├── dataset/
│ ├── healthy/
│ └── damaged/
│
├── train_cnn.py
├── backend.py
├── app.py
├── index.html
├── crop_damage_model.h5
├── README.md

---

 ▶️ How to Run the Project

1️⃣ Clone Repository
```bash
git clone https://github.com/sinchana-aiml/AgriVision-Crop-Damage-Detection.git
cd AgriVision-Crop-Damage-Detection
2️⃣Install Dependencies
pip install tensorflow flask numpy pillow matplotlib

3️⃣ Run Backend
python backend.py

4️⃣ Open in Browser
http://127.0.0.1:5000
🔮 Future Enhancements

Database integration (SQLite / MongoDB)

PDF claim report generation

Mobile app version

Public cloud deployment

Multi-crop & multi-disease detection

👩‍💻 Developed By

Sinchana
AIML Mini Project – AgriVision

⭐ Acknowledgements

PlantVillage Dataset

TensorFlow & Flask Community

Government of India – PMFBY Scheme
