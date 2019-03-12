from flask import Flask, request
from flask_cors import CORS
# from server import model

app = Flask(__name__)
CORS(app, support_credentials=True)
app.secret_key = "82bfce4d0166155f1dd8524112584fb1"

@app.route("/")
def index():
    return "Hello World"

@app.route('/api/travelType=<travelType>&preference=<preferenceList>&numberOfDays=<days>')
def loc(travelType,preferenceList,days):
    print(preferenceList)
    return travelType,preferenceList


if __name__ == '__main__':  
    app.run(host="0.0.0.0",debug=True)