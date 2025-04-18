
# canvas.create_rectangle(10,10, 110, 110, fill="yellow", outline="green")

#Самостоятельное задание - нарисовать 3 квадратика со сторонами 20x20, 40x40, 60x60
# canvas.create_rectangle(120,120, 140, 140, fill="yellow", outline="green")
# canvas.create_rectangle(150,150, 190, 190, fill="yellow", outline="green")
# canvas.create_rectangle(200,200, 260, 260, fill="yellow", outline="green")
# canvas.create_oval(200,200, 260, 260, fill="green", outline="green")

#нарисовать домик
# canvas.create_polygon(10, 260, 60, 200, 110, 260, fill="cyan", outline="black")
# canvas.create_rectangle(10, 260, 110, 360, fill="cyan", outline="black")

from tkinter import *

w=800
h = 600

window = Tk()
window.geometry(str(w)+"x"+str(h)) #"800x600"
canvas = Canvas(window, width=w, height=h, bg="white")
canvas.pack() #.place(x=?,y=?) #.grid(?,?)

class House:
    def __init__(self, roof_color, wall_color):
        self.roof_color1 = roof_color
        self.wall_color1 = wall_color
        self.height = 130
        self.width = 140
    
    def drawHouse(self, x, y):
        canvas.create_polygon(x, y, x + self.width, y, x+ (self.width//2), y-100, fill=self.roof_color1, outline="black")
        canvas.create_rectangle(x, y, x+self.width, y+self.height, fill=self.wall_color1, outline="black")

    def print_info(self):
        print("Roof Color:" + self.roof_color1)
        print("Wall Color:" + self.wall_color1)
        print("Sizes of the house:" + str(self.height) + "x" + str(self.width))

house1 = House(roof_color="green", wall_color="yellow")
#print(dir(house1))
#print(house1.height, house1.width, house1.roof_color1, house1.wall_color1)
house1.drawHouse(100,200)
house1.print_info()
house2 = House(roof_color="cyan", wall_color="pink")
house2.drawHouse(300,200)
window.mainloop()