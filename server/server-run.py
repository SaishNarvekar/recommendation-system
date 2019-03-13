from flask import Flask, request
from flask_cors import CORS
import json
from itinerary import Itinerary

app = Flask(__name__)
CORS(app, support_credentials=True)
app.secret_key = "82bfce4d0166155f1dd8524112584fb1"

@app.route("/")
def index():
    return """{"0": ["Vasco da Gama", "Bambolim Beach", "Dona Paula", "Our Lady of the Immaculate Conception Church", "St. Thomas Chapel", "Aguada Fort", "Sinquerim Beach", "Candolim Beach Rd", "Calangute Beach", "Baga Beach", "Anjuna Beach", "Vagator Beach", "Chapora Fort", "Morjim Beach", "Arambol Beach", "Church of St. Francis of Assisi", "Mandovi River", "Se Cathedral", "Basilica of Bom Jesus", "Church of St. Cajetan", "Majorda Beach", "Colva Beach", "Benaulim Beach", "Cabo de Rama Beach", "Cabo de Rama Fort", "Butterfly Beach", "Dudhsagar Falls", "Bhagwan Mahaveer Sanctuary and Mollem National Park", "Mhadei Wildlife Sanctuary"]}"""

@app.route('/api/travelType=<travelType>&numberOfDays=<days>&prefence1=<data1>&prefence2=<data2>&prefence3=<data3>&prefence4=<data4>')
def loc(travelType,days,data1,data2,data3,data4):
    
    dataList = [data1,data2,data3,data4]
    itinerary = Itinerary(travelType,days,dataList)
    # print(json.dumps(itinerary.getItinerary()))
    return json.dumps(itinerary.getItinerary())

if __name__ == '__main__':  
    app.run(host="0.0.0.0",debug=True)