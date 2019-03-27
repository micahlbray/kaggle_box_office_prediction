import pandas as pd

train_df = pd.read_csv('train.csv')
train_df = train_df[train_df.revenue > 0] #remove 0 values from revenue
train_df = train_df[['id', 'revenue']]
train_df.rename(columns={'id': 'movie_id'}, inplace=True)

train_cast_df = pd.read_csv('train_cast.csv')
train_cast_df = train_cast_df[['id', 'movie_id', 'order']]
train_cast_df.rename(columns={'id': 'person_id'}, inplace=True)

#### Merged Data Set ####
cast_df = pd.merge(train_df, train_cast_df, how='inner', on='movie_id')
# pivot is for an index without duplicates and pivot_table is the opposite
# print(cast_df.pivot(index='movie_id', columns='person_id', values='order'))
#print(cast_df.pivot_table(index='movie_id', columns='person_id', values='order', aggfunc='sum'))

test = cast_df.groupby(['movie_id', 'person_id'])['order'].sum().unstack()

test.dropna(axis=1)

test.to_csv('test.csv')