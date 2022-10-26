from cProfile import label
from tkinter import *
from random import randint
root=Tk()
root.title("Dice")


a=["*","* *","* * *","* *\n* *","* *\n *\n* *","* * *\n* * *"]
def roll():
    x=a[randint(0,5)]
    lab=Label(root,text=x)
    lab.grid(row=0,column=0,padx=20,pady=20)
inpu=Button(root,text="roll",command=roll)
inpu.grid(row=999,column=5,padx=10,pady=10)

root.mainloop()
