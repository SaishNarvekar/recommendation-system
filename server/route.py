from connection import Connection
import csv
from model import Model
from clustering import Clustering
from math import sqrt

con = Connection() #database Connection 
cluster = Clustering()

class Route:

    def __init__(self,prefernce,startPoint):
        
        self.userPreference = prefernce
        self.starting = startPoint
        self.filterLocation(prefernce) #fliter Location based on user location
        
    def filterLocation(self,userPreference):
        sql = "select * from places where type in {}".format(tuple(userPreference))
        cur = con.retrive(sql)
        with open('fliter.csv', 'w') as csvfile:
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

        locations.remove(self.starting)
        visitedLocation.append(self.starting)
        placesVisited = 0

        while placesVisited !=20:
            if len(locations) == 0:
                break 
            close = self.findClosestLocation(visitedLocation[-1],locations)
            print(close)
            locations.remove(close)
            visitedLocation.append(close)
            placesVisited+=1
        print(visitedLocation)
        
route = Route(['Beach','Monumental'],'Vasco da Gama') #List will get created by user and filled with data from front end
model = Model()
# route.traversingClusters()
route.GameOver()