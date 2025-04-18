from tkinter import *
import time
import random
import pygame
from PIL import Image, ImageTk

pygame.init()

class Ball:
    def __init__(self, canvas, platform, color):
        self.canvas = canvas
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.dir = [-3, -2, 2, 3, -4, 4, -1, 1, -0.5, 0.5, -2.5, 2.5, -3.5, 3.5, -1.5, 1.5, -4.5, 4.5]
        self.x = random.choice(self.dir)
        self.y = -1
        self.platform = platform
        self.bootom_touch = False
        self.sound = pygame.mixer.Sound("sound.mp3")
        self.sound.set_volume(0.05)
        self.alive = True

    def touch_platform(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform.rect)
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            if ball_pos[3] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                return True
        return False

    def draw(self):
        if self.bootom_touch == False:
            self.canvas.move(self.oval, self.x, self.y)
            pos = self.canvas.coords(self.oval) # получаем 4 координаты [x1, y1, x2, y2]
            if pos[0] <= 0 :
                self.x = 3
                self.sound.play()
            if pos[2] >= 500:
                self.x = -3
                self.sound.play()
            if pos[1] <= 0:
                self.y = 3
                self.sound.play()
            if self.touch_platform(pos) == True:
                self.y -= 3
                self.sound.play()
            if pos[1] >= 400:
                self.bootom_touch = True

class Platform:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0
        self.canvas.bind_all("<KeyPress-Left>", self.left)
        self.canvas.bind_all("<KeyPress-Right>", self.right)

    def left(self, event):
        self.x = -3
    def right(self, event):
        self.x = 3

    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        pos = self.canvas.coords(self.rect)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= 500:
            self.x = 0

window = Tk()
window.title("Arcanoid")
window.resizable(0,0)
window.geometry("500x400")
window.wm_attributes("-topmost", 1)

canvas = Canvas(window, width=500, height=400)
canvas.pack()
img = Image.open("bg.png")
img = img.resize((500, 400))
img = ImageTk.PhotoImage(img)
canvas.create_image(250, 200, image=img)

platform = Platform(canvas, "green")
balls = [Ball(canvas, platform, "red") for i in range(10)]
end = True
while end:
    end = False
    for ball in balls:
        ball.draw()
        if ball.bootom_touch == False:
            end = True
    platform.draw()
    window.update()
    time.sleep(0.01)