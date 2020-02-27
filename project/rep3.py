print('Report3')
x = input('Press Enter')
from sklearn.metrics import r2_score,mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
ts_score=[]
mydataset=pd.read_csv("exp_sal.csv")
x=mydataset.iloc[:,0:1]
y=mydataset.iloc[:,1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5,random_state=4)
r=LinearRegression()
r.fit(x_train,y_train)
y_pred=r.predict(x_test)
p=r.coef_
q=r.intercept_
print("Coefficient is: ")
print(p)
print("intercept is: ")
print(q)

