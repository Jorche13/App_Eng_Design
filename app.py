from flask import Flask, render_template, url_for, request, redirect
import os

UPLOAD_FOLDER = os.path.join('static', 'css')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

initial_treshold = 10

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forecast')
def forecast():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'latest_forecast.png')
    return render_template('forecast.html', user_image = full_filename)

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/set_treshold', methods=['POST', 'GET'])
def set_treshold():
    global initial_treshold
    output = request.form.to_dict()
    number = output['number']
    if number:
        initial_treshold = number
    return render_template('settings.html', number=number, initial_treshold=initial_treshold)

@app.route('/display', methods = ['GET'])
def display():
    string_from_jojo = request.get_data()
    return render_template('settings.html', string_from_jojo=string_from_jojo)

#accesses the override webpage
@app.route('/override')
def override():
    #if request.method == 'POST':
       # if request.form.get('action') == 'VALUE':
           # pass

       # else:
         #   pass

   # elif request.method == 'GET':
      #  return render_template('override.html')

    return render_template('override.html')

#Uses the overriding button to execute a function in the terminal, namely printing Hello
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")

#@app.route('/static/css/latest_forecast.png')
#def latest_event():
    #return send_from_directory(os.path.join(app.root_path, 'static'), 'latest_forecast.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug = True)