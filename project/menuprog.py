from tkinter import *
import sys
import os
import subprocess
from sys import platform

class Empsal:

   
    def __init__(self, root):

        self.main_lbl=Label(root, text='Experience Vs.Salary Linear Regression and Predict Salary Based On Experience', fg='red', font=('Arial', -22, 'bold underline'))
        self.main_lbl.place(x=350, y=350)
        
        self.callPython = ""
        if platform == "linux" or platform == "linux2":
            self.callPython = "python3"
        elif platform == "win32":
            self.callPython = "python.exe"

        self.menubar=Menu(root)
        root.config(menu=self.menubar)             
        self.mysql_menu=Menu(root, tearoff=0)

        self.menubar.add_cascade(label='Data Conversion', menu=self.mysql_menu)
        self.mysql_menu.add_command(label='Build DF', command=self.create_df)
        self.mysql_menu.add_command(label='Build CSV', command=self.create_csv)
        self.mysql_menu.add_command(label='Convert to Excel', command=self.mysql_to_xls)
         
      
        self.mysql_menu.add_separator()
        self.mysql_menu.add_command(label='Exit', command=root.destroy)

        self.data_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Reports', menu=self.data_menu)
        self.data_menu.add_command(label='Rep1', command=self.rep1)
        self.data_menu.add_command(label='Rep2', command=self.rep2)
        self.data_menu.add_command(label='Rep3', command=self.rep3)
        self.data_menu.add_command(label='Plot', command=self.plot)
        
       
        self.predict_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Prediction', menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict', command=self.predict)
         

    def create_df(self):
        subprocess.check_call([self.callPython,"create_df.py"])
    def create_csv(self):
        subprocess.check_call([self.callPython,"create_csv.py"])
    def mysql_to_xls(self):
        subprocess.check_call([self.callPython, "create_excl.py"])
    
    def rep1(self):
        subprocess.check_call([self.callPython, "rep1.py"])
    def rep2(self):    
        subprocess.check_call([self.callPython, "rep2.py"])
    def rep3(self):
        subprocess.check_call([self.callPython, "rep3.py"])               
    def plot(self):
        subprocess.check_call([self.callPython, "plot.py"])
        
    def predict(self):
        subprocess.check_call([self.callPython, "predict.py"])     
#=====================================================================================================
  
root=Tk()
root.title('Experience vs. Salary Linear Regression and predict Salary based on Experience')

obj=Empsal(root)
root.geometry('800x600')
root.mainloop()

                                 
        
        
        
        
                 
