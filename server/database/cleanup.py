import json 
import requests as r
from connection import Connection

con = Connection()

baseURL = "https://maps.googleapis.com/maps/api/place/details/json"
API_KEY = "AIzaSyAgFaxKO-dDZwjWGLvjlKrhGd6uLStEElY"

places_ids = con.retrive("SELECT place_id from places where state = 'Rajasthan'")

count = 0

for pid in places_ids:
    pid = pid[0]
    para = {'key':API_KEY,'placeid':pid}

    data = r.get(baseURL,para).json()

    if 'Rajasthan' not in data['result']['formatted_address']:
        sql = "Delete from places where place_id = '{}'".format(pid)
        con.insert(sql)
        count+=1
        print('deleted place {}'.format(count))