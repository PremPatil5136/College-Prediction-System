# 🎓 College Prediction System

AI-Powered College Admission Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Machine Learning](https://img.shields.io/badge/ML-Machine_Learning-green.svg)
![Flask](https://img.shields.io/badge/Flask-Web_App-red.svg)
![Random Forest](https://img.shields.io/badge/Model-Random_Forest-orange.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-95%25+-success.svg)

---

## 📺 Project Demo Video

**Watch the complete walkthrough** of the College Prediction System including data preprocessing, model training, web interface, and live predictions.

📹 **Video File:** `[[Utils/ML Project.m](https://github.com/PremPatil5136/College-Prediction-System/assets/USER_ID/VIDEO.mp4)`

---

## 📖 About the Project

The **College Prediction System** is an intelligent machine learning application that predicts college admissions based on CAP (Centralized Admission Process) round data. Using a Random Forest Classifier trained on 100,000+ records from three CAP rounds, the system provides students with the top 5 most probable colleges they can get admission to, along with probability percentages.

---

## ✨ Key Features

### 🎯 Smart Predictions
Get top 5 college recommendations with accurate probability scores based on your profile

### 📊 Multi-Round Analysis
Trained on CAP Round 1, 2, and 3 data for comprehensive predictions

### 🌐 Web Interface
User-friendly Flask-based web application with intuitive design

### ⚡ Real-time Results
Instant predictions processed in milliseconds

### 📈 Data Visualization
Comprehensive EDA with interactive charts and graphs

### 🔒 High Accuracy
95%+ test accuracy with optimized Random Forest model

---

## 💻 Input & Output

### 📥 Input Parameters

- **Branch:** Engineering branch (Civil, Computer, etc.)
- **Marks:** Percentile/Score obtained
- **Caste:** Category (NGOPENH, SC, ST, OBC)
- **CAP Round:** Round number (1, 2, or 3)
- **Status:** Government/Private preference

### 📤 Output Results

- Top 5 predicted colleges
- Admission probability percentage
- Ranked by likelihood
- Confidence scores for each prediction
- Instant processing time

---

## 🎓 Example Prediction
```
📝 Input:
Branch: Civil Engineering
Marks: 83.8
Caste: NGOPENH
CAP Round: 2
Status: Government

🎯 Output - Top 5 Predicted Colleges:

1. College of Engineering Pune — 87.45%
2. VJTI Mumbai — 76.32%
3. COEP Technological University — 65.18%
4. Walchand College Sangli — 54.27%
5. Government College Amravati — 48.91%
```

---

## 🔬 Model Training Process

### 1️⃣ Data Collection
Combined 3 CAP rounds with 100,000+ records

### 2️⃣ Data Cleaning
Handled missing values with interpolation and forward fill

### 3️⃣ Feature Engineering
Label encoding for categorical variables

### 4️⃣ Model Training
Random Forest with 80/20 train-test split

### 5️⃣ Evaluation
Accuracy, MSE, and R² score metrics

### 6️⃣ Deployment
Saved models as .pkl files for production

---

## 📊 Project Statistics

- **100,000+** Training Records
- **3** CAP Rounds Analyzed
- **95%+** Prediction Accuracy
- **Top 5** College Recommendations
- **Real-time** Processing

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Machine Learning**
- **Flask Web App**
- **Random Forest**
- **Scikit-learn**
- **Pandas**
- **NumPy**

---

## 📁 Project Structure
```
College_Prediction_Project/
│
├── CSV_Dataset/
│   ├── CAP_Round1_Full.csv
│   ├── CAP_Round2_Full.csv
│   └── CAP_Round3_Full.csv
│
├── models/
│   ├── college_model.pkl
│   ├── feature_encoders.pkl
│   └── label_encoder.pkl
│
├── static/
│   ├── style.css
│   ├── app.js
│   └── images/logo.png
│
├── templates/
│   ├── index.html
│   ├── about.html
│   └── contact.html
│
├── Utils/
│   ├── ML Project.mp4
│   └── redMe.html
│
├── app.py
├── index.ipynb
└── README.md
```

---

## 🚀 How to Run

### Installation
```bash
git clone https://github.com/PremPatil5136/College-Prediction-System.git
cd College-Prediction-System
pip install flask pandas scikit-learn numpy
```

### Run Application
```bash
python app.py
```

Open your browser and navigate to `http://localhost:5000`

---

## 👨‍💻 Project By: Prem Patil

**College Prediction System - AI/ML Project**

- 🔗 [GitHub](https://github.com/PremPatil5136)
- 💼 [LinkedIn](#)
- 📧 [Email](#)
- 🌐 [Portfolio](#)

---

## ⭐ Show Your Support

Star this project on GitHub if you find it helpful!

**Made with ❤️ using Python & Machine Learning**

© 2026 College Prediction System. All rights reserved.
