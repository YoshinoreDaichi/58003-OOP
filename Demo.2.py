from tkinter import *

win=Tk()
win.geometry("400x300+10+10")
win.title("Grid manager")
#begin placing your widgets here

txt1 = Entry(bd=2)
txt1.grid(row=0,column=0,sticky=N)
txt1.insert(0,"row 1""column=1")
txt2 = Entry(bd=2)
txt2.grid(row=0,column=1,sticky=N)
txt2.insert(1,"row 1""column=2")
txt3 = Entry(bd=2)
txt3.grid(row=0,column=2,sticky=N)
txt3.insert(0,"row 1""column=3")
txt4 = Entry(bd=2)
txt4.grid(row=1,column=0,sticky=N)
txt4.insert(0,"row 2""column=1")
txt5 = Entry(bd=2)
txt5.grid(row=1,column=1,sticky=N)
txt5.insert(0,"row 2""column=2")
txt6 = Entry(bd=2)
txt6.grid(row=1,column=2,sticky=N)
txt6.insert(0,"row 2""column=3")
txt7 = Entry(bd=2)
txt7.grid(row=2,column=0,sticky=N)
txt7.insert(0,"row 3""column=1")
txt8 = Entry(bd=2)
txt8.grid(row=2,column=1,sticky=N)
txt8.insert(0,"row 3""column=2")
txt9 = Entry(bd=2)
txt9.grid(row=2,column=2,sticky=N)
txt9.insert(0,"row 3""column=3")



win.mainloop()
