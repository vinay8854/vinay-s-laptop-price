from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the model and data
pipe = joblib.load('pipe.joblib')  # Using joblib for model
df = joblib.load('df.pkl')  # If possible, use joblib for df.pkl too

# Home route
@app.route('/')
def home():
    return render_template('index.html', 
                           brands=df['Company'].unique(),
                           types=df['TypeName'].unique(),
                           cpu_brands=df['Cpu brand'].unique(),
                           gpu_brands=df['Gpu brand'].unique(),
                           os_list=df['os'].unique())

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data from the request
        company = request.form['company']
        type_name = request.form['type_name']
        ram = int(request.form['ram'])
        weight = float(request.form['weight'])
        touchscreen = 1 if request.form['touchscreen'] == 'Yes' else 0
        ips = 1 if request.form['ips'] == 'Yes' else 0
        screen_size = float(request.form['screen_size'])
        resolution = request.form['resolution']
        cpu = request.form['cpu']
        hdd = int(request.form['hdd'])
        ssd = int(request.form['ssd'])
        gpu = request.form['gpu']
        os = request.form['os']

        # Calculate PPI (Pixels per inch)
        X_res, Y_res = map(int, resolution.split('x'))
        ppi = ((X_res**2 + Y_res**2)**0.5) / screen_size

        # Prepare input data for prediction
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

        # Predict the log price using the model pipeline
        predicted_log_price = pipe.predict(query)[0]
        predicted_price = int(np.exp(predicted_log_price))

        # Return the predicted price as a JSON response
        return jsonify({'price': f"₹{predicted_price:,}"})

    except Exception as e:
        # If any exception occurs, return an error message
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
