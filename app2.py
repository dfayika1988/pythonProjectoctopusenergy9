import requests
import configparser
from flask import Flask, render_template, request

from flask import Flask

app = Flask(__name__)

@app.route('/')
def macthes_dashboard():
    return render_template('home.html')

@app.route('/results2' , methods=['POST'])
def render_results():
    id_code = request.form['idCode']

    api_key = get_api_key()
    data = get_match_results(id_code, api_key)
    matches = "{0:.2f}".format(data["competitions"][0]["id"])
    matchcompition = data["competitions"][0]["name"]
    code = data["competitions"][0]["code"]
    Plan = data["competitions"][0]["plan"]

    return render_template('results2.html',
                           matches=matches, matchcompition=matchcompition, code=code, Plan=Plan)
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['football-data']['api']

def get_match_results(id, api_key):
     api_url = "http://api.football-data.org" \
               "/v2/competitions".format(id, api_key)
     r = requests.get(api_url)
     return r.json()

if __name__ == '__main__':
    app.run()


