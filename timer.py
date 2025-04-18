from tkinter import *

win=Tk()

time=5 #input('enter time in seconds ... ')

def update_timer():
    global time
    time -=1
    la.config(text=time)
    if time==0:
        la.config(text="finish")
    else:
        win.after(1000,update_timer)
    
la=Label(win,font=(22), height=8)
la.pack()
update_timer()

win.mainloop()