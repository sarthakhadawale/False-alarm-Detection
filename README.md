False Alarm Detection System

This project is a Machine Learning-based system designed to predict false alarms in detection systems. The system uses Python, Flask, and HTML for user interaction and prediction display.

🚀 Features

✅ Predicts false alarms using machine learning algorithms
✅ User-friendly HTML form for input
✅ Displays prediction results directly on the webpage
✅ Built using Python, Flask, and scikit-learn

📂 Project Structure

/False-Alarm-Detection-System
 ├── app.py             # Main Flask application (entry point)
 ├── train.py           # ML model training script
 ├── model.pkl          # Trained machine learning model
 ├── requirements.txt   # Dependencies for the project
 ├── templates/         # HTML templates folder
 │   ├── front.html     # Welcome page
 │   └── index.html     # Input form for prediction
 └── static/            # CSS, images, etc.

🖥️ Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/YourUsername/False-Alarm-Detection-System.git
cd False-Alarm-Detection-System

Step 2: Create a Virtual Environment

python -m venv venv

Step 3: Activate the Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

Step 4: Install Dependencies

pip install -r requirements.txt

Step 5: Run the Flask App

python app.py

Step 6: Access the Application

Open your browser and go to:➡️ http://localhost:5000

⚙️ Usage

On the Welcome Page, click "Continue".

Fill in the required input values in the HTML form.

Click the "Submit" button to get the prediction result.

The predicted result (whether it's a false alarm or not) will be displayed on the same page.

📊 Input Features

Ambient Temperature (°C)

Calibration (days)

Unwanted Substance Deposition (0/1)

Humidity (%)

H2S Content (ppm)

Detected by (% of sensors)

🔎 Sample Prediction Output

✅ Prediction: The detected alarm is a False Alarm
✅ Prediction: The detected alarm is Genuine

🧩 Model Training

The train.py script is used to train the machine learning model.

The trained model is saved as model.pkl and loaded in app.py for predictions.

❗ Important Notes

Ensure the model.pkl file is present in the project folder.

If you face issues like ModuleNotFoundError, run:

pip install <missing_module>

🤝 Contributing

Contributions are welcome! If you encounter any bugs or have suggestions for improvement, feel free to create an issue or submit a pull request.

🏆 Credits

Developed by Sarthak Hadawale

Project guided by Technogeek's Data Science course



