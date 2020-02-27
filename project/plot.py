print('Plot')
x = input('Press Enter')
from sklearn.metrics import r2_score,mean_squared_error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
mydataset=pd.read_csv("exp_sal.csv")
ts_score=[]
x=mydataset.iloc[:,0:1]
y=mydataset.iloc[:,1]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5,random_state=4)
r=LinearRegression()
r.fit(x_train,y_train)
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, r.predict(x_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
x=plt.show()
print("The training set plot is: ",x)
plt.scatter(x_test,y_test,color='red')
plt.plot(x_test,r.predict(x_test),color='blue')
plt.title("experience vs salary(Test set)")
plt.xlabel('experience')
plt.ylabel('salary')
y=plt.show()
print("The test set plot is: ",y)



