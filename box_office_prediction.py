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

### COLUMNS AS LISTS WITH DICTS TO EXTRACT DATA FROM ###
cols = ['belongs_to_collection', 'genres', 'production_companies', 'production_countries',
        'spoken_languages', 'Keywords', 'cast', 'crew']

train_df = pd.read_csv(train_file)
for col in cols:
    print(col)
    out_df = pd.DataFrame()  # empty dataframe to fill
    train_df[col] = train_df[col].fillna('[]')
    for i in range(len(train_df)):
        movie_id = int(train_df.loc[i, 'id'])  # keep track of movie's id
        data = ast.literal_eval(train_df.loc[i, col])
        if len(data) > 0:
            for j in range(len(data)):
                row_dict = {'movie_id': movie_id}
                row_dict.update(data[j])
                out_df = out_df.append(row_dict, ignore_index=True)
    out_df.to_csv('train_' + col + '.csv', index=False)

test_df = pd.read_csv(test_file)
for col in cols:
    print(col)
    out_df = pd.DataFrame()  # empty dataframe to fill
    test_df[col] = test_df[col].fillna('[]')
    for i in range(len(test_df)):
        movie_id = int(test_df.loc[i, 'id'])  # keep track of movie's id
        data = ast.literal_eval(test_df.loc[i, col])
        if len(data) > 0:
            for j in range(len(data)):
                row_dict = {'movie_id': movie_id}
                row_dict.update(data[j])
                out_df = out_df.append(row_dict, ignore_index=True)
    out_df.to_csv('test_' + col + '.csv', index=False)