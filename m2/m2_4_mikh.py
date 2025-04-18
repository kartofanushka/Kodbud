from tkinter import *
import random

window = Tk()
w = 600
h = 600
window.geometry(str(w)+"x"+str(h))

canvas = Canvas(window, width=w, height=h)
canvas.place(x=0, y=0)

bg_photo = PhotoImage(file="bg_2.png")

class Knight():
    def __init__(self):
        self.x = 70
        self.y = h//2
        self.v = 0
        self.photo = PhotoImage(file="knight.png")
    
    def up(self, event):
        self.v = -3
    
    def down(self, event):
        self.v = 3

    def stop(self, event):
        self.v = 0
    

class Dragon:
    def __init__(self):
        self.x = 500
        self.y = random.randint(50,550)
        self.v = random.randint(1, 3)
        self.photo = PhotoImage(file="dragon.png")

dragons = []

for i in range(4):
    dragons.append(Dragon())

knight = Knight()

def game():
    canvas.delete("all")
    canvas.create_image(300, 300, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image = knight.photo)

    knight.y += knight.v

    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image = dragon.photo)

        if ( (dragon.x-knight.x)**2 + (dragon.y-knight.y)**2 ) <= 96**2:
            number = dragons.index(dragon)
            del dragons[number]

        if dragon.x <= 0:
            canvas.delete("all")
            canvas.create_text(w//2, h//2, text="You lose!", font= "Verdana 42", fill="red")
            break
    
    if len(dragons) == 0:
        canvas.delete("all")
        canvas.create_text(w//2, h//2, text="You win!", font= "Verdana 42", fill="green")


    window.after(5, game)

game()

window.bind("<Key-Up>", knight.up)
window.bind("<Key-Down>", knight.down)
window.bind("<KeyRelease>", knight.stop)

window.mainloop()