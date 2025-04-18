from tkinter import *
import time
window = Tk()

window.geometry("900x300")

window.resizable(height=False, width=False)

window.config(bg='black')

text = Label(text="Ваш компудактер заражен))!", fg="green", font=("Courier", 34), bg="black")

text.place(x=100, y=100, width=700, height=100)

count = Label(text="5", fg="green", font=("Courier", 34), bg="black")



def count_start():
    if int(count['text']) > 0:
        count['text'] = int(count['text']) - 1
        count.place(x=250, y=25, width=400, height=100)
        window.after(1000, count_start) #через 1000 миллисекунд и запускает функцию count_start
    else:
        count["text"] = 0
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry(str(width) + "x" + str(height))
        photo = PhotoImage(file="m1_8_skelet.gif")
        label = Label(image=photo, bg="black")
        label.image = photo
        label.place(width=width, height=height, x=0,y=0)
        print("Конец")


def on_close():
    count_start()
    #window.destroy()

window.protocol("WM_DELETE_WINDOW", on_close)


window.mainloop()