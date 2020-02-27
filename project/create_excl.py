print('Create Excel')
x = input('Press Enter')
import pandas as pd
import numpy as np
import os
import sys

mydataset=pd.read_csv("exp_sal.csv")
mydataset.to_excel(os.path.join(sys.path[0],'exp_sal.xlsx'),sheet_name='create_excl')

