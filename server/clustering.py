import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2, whiten
from server.connection import Connection
import json

con = Connection()

class Clustering:

    def __init__(self):
        pass

    def createClusters(self, locations):

        loca = list()

        for l in locations:
            sql = 'select Lat,lng from places where name = "{}"'.format(l)
            # print(sql)
            cur = con.retrive(sql)
            # print(cur)
            # print(l)
            loca.append(cur[0])

        # print(loca)

        coordinates = np.array(loca)
        # print(coordinates)

        x, self.y = kmeans2(whiten(coordinates), 2, iter=50)
        # print(y) #cluster number
        # plt.scatter(coordinates[:, 0], coordinates[:, 1], c=y)
        # plt.show()

    def getClusters(self,locations):

        clusterOne = list()
        clusterTwo = list()

        k = 0

        for i in locations:
            if self.y[k] == np.int(0):
                clusterOne.append(i)
            else:
                clusterTwo.append(i)
            k+=1
    
        return clusterOne,clusterTwo