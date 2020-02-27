print('Predict ')
p=input('Press Enter')
from tkinter import *
from tkinter import messagebox as msg
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
p=r.coef_
q=r.intercept_
def calculate():
      try:
         if (float(sal_entry.get()) <= 0):
            raise AssertionError
     
         hra  = 8550*float(sal_entry.get())+31073.789  
         output_label.configure(text = 'Salary is {:.2f}'.format(hra))
                  
      except ValueError as e:
         msg.showerror('Experience Must be numeric', 'Experience must be numeric')
         sal_entry.focus()
         
      except AssertionError as e:
         msg.showerror('experience can not be <= 0', 'Experience must be >=0')
         sal_entry.focus()
               
def reset():
      sal_entry.delete(0,END)   
      output_label.configure(text = '')   
      sal_entry.focus()
root = Tk()
root.title('Salary calculation from Experience')
root.geometry('600x400')
message_label = Label(root,text='Enter Experience',font=('Arial', 14))
output_label = Label(root,text='', font=('Arial', 14))
sal_entry = Entry(root, font=('Arial', 14), width=6)

calc_button = Button(root,text='Calculate Salary', font=('Arial', 14),
                     bg='Orange', fg='Black',command=calculate)
reset_button = Button(root,text='Clear', font=('Arial', 14), bg='Blue',
                            fg='Black', command=reset)
exit_button = Button(root,text='Exit', font=('Arial', 14),
                     bg='Yellow', fg='Black', command=root.destroy)
message_label.grid(row=0, column=0)
sal_entry.grid(row=0, column=1)
calc_button.grid(row=2, column=1)
reset_button.grid(row=2, column=2)
exit_button.grid(row=2, column=3)
output_label.grid(row=1, column=0, columnspan=3)
sal_entry.focus()
root.mainloop()
 

