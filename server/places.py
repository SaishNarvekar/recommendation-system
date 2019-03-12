import json 
import requests as r
from server.connection import Connection
# import os

con = Connection()

# API_KEY = os.environ["PLACES_API_KEY"]
API_KEY = "AIzaSyB62-VZMuBZO2r3Ncja9bTbHSfkARc3kQc"
baseURL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

names = con.retrive("SELECT * from Names")

for name in names:

  para = {'key':API_KEY,'query':name[0]}
  data = r.get(baseURL,para).json()
  print(data)

  for result in data['results']:
    
    sql = "insert into places values {}".format(tuple((result['place_id'],result['name'],float(result['geometry']['location']['lat']),float(result['geometry']['location']['lng']))))

    con.insert(sql)

