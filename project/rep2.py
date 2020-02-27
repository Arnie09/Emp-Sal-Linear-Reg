print('Report2')
x = input('Press Enter')
from sklearn.metrics import r2_score,mean_squared_error
import pandas as pd
import numpy as np
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
print("r2 score is: ")
print(r2_score(y_test,y_pred))
print("mean squared error is: ")
print(mean_squared_error(y_test,y_pred))
