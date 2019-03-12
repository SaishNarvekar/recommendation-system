from flask import Flask, request
from flask_cors import CORS
from server.route import Route
import json
# from server import model

app = Flask(__name__)
CORS(app, support_credentials=True)
app.secret_key = "82bfce4d0166155f1dd8524112584fb1"

@app.route("/")
def index():
    return "Hello World"

@app.route('/api/travelType=<travelType>&numberOfDays=<days>&prefenceList<dataList>')
def loc(travelType,days,dataList):
    route = Route('Vasco da Gama',3,['Beach','Monumental']) #List will get created by user and filled with data from front end
    itinerary = route.GameOver()
    jsonObj = {}
    for i in itinerary:
        jsonObj[i] = i
    return json.dumps(jsonObj)

if __name__ == '__main__':  
    app.run(host="0.0.0.0",debug=True)