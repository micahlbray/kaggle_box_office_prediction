import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

train_df = pd.read_csv('train.csv')
train_df = train_df[train_df.budget > 0] #remove 0 values from budget
train_df = train_df[pd.notnull(train_df['runtime'])] #remove null values from runtime

#### Correlation ####
# Correlation matrix with pandas
print(train_df.corr())
# Individual correlation with numpy
print(np.corrcoef(train_df.budget, train_df.revenue)[0, 1]) # 0.7398
print(np.corrcoef(train_df.popularity, train_df.revenue)[0, 1]) # 0.4444
print(np.corrcoef(train_df.runtime, train_df.revenue)[0, 1]) # 0.2067

# Declare X and y
X = train_df[['budget']] #, 'popularity', 'runtime']]
y = train_df['revenue']

plt.scatter(X, y)
plt.title("Budget and Revenue")
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.show()

####################################################################################
# StatsModels
####################################################################################
# Add a constant
X = sm.add_constant(X)

# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model

# Print out the statisticsS
print(model.summary())

####################################################################################
# sklearn
####################################################################################
lm = skl.linear_model.LinearRegression()
model = lm.fit(X, y)
lm.score(X, y)
skl.feature_selection.f_regression(X, y)

####################################################################################
# Data cleanup notes
####################################################################################
# test to see if there are null values
# X.isnull().values.any()

# select null values in dataframe
# X[X.isnull().any(axis=1)]
