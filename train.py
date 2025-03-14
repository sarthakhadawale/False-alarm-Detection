import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
data=pd.read_excel("historical.xlsx")
# print(data.info())
# print(data.head())
data.drop(["Case No."],inplace=True,axis=1)
# print(data.columns)
# print(data.head())
x=data[['Ambient Temperature( deg C)', 'Calibration(days)',
       'Unwanted substance deposition(0/1)', 'Humidity(%)', 'H2S Content(ppm)',
       'detected by(% of sensors)']]
y=data['Spuriosity Index(0/1)']
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
sc=scalar.fit_transform(x)
x1=pd.DataFrame(sc,columns=['Ambient Temperature( deg C)', 'Calibration(days)',
       'Unwanted substance deposition(0/1)', 'Humidity(%)', 'H2S Content(ppm)',
       'detected by(% of sensors)'])
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x1,y,random_state=60,train_size=0.70)
# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(y_test.shape)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)

with open("train1.pkl",'wb') as file:
    pickle.dump({"model":model,"scalar":scalar},file)
print("Model is train and pkl file is generate successfully")

