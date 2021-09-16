from flask import Flask, jsonify, request, render_template, redirect, url_for
import random
import requests
import json
from database import *

import webbrowser
# This is a sample Python script.
app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





@app.route('/', methods=['GET', 'POST'])
@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        email = request.form['email']
        pasw = request.form['pasw']
        if login(email, pasw) == true:
            return redirect(url_for('weather'))
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        pasw = request.form['pasw']
        success = add_member(email, pasw)
        if success == 1:
            return redirect(url_for('main'))
        else:
            return render_template('signup.html')
    else:
        return render_template('signup.html')


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        try:
            lat = request.form['lat']
            lon = request.form['lon']
            response = requests.get(
                "https://api.breezometer.com/weather/v1/current-conditions?lat="+lat+"&lon="+lon+"&key=968e39ec6d3647bb842e5945a4abdaf0")
            data = response.json()
            info = data['data']
            print(info)
            return render_template('weather.html', info=info, lat=lat, lon=lon)
        except:
            response = requests.get(
                "https://api.breezometer.com/weather/v1/current-conditions?lat=48.857456&lon=2.354611&key=968e39ec6d3647bb842e5945a4abdaf0")
            data = response.json()
            info = data['data']
            print(info)
            lon = '2.354611'
            lat = '48.857456'
            return render_template('weather.html', info=info, lat=lat, lon=lon)
    else:
        response = requests.get(
            "https://api.breezometer.com/weather/v1/current-conditions?lat=48.857456&lon=2.354611&key=968e39ec6d3647bb842e5945a4abdaf0")
        data = response.json()
        info = data['data']
        print(info)
        lon = '2.354611'
        lat = '48.857456'
        return render_template('weather.html', info=info, lat=lat, lon=lon)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
        debug=True
    )
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
