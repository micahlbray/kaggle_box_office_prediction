# -*- coding: utf-8 -*-
"""
Kaggle Competition Entry
Analyzes The Movie Database data set to predict box office revenue for a movie
"""

import pandas as pd
import json

train_file = 'train.csv'
test_file = 'test.csv'

train_df = pd.read_csv(train_file)
#test_df = pd.read_csv(test_file)

### train_df COLUMNS AS DICTS TO EXTRACT DATA FROM ###
cols = ['belongs_to_collection', 'genres', 'production_companies', 'production_countries',
        'spoken_languages', 'Keywords', 'cast', 'crew']
for col in cols:
    for i in range(len(train_df)):
        #data = json.loads(train_df.loc[i, col])
        data = train_df.loc[i, col]
        try:
            data = '"' + data[1:-1] + '"'
            try:
                data = json.loads(data)
            except:
                print("Could't convert to JSON")
        except:
            pass
        print(data)
