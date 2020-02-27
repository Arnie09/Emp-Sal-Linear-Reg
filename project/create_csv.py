print('Create CSV')
x = input('Press Enter')
from tkintertable import TableCanvas, TableModel
from tkinter import *
class TestApp():
    def __init__(self, root):
        self.f = Frame(root, height=200, width=300) 
        self.f.pack(fill=BOTH,expand=1)
        
        self.table = TableCanvas(self.f, read_only=True)
        self.table.importCSV('exp_sal.csv')
        print (self.table.model.columnNames)
        self.table.show()
                  
#---------------------------------
root = Tk()
root.title('Testing tkintertable')
root.geometry('500x300')
obj=TestApp(root)
root.mainloop()


        

