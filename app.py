import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Laptop Price Predictor 💻", page_icon="💰", layout="centered")

# Title and description
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💻 Laptop Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Estimate the price of your dream laptop based on its specifications.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Input layout
col1, col2 = st.columns([1, 1])

with col1:
    company = st.selectbox('💼 Brand', df['Company'].unique())
    type = st.selectbox('🖥️ Type', df['TypeName'].unique())
    ram = st.selectbox('🧠 RAM (GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = st.number_input('⚖️ Weight (kg)')
    touchscreen = st.selectbox('🖐️ Touchscreen', ['No', 'Yes'])
    ips = st.selectbox('🎨 IPS Display', ['No', 'Yes'])

with col2:
    screen_size = st.slider('📐 Screen Size (inches)', 10.0, 18.0, 13.0)
    resolution = st.selectbox('🖼️ Resolution', [
        '1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800',
        '2880x1800', '2560x1600', '2560x1440', '2304x1440'
    ])
    cpu = st.selectbox('🧩 CPU Brand', df['Cpu brand'].unique())
    hdd = st.selectbox('💾 HDD (GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox('⚡ SSD (GB)', [0, 8, 128, 256, 512, 1024])
    gpu = st.selectbox('🎮 GPU Brand', df['Gpu brand'].unique())
    os = st.selectbox('🖥️ Operating System', df['os'].unique())

st.markdown("<hr>", unsafe_allow_html=True)

# Prediction
if st.button('🔍 Predict Price'):
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    query_df = pd.DataFrame([{
        'Company': company,
        'TypeName': type,
        'Ram': ram,
        'Weight': weight,
        'Touchscreen': touchscreen,
        'Ips': ips,
        'ppi': ppi,
        'Cpu brand': cpu,
        'HDD': hdd,
        'SSD': ssd,
        'Gpu brand': gpu,
        'os': os
    }])

    predicted_price = int(np.exp(pipe.predict(query_df)[0]))

    st.markdown(
        f"""
        <div style='
            background-color: #e3f2fd;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-top: 30px;
        '>
            <h2 style='color: #0d47a1;'>💰 Estimated Price: ₹{predicted_price:,}</h2>
            <p style='font-size: 16px; color: #333;'>Based on your configuration, this is the expected market price.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.balloons()
