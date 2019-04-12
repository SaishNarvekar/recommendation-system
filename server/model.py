import numpy as np
import pandas as pd

class Model:
    
    def __init__(self):
        pass

    def filterPlaces(self,starting):
        #Select Filtered Places
        self.poi= pd.read_csv('.\\server\\files\\filter.csv',index_col='Name',names = ['placeID','Name','Lat','Lng','Rating','Type','State'])

        # Select Reviews
        self.reviews = pd.read_csv('.\\server\\files\\reviews.csv',index_col='Name',names=['ID','Name','UserID','UserRating'])
        
        # Droppped Unwanted Columns
        self.poi.drop(columns=['placeID','Lat','Lng','State'],axis=1,inplace=True)
        self.reviews.drop(columns=['ID'],axis=1,inplace=True)
        
        # Forming Matrix of Reviews and Filtered Placed on Name Column
        self.overall = self.poi.join(self.reviews,on='Name')
        self.overall_pvtable = self.overall.pivot_table(index='UserID',columns='Name',values='UserRating')
        
        # Selected Starting Location
        self.startingLocation = self.overall_pvtable[starting]
        
        # Selected Similar Location using Correlation
        self.similarToStarting = pd.DataFrame(self.overall_pvtable.corrwith(self.startingLocation),columns=['Correlation'])
        self.similarToStarting.dropna(inplace=True)
        self.similarToStarting.sort_values(by='Correlation',ascending=False)
        self.recommendedLocation = self.similarToStarting.join(self.poi,on='Name').sort_values(by='Rating',ascending=False)
        
        # Returning Name of Selected Location
        return self.recommendedLocation.index