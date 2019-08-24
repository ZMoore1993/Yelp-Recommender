# -*- coding: utf-8 -*-
"""

@author: Zach
NOTE: REDUCE DATASET SIZE. TOOK TO LONG TO FILL RATINGS
"""

import pandas as pd
import numpy as np

def fillUserRatingsDf(df,rdf):
    for i in range(rdf.shape[0]):
        bid = rdf.iloc[i,0]         #business_id of the review
        uid = rdf.iloc[i,5]         #user_id of the review
        rdf.loc[uid,bid] = int(rdf.iloc[i,3])
        print(bid,uid,rdf.loc[uid,bid])
        
def run():
    path = './dataset/'
    #read csv files into dataframes
    udf = pd.read_csv(path + 'dataset_user.csv')
    bdf = pd.read_csv(path + 'dataset_business.csv')
    rdf = pd.read_csv(path + 'dataset_review.csv')
    #create df with user_id as row index and business_id as col index
    df = pd.DataFrame(index=udf.iloc[:,3],columns=bdf.iloc[:,1])
    #replace NaN values with 0
    df = df.fillna(0)
    #fill ratings df
    df = fillUserRatingsDf(df,rdf)

if __name__ == '__main__':
    run()