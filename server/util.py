from server.connection import Connection
from math import sqrt

con = Connection() #database Connection


class Util:
    def __init__(self):
        pass

    def getLatLong(self,location):
        sql = 'select lat,lng from places where name = "{}"'.format(location)
        # print(sql)
        cur = con.retrive(sql)
        for row in cur:
            pass
        return row[0],row[1]

    def findClosestLocation(self,location,cluster):
        x1,y1 = self.getLatLong(location) #current location lat #current location long
        min = 9999999
        closeLocation = ""
        for i in cluster:
            if i == location:
                continue
            x2,y2 = self.getLatLong(i)  # i'th locations lat from cluster # i'th locations long from cluster
            dis = self.getDistance(x1,y1,x2,y2)
            if(dis < min):
                min = dis
                closeLocation = i
        return closeLocation

    #Euclidean Distance
    def getDistance(self,xa,ya,xb,yb):
        return sqrt((xa-xb)**2 + (ya-yb)**2)

    # Output Formating Function
    def formatedOutput(self,itinerary):
        formatedItinerary = list()
        for i in itinerary:
            op = {}
            lat,lng = self.getLatLong(i)
            op['name'] = i
            op['lat'] = lat
            op['lng'] = lng
            formatedItinerary.append(op)
        return formatedItinerary