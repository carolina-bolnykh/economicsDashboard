from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)
fred_api_key = 'c64b2c124e8219d275c7479c7d02c644'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/gdp')
def get_data():
    gdp_url = f"https://api.stlouisfed.org/fred/series/observations?series_id=GDP&api_key={fred_api_key}&file_type=json"
    response = requests.get(gdp_url)
    return jsonify(response.json())

@app.route('/api/unemployment')
def get_unemployment_data():
    gdp_url = f"https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&api_key={fred_api_key}&file_type=json"
    response = requests.get(gdp_url)
    return jsonify(response.json())
    

if __name__ == '__main__':
    app.run(debug=True)
