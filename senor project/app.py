import tkinter as tk
from tkinter import *
from tkinter import ttk





win = tk.Tk()

win.geometry("750x750")

def display_text():
   global m1
   global CheckVar2
   if CheckVar2.get() == 0:
      string= m1.get("1.0",END)
   else:
      string= "button is pressed"
   
   label.delete('1.0',"end")
     
   label.insert('1.0', string)

#Initialize a Label to display the User Input
label=Text(win, font=("Courier 22 bold"),  background="red")
scrollbar = ttk.Scrollbar(win, orient='vertical', command=label.yview)


#  communicate back to the scrollbar
label['yscrollcommand'] = scrollbar.set

CheckVar2 = IntVar()

m1 = Text( win,  width= 80, height= 15, background="red" )

m1.pack()

r1 =  Checkbutton(win, text = "Video", variable = CheckVar2,
                 onvalue = 1, offvalue = 0, height=5,
                 width = 20)
r1.pack(padx=15)

ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(padx=245)

label.pack()


win.mainloop()