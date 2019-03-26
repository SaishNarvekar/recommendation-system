from connection import Connection
import csv
from model import Model
from math import sqrt

con = Connection() #database Connection 
model = Model()


class Route:

    def __init__(self,startPoint,days,prefernce,state):
        
        self.days = days
        self.userPreference = prefernce
        self.starting = startPoint
        self.state = state
        self.filterLocation(prefernce,state) #fliter Location based on user location
        
    def filterLocation(self,userPreference,state):

        if self.state == 'Goa':

            if 'Beach' in userPreference:
                sql = "select * from places where state = '{}' and type in {} and Rating >= 4.0 UNION select * from places where name = '{}' UNION select * from places where name = '{}'".format(self.state,tuple(userPreference),'Vasco da Gama','Colva Beach')
            else:
                sql = "select * from places where state = '{}' and type in {} UNION select * from places where name = '{}' UNION select * from places where name = '{}'".format(self.state,tuple(userPreference),'Vasco da Gama','Colva Beach')

        if self.state == 'Rajasthan':
            # print('Here')
            sql = "select * from places where state = '{}' and Rating >= 4.0".format(self.state)


        cur = con.retrive(sql)
        # print(cur)
        with open('filter.csv', 'w+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in cur:
                filewriter.writerow(list(row))
                
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

    def GameOver(self):

        locations = list()
        visitedLocation = list()

        for index in model.filterPlaces(self.starting):
            locations.append(index)

        # print(locations)
    
        locations.remove(self.starting)
        visitedLocation.append(self.starting)
        placesVisited = 1

        while placesVisited != int(self.days)*3:
            if len(locations) == 0:
                break 
            close = self.findClosestLocation(visitedLocation[-1],locations)
            # print(close)
            locations.remove(close)
            visitedLocation.append(close)
            placesVisited+=1
        return visitedLocation