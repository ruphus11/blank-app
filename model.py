import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.metrics import mean_squared_error, r2_score # type: ignore

# Reads the csv file
df = pd.read_csv('salaryData.csv')
# 1. DATA CLEANING

# Finds out how many columns are empty in each row
print(df.isnull().sum())
# Removes any missing values in the data frame
df = df.dropna(axis=0, how='any')
print(df.isnull().sum())
print(df["Job Title"].value_counts())
# Shows the data types of each column
print(df.dtypes)
# Changing the columns with strings to categorical data so as to be able to encode the categorical data into integers
# to allow easier modelling
df["Job Title"] = df["Job Title"].astype("category")  # Changes Job title to categorical data
df["Job Title Encoded"] = df["Job Title"].cat.codes  # Creates a new column with codes for each title
df["Gender"] = df["Gender"].astype("category")  # Changes Gender to categorical data
df["Gender Encoded"] = df["Gender"].cat.codes  # Creates a new column with codes for each gender
df["Education Level"] = df["Education Level"].astype("category")  # Changes Education level to categorical data
df["Education Level Encoded"] = df["Education Level"].cat.codes  # Creates a new column with codes for each level
# Shows each column and its data type
print(df.dtypes)
# Removes the highlighted columns from the df to make more memory for faster execution time
df_final = df.drop(["Education Level", "Gender", "Job Title"], axis=1)
print(df_final.head())

# 2. DATA MODELLING

# Identifying the X and Y variables
X = df_final[["Age","Gender Encoded","Education Level Encoded","Job Title Encoded","Years of Experience"]]
y = df_final["Salary"]
# Splitting the data to be trained and data to be tested
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# Creating the model and training it
regModel = LinearRegression()  # Creating
regModel.fit(X_train, y_train)  # Training
# Making predictions
y_pred = regModel.predict(X_test)
print(y_pred)
print(regModel.score(X_test, y_test))

# 3. EVALUATING PERFORMANCE OF THE MODEL
mse = mean_squared_error(y_test, y_pred)
rSquareValue = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R squared value: {rSquareValue}")
