# Python program to create a table 
   
from tkinter import *

class Table_Grid: 
      
    def __init__(self,root,data,total_columns,total_rows,origin): 
          
        # code for creating table 
        
        self.j=0
        self.i = 0
        for row in data:
            for key,value in row.items():
                if(self.i==0):
                    self.e = tk.Entry(root, width=10, fg='black', 
                               font=('Arial',16)) 
                else:
                    self.e = tk.Entry(root, width=10, fg='black', 
                               font=('Arial',14)) 
                self.e.grid(row=self.i+origin[1], column=self.j+origin[0]) 
                self.e.insert(tk.END, value) 
                self.j += 1
            self.i += 1
            self.j = 0
    
  
class Table: 
      
    def __init__(self,root,lst): 
          
        # code for creating table 
        for i in range(len(lst) ): 
            for j in range(lst[0]): 
                  
                self.e = Entry(root, width=20, fg='blue', 
                               font=('Arial',16,'bold')) 
                  
                self.e.grid(row=i, column=j) 
                self.e.insert(END, lst[i][j]) 

##
#Example usage of the Table Class
##

# take the data 
lst = [(1,'Raj','Mumbai',19), 
       (2,'Aaryan','Pune',18), 
       (3,'Vaishnavi','Mumbai',20), 
       (4,'Rachna','Mumbai',21), 
       (5,'Shubham','Delhi',21)] 
   
   
# create root window 
root = Tk() 
t = Table(root,lst) 
root.mainloop() 
