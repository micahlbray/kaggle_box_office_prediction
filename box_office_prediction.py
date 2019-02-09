# -*- coding: utf-8 -*-
"""
Kaggle Competition Entry
Analyzes The Movie Database data set to predict box office revenue for a movie
"""

import pandas as pd
import json
import ast

train_file = 'train.csv'
test_file = 'test.csv'

train_df = pd.read_csv(train_file)
#test_df = pd.read_csv(test_file)

### train_df COLUMNS AS LISTS WITH DICTS TO EXTRACT DATA FROM ###
cols = ['belongs_to_collection', 'genres', 'production_companies', 'production_countries',
        'spoken_languages', 'Keywords', 'cast', 'crew']
for col in cols:
    train_df[cols] = train_df[cols].fillna('[]')
    for i in range(1,5): #range(len(train_df)):
        data = ast.literal_eval(train_df.loc[i, col])
        if len(data) > 0:
            for j in range(len(data)):
                print(data[j])
        else:
            print(data) #should print empty list

