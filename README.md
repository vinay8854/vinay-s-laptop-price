# 💻 Laptop Price Predictor 📈

An end-to-end Machine Learning project that predicts the price of laptops based on their specifications. This model is deployed as a web application using Flask and Render.

**Live Demo:** [https://vinay-s-laptop-price-1.onrender.com/]
*(Note: The app may take 30-60 seconds to "wake up" .)*

Screenshots
<img width="927" height="889" alt="image" src="https://github.com/user-attachments/assets/a6effbe6-1ed6-4475-aa34-d905bbe1cecc" />
<img width="945" height="798" alt="image" src="https://github.com/user-attachments/assets/284434d7-cb5d-447d-b170-582cd4e1d040" />



---

## 📖 Overview

This project was built to practice the complete Machine Learning project lifecycle. It starts with a raw dataset, which is cleaned and processed. A machine learning model is then trained, and finally, the model is deployed as a web application where a user can input laptop features and get a price prediction.

The model used is a **Random Forest Regressor** (part of a `scikit-learn` pipeline) which was chosen for its high accuracy and robustness.

## ✨ Features

* **User-Friendly Interface:** A clean web form for users to select laptop specifications.
* **Dynamic Dropdowns:** All options (Brand, CPU, GPU, etc.) are loaded dynamically from the dataset.
* **Real-time Prediction:** The app takes 12 different features and predicts the laptop's price in real-time.
* **Feature Engineering:** Includes on-the-fly feature engineering, such as calculating **PPI (Pixels Per Inch)** from screen size and resolution.

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn, Pandas, NumPy
* **Deployment:** Render (or Heroku, PythonAnywhere, etc.)
* **Model:** `joblib` for loading the pre-trained `scikit-learn` pipeline.

---

