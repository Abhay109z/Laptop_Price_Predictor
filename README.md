## Laptop Price Predictor

A machine learning web application that predicts laptop prices based on user-selected specifications. Built using Python, Scikit-learn, Streamlit, and deployed via Render.

## Features

Predicts laptop prices using trained regression models

Interactive UI built with Streamlit

Uses a cleaned dataset of laptop specifications

Includes preprocessing pipeline and serialized model files

## Project Structure

├── app.py                  # Streamlit app
├── Laptop_Price_predictor.ipynb  # Model training notebook
├── laptop_data.csv         # Raw dataset
├── df.pkl                  # Preprocessed DataFrame
├── pipe.pkl                # Trained pipeline
├── requirements.txt        # Python dependencies
├── Procfile                # Deployment config
├── setup.sh                # Environment setup script
└── .idea/, .gitignore      # IDE and Git config

## Getting Started

- Clone the repo

git clone https://github.com/Abhay109z/Laptop_Price_Predictor.git
cd Laptop_Price_Predictor

- Create a virtual environment

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

- Install dependencies

pip install -r requirements.txt

- Run the app

streamlit run app.py

## Model Details

Algorithm: Linear Regression (can be extended to Random Forest, etc.)

Features used: Brand, RAM, CPU, GPU, OS, Weight, Touchscreen, IPS Panel, Screen Size, Resolution

Target: Laptop Price (in INR)

## Deployment

Hosted on Render using Procfile and setup.sh

Streamlit UI for real-time predictions
