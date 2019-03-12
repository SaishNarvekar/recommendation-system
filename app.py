from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)
app.secret_key = "82bfce4d0166155f1dd8524112584fb1"

@app.route("/")
def index():
    return "Hello World"

@app.route('/api',methods=['GET','POST'])
def api():
    return '[{"name": "Dona Paula", "lat": "15.4608099", "log": "73.8095574", "cluster": "1"}, {"name": "Vasco da Gama", "lat": "15.388556", "log": "73.843792", "cluster": "0"}, {"name": "Butterfly Beach", "lat": "15.0196019", "log": "74.001647", "cluster": "0"}, {"name": "Anjuna Beach", "lat": "15.5735995", "log": "73.7407065", "cluster": "1"}, {"name": "Calangute Beach", "lat": "15.549441", "log": "73.7534857", "cluster": "1"}, {"name": "Morjim Beach", "lat": "15.6206197", "log": "73.7310943", "cluster": "1"}, {"name": "Sinquerim Beach", "lat": "15.4991464", "log": "73.7674666", "cluster": "1"}, {"name": "Benaulim Beach", "lat": "15.2570626", "log": "73.9187138", "cluster": "0"}, {"name": "Basilica of Bom Jesus", "lat": "15.5008938", "log": "73.9116272", "cluster": "0"}, {"name": "Baga Beach", "lat": "15.5552787", "log": "73.7517307", "cluster": "1"}, {"name": "Arambol Beach", "lat": "15.6846886", "log": "73.7032836", "cluster": "1"}, {"name": "Majorda Beach", "lat": "15.3111553", "log": "73.9018114", "cluster": "0"}, {"name": "St. Thomas Chapel", "lat": "15.4995263", "log": "73.8322494", "cluster": "1"}, {"name": "Vagator Beach", "lat": "15.6029835", "log": "73.733627", "cluster": "1"}, {"name": "Se Cathedral", "lat": "15.5038769", "log": "73.9121918", "cluster": "0"}, {"name": "Our Lady of the Immaculate Conception Church", "lat": "15.4986628", "log": "73.8292705", "cluster": "1"}, {"name": "Church of St. Francis of Assisi", "lat": "15.6486519", "log": "73.830773", "cluster": "1"}, {"name": "Colva Beach", "lat": "15.2791055", "log": "73.935596", "cluster": "0"}, {"name": "Aguada Fort", "lat": "15.4926018", "log": "73.7736513", "cluster": "1"}, {"name": "Chapora Fort", "lat": "15.6060713", "log": "73.7364444", "cluster": "1"}, {"name": "Church of St. Cajetan", "lat": "15.5055969", "log": "73.9150423", "cluster": "0"}, {"name": "Cabo de Rama Fort", "lat": "15.0887849", "log": "73.9215933", "cluster": "0"}, {"name": "Cabo de Rama Beach", "lat": "15.1031826", "log": "73.9255111", "cluster": "0"}, {"name": "Bambolim Beach", "lat": "15.4521897", "log": "73.8487063", "cluster": "0"}, {"name": "Candolim Beach Rd", "lat": "15.5183527", "log": "73.765218", "cluster": "1"}]'

@app.route('/api/<location>')
def loc(location):
    return '[{"name":{}, "lat": "15.4608099", "log": "73.8095574", "cluster": "1"}]'.format(location)

if __name__ == '__main__':  
    app.run(host="0.0.0.0",debug=True)