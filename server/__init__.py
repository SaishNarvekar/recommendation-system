from flask import Flask, request
from flask_cors import CORS
from server.itinerary import Itinerary
import json

app = Flask(__name__)
CORS(app, support_credentials=True)
app.secret_key = "82bfce4d0166155f1dd8524112584fb1"

@app.route("/")
def index():
    return """hello world"""

@app.route('/api/travelType=<travelType>&numberOfDays=<days>&prefence1=<data1>&prefence2=<data2>&prefence3=<data3>&prefence4=<data4>&state=<state>')
def loc(travelType,days,data1,data2,data3,data4,state):
    
    dataList = [data1,data2,data3,data4]
    itinerary = Itinerary(travelType,days,dataList,state)
    return json.dumps(itinerary.getItinerary())
