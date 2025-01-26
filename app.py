import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model and data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Set page configuration
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    .stTitle {
        color: #4a4a4a;
        font-family: 'Arial', sans-serif;
    }
    .stContainer {
        background-color: white;
        border-radius: 8px;
        padding: 2em;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("Laptop Price Predictor")

with st.container():
    st.markdown('<div class="stContainer">', unsafe_allow_html=True)

    # Layout using columns
    col1, col2 = st.columns(2)

    with col1:
        company = st.selectbox('Brand', df['Company'].unique())
        type_name = st.selectbox('Type', df['TypeName'].unique())
        ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
        weight = st.number_input('Weight of the Laptop (in kg)', format="%.2f")

    with col2:
        touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
        ips = st.selectbox('IPS', ['No', 'Yes'])
        screen_size = st.slider('Screen size (in inches)', 10.0, 18.0, 13.0)
        resolution = st.selectbox(
            'Screen Resolution',
            ['1920x1080', '1366x768', '1600x900', '3840x2160', 
             '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440']
        )

    X_res, Y_res = map(int, resolution.split('x'))
    ppi = ((X_res**2 + Y_res**2)**0.5) / screen_size

    cpu = st.selectbox('CPU', df['Cpu brand'].unique())
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
    gpu = st.selectbox('GPU', df['Gpu brand'].unique())
    os = st.selectbox('OS', df['os'].unique())

    # Convert categorical inputs to numeric
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    st.markdown('</div>', unsafe_allow_html=True)

# Predict price button
if st.button('Predict Price'):
    query = pd.DataFrame({
        'Company': [company],
        'TypeName': [type_name],
        'Ram': [ram],
        'Weight': [weight],
        'Touchscreen': [touchscreen],
        'Ips': [ips],
        'ppi': [ppi],
        'Cpu brand': [cpu],
        'HDD': [hdd],
        'SSD': [ssd],
        'Gpu brand': [gpu],
        'os': [os]
    })

    try:
        predicted_log_price = pipe.predict(query)[0]
        predicted_price = int(np.exp(predicted_log_price))

        st.success(f"The predicted price is ₹{predicted_price:,}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
