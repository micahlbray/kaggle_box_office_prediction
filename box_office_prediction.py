# -*- coding: utf-8 -*-
"""
Kaggle Competition Entry
Analyzes The Movie Database data set to predict box office revenue for a movie
"""

import pandas as pd

train_file = 'train.csv'
test_file = 'test.csv'

train_df = pd.read_csv(train_file)
#test_df = pd.read_csv(test_file)

print(train_df.dtypes)
print(train_df.head())