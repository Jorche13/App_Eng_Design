from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect
import os
import weather

UPLOAD_FOLDER = os.path.join('static', 'css')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ideally this should be in a file or database
threshold: int = 75
water_amount: int = 25
location = 'Eindhoven'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/forecast')
def forecast():
    global location

    try:
        data = weather.WeatherAPI(location, '2096fe218663d046a3a37855c4aea57f')

    except (ValueError, ConnectionError):
        return render_template('error.html')

    full_filename = os.path.join(
        app.config['UPLOAD_FOLDER'], 'latest_forecast.png')
    return render_template('forecast.html', user_image=full_filename, data=data)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global threshold
    global water_amount
    global location

    print(threshold, water_amount)

    if request.method == 'POST':
        location = request.form["location"]
        threshold = request.form["threshold"]
        water_amount = request.form["water-amount"]

    return render_template('settings.html', threshold=threshold, water_amount=water_amount, location=location)


@app.route('/base', methods=['POST'])
def display():
    string_from_jojo = request.get_data()
    print(string_from_jojo)
    return render_template('settings.html', string_from_jojo=string_from_jojo)


@app.route('/override')
def override():
    last_watered = datetime.now()

    if request.method == 'POST':
        if request.form.get('action') == 'VALUE':
            pass

    return render_template('override.html', last_watered=last_watered)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
