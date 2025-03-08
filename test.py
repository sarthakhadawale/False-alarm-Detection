
from flask import Flask, render_template,render_template_string, request
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

app = Flask(__name__)
scalar=StandardScaler()
# Load your trained ML model (replace 'train.pkl' with your model file)
model = pickle.load(open('train1.pkl', 'rb'))
@app.route('/')
def front():
    return render_template('front.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST','GET'])
def predict():
    # Extract input values from form
    temperature = int(request.form['temperature'])
    calibration = int(request.form['calibration'])
    deposition = int(request.form['deposition'])
    humidity = int(request.form['humidity'])
    h2s_content = int(request.form['h2s_content'])
    sensors_detected = int(request.form['sensors_detected'])

    # Create input array for the model
    input_data = np.array([[temperature, calibration,deposition, humidity,h2s_content, sensors_detected]])
    # x_scale=scalar.fit_transform(input_data)
    test_array = input_data.reshape(1, 6)
    x1=pd.DataFrame(test_array,columns=['Ambient Temperature( deg C)','Calibration(days)',
       'Unwanted substance deposition(0/1)','Humidity(%)','H2S Content(ppm)',
       'detected by(% of sensors)'])
    
   
    # Make prediction
    prediction = model.predict(x1)

    # Return the result
    result = "False Alarm,No Danger" if prediction[0] == 1 else "True Alarm,Danger"
    return render_template_string (f'''<html>
    <head><title>False alarm Detection Result</title></head>
    <body>
    <h1>{prediction}</h1><hr>
    <h1>Result:</h1><hr>
    <h3>Input Data:</h3><br>
    <h3>Temperature:{temperature}</h3><br>
    <h3>Calibration:{calibration}</h3><br>
    <h3>Deposition:{deposition}</h3><br>
    <h3>Humidity:{humidity}</h3><br>
    <h3>H2S Content:{h2s_content}</h3><br>
    <h3>Sensor Detected:{sensors_detected}</h3>
    <hr>
    <h1><b>Result</b></h1>
    <h1>{result}</h1>
    <br>
    <h1><i>Thank You......</i></h1>
    </body>
    </html>''')

if __name__ == '__main__':
    app.run(debug=True,port=5002)