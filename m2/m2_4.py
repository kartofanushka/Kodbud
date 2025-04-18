class Dragon:
    def __init__(self):
        self.x=500
        self.y=random.randint(50,550)
        self.v=random.randint(1,3)
        self.photo=PhotoImage(file='4-2/dragon.png')

class Knight:
    def __init__(self):
        self.x=80
        self.y=h//2
        self.v=0
        self.vv=0
        self.photo=PhotoImage(file='4-2/knight.png')
    def up(self,event):
        self.v =-3
    def down(self,event):
        self.v =3
    def left(self,event):
        self.vv =-3
    def right(self,event):
        self.vv =3
    def stop(self,event):
            self.v =0
            self.vv =0


from tkinter import*
import random

w=600
h=600
window=Tk()
window.geometry(str(w)+'x'+str(h))
canvas= Canvas(window, width=w, height=h, bg='white')
canvas.place(x=0,y=0) #.grid(?,?)

bg_photo= PhotoImage(file='4-2/bg_2.png')

dragon = Dragon()
dragons=[]

for i in range(random.randint(3,4)):
    dragons.append(Dragon())
    dragons_count=len(dragons)

knight=Knight()
dr_photo=dragon.photo
def game():
    canvas.delete('all')
    canvas.create_image(300,300, image=bg_photo)
    canvas.create_image(knight.x,knight.y, image=knight.photo)
            
    # knight.y += knight.v
    if knight.y<=65 or knight.y>=h-65:
        knight.y = knight.y
    else:
       knight.y += knight.v
    if knight.x<=65 or knight.x>=w-65:
        knight.x = knight.x
    else:
       knight.x += knight.vv
    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x,dragon.y, image=dragon.photo)
        if (knight.x-dragon.x)**2+(knight.y-dragon.y)**2<=96**2:
            number=dragons.index(dragon)
            del dragons[number]
        if dragon.x<= 0:
            canvas.delete('all')
            score=len(dragons)
            canvas.create_image(300,300, image=bg_photo)
            canvas.create_text(w//2, h//6,text='You Lose',font='Times 60', activefill='black', fill='red')
            canvas.create_text(w//2, h-h//6,text=score,font='Times 60', activefill='black', fill='red')
            for l in range(score):
                # canvas.create_text(w//3-10*l, h-h//7,text=score,font='Times 36', activefill='black', fill='red')
                canvas.create_image(w//3+100*l,h-h//2, image=dragon.photo)
            break
    if len(dragons)==0:
        canvas.delete('all')
        canvas.create_image(300,300, image=bg_photo)
        canvas.create_text(w//2, h//6,text='You Win',font='Times 60',fill='green')
        canvas.create_image(w//7, h-h//5, image=knight.photo)
        for l in range(dragons_count):
            # print(l,dragons_count)
            canvas.create_image(w//3+100*l,h-h//6,image=dr_photo)
        
            canvas.create_text(w//3+100*l, h-h//6,text=X,font='Arial 60', activefill='black', fill='red')
   
    window.after(5,game)
game()

# пересечение картинок по т пифагора
# (x1-x2)**2+(y1-y2)**2<=(w1/2+w2/2)**2+(w1/2+w2/2)***2

window.bind('<Key-Up>',knight.up)
window.bind('<Key-Down>',knight.down)
window.bind('<Key-Left>',knight.left)
window.bind('<Key-Right>',knight.right)

window.bind('<KeyRelease>',knight.stop)
window.mainloop()

# 1
# Доделайте нашу игру с рыцарем. Первым делом необходимо сделать рамки в игре, чтобы рыцарь не улетал за наше окно. Реализуйте это с помощью кода.
# 2
# Добавьте рыцарю движение по оси X.