print("Create DF")
print("Press Enter")
import pandas as pd
import numpy as np
mydataset=pd.read_csv("exp_sal.csv")
print(mydataset)
x=mydataset.isnull().sum()
y=mydataset.info()
print("The null values are: ")
print(x)
print(y)



