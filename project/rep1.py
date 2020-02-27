print('Report1')
x = input('Press Enter')
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
ts_score=[]
mydataset=pd.read_csv("exp_sal.csv")
x=mydataset.iloc[:,0:1]
y=mydataset.iloc[:,1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5,random_state=4)
print("Training dataset is: ")
print(x_train)
print("Test dataset is: ")
print(y_test)
