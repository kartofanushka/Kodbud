import random
"""
from tkinter import*

w=800
h=600
window=Tk()
window.geometry(str(w)+'x'+str(h))
canvas= Canvas(window, width=w, height=h, bg='white')
canvas.pack()# .place(x=?,y=?) .grid(?,?)
def color():
    col=hex(random.randint(0,255))[2:4]+hex(random.randint(0,255))[2:4]+hex(random.randint(0,255))[2:4]
    print("#"+col)
# color()

#Самостоятельное задание - нарисовать 3 квадратика со сторонами 20x20, 40x40, 60x60
canvas.create_rectangle(120,120, 140, 140, fill="yellow", outline="green")
canvas.create_rectangle(150,150, 190, 190, fill="yellow", outline="green")
canvas.create_rectangle(200,200, 260, 260, fill="yellow", outline="green")
canvas.create_oval(200,200, 260, 260, fill="green", outline="green")

#нарисовать домик
canvas.create_polygon(10, 260, 60, 200, 110, 260, fill="cyan", outline="black")
canvas.create_rectangle(10, 260, 110, 360, fill="cyan", outline="black")

# triangle pattern
# canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill="cyan", outline="black")
"""
"""
x=10
y=200
s=100
# canvas.create_polygon(x, y, x+w/8, y-150, x+w/4,y, fill="cyan", outline="black")
x=10
y=100
canvas.create_polygon(x, y, 1/2*s+x, y-((s**2)-(s/2)**2)**0.5, x+s,y, fill="cyan", outline="black")

class House:
    def __init__(self,roof_color, wall_color):
        self.roof_color=roof_color
        self.wall_color=wall_color
        self.height=130
        self.width=140
    def draw_house(self,x,y):
        canvas.create_polygon(x,y,x+self.width/2,y-self.height,x+(self.width),y, fill=self.roof_color, outline="blue")
        canvas.create_rectangle(x,y,x+self.width,y+self.width, fill=self.wall_color, outline="orange")
    def print_info(self):
        print("Roof color:"+self.roof_color)
        print("Wall Color:" + self.wall_color1)
        print("Sizes of the house:" + str(self.height) + "x" + str(self.width))

house1=House(roof_color="green", wall_color="red" )
house2=House(roof_color="cyan", wall_color="pink" )
# print(dir(house1)) #все функц класса
print(house1.height, house1.width, house1.wall_color)

house1.draw_house(200,200)

house2.draw_house(400,200)

"""
"""
=======================
class Fox:
    def __init__(self,main_color, tail_color,nose_color):
        self.main_color=main_color
        self.tail_color=tail_color
        self.n_y_color=nose_color
        self.size=200
        # self.width=140
    def draw_fox(self,x,y,size):
        s=size
        # x=50
        # y=500
        # s=200
        canvas.create_polygon(x, y, 1/2*s+x, y-((s**2)-(s/2)**2)**0.5, x+s,y, fill=self.main_color, outline="black") #body
        canvas.create_rectangle(x, y, x+s, y+s/10, fill=self.main_color, outline="black")

        s1=s/3
        canvas.create_polygon(x+s1, y, 1/2*s1+x+s1, y-((s1**2)-(s1/2)**2)**0.5, x+2*s1,y, fill=self.tail_color, outline="black")
        s5=s/10*4
        canvas.create_polygon(x+s, y, 1/2*s5+x+s, y-((s5**2)-(s5/2)**2)**0.5, x+s+s5,y, fill=self.main_color, outline="black") #tail1
        canvas.create_polygon(1/2*s5+x+s, y-((s5**2)-(s5/2)**2)**0.5, x+s+s5, y, 1/2*s5+x+s+s5,y-((s5**2)-(s5/2)**2)**0.5, fill=self.tail_color, outline="black") #tail2

        x=x-1*s/10
        y=y-((s**2)-(s/2)**2)**0.5
        s2=s/5*4
        canvas.create_polygon(x, y, 1/2*s2+x, y-((s2**2)-(s2/2)**2)**0.5, x+s2,y, fill=self.main_color, outline="black") #head
        s4=s/10*3
        canvas.create_polygon(x+s2-s4/2, y-((s4**2)-(s4/2)**2)**0.5, x+s2, y, x+s2+s4/2, y-((s4**2)-(s4/2)**2)**0.5, fill=self.main_color, outline="black") # ear2

        s3=s/5
        canvas.create_polygon(x, y, 1/2*s3+x, y-((s3**2)-(s3/2)**2)**0.5, x+s3,y, fill=self.n_y_color, outline="black")  #nose

        # ((s5**2)-(s5/2)**2)**0.5
        # s2/3
        canvas.create_oval(1/2*s2+x, y-1/2*s2, 1/2*s2+x+s2/20, y-1/2*s2+s2/20, fill=self.n_y_color, outline="black") #eyes
        canvas.create_oval(5/8*s2+x, y-1/4*s2, 5/8*s2+x+s2/20, y-1/4*s2+s2/20, fill=self.n_y_color, outline="black")

        x=1/2*s2+x
        y=y-((s2**2)-(s2/2)**2)**0.5
        s4=s/10*3
        canvas.create_polygon(x, y, 1/2*s4+x, y+((s4**2)-(s4/2)**2)**0.5, x+s4,y, fill=self.main_color, outline="black")  #ear1
        
        
        # canvas.create_polygon(x,y,x+self.width/2,y-self.height,x+(self.width),y, fill=self.roof_color, outline="blue")
        # canvas.create_rectangle(x,y,x+self.width,y+self.width, fill=self.wall_color, outline="orange")
colors=['black', 'silver', 'gray', 'white', 'maroon', 'red', 'purple', 'fuchsia', 'green', 'lime', 'olive', 'yellow', 'navy', 'blue', 'teal', 'aqua', 'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black', 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 
'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 
'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']

fox1=Fox(main_color="orange",tail_color="#FFFFFF", nose_color="black" )

fox2=Fox(main_color=random.choice(colors), tail_color=random.choice(colors), nose_color=random.choice(colors) )
fox3=Fox(main_color=random.choice(colors), tail_color=random.choice(colors), nose_color=random.choice(colors) )
fox4=Fox(main_color=random.choice(colors), tail_color=random.choice(colors), nose_color=random.choice(colors) )

fox1.draw_fox(50,200,100)

fox2.draw_fox(400,500,200)
fox3.draw_fox(100,500,150)
fox4.draw_fox(600,150,75)
=======================
"""
"""
x=50
y=500
s=200
canvas.create_polygon(x, y, 1/2*s+x, y-((s**2)-(s/2)**2)**0.5, x+s,y, fill="cyan", outline="black") #body
canvas.create_rectangle(x, y, x+s, y+s/10, fill="cyan", outline="black")

s1=s/3
canvas.create_polygon(x+s1, y, 1/2*s1+x+s1, y-((s1**2)-(s1/2)**2)**0.5, x+2*s1,y, fill="white", outline="black")
s5=s/10*4
canvas.create_polygon(x+s, y, 1/2*s5+x+s, y-((s5**2)-(s5/2)**2)**0.5, x+s+s5,y, fill="orange", outline="black") #tail1
canvas.create_polygon(1/2*s5+x+s, y-((s5**2)-(s5/2)**2)**0.5, x+s+s5, y, 1/2*s5+x+s+s5,y-((s5**2)-(s5/2)**2)**0.5, fill="white", outline="black") #tail2

x=x-1*s/10
y=y-((s**2)-(s/2)**2)**0.5
s2=s/5*4
canvas.create_polygon(x, y, 1/2*s2+x, y-((s2**2)-(s2/2)**2)**0.5, x+s2,y, fill="cyan", outline="black") #head
s4=s/10*3
canvas.create_polygon(x+s2-s4/2, y-((s4**2)-(s4/2)**2)**0.5, x+s2, y, x+s2+s4/2, y-((s4**2)-(s4/2)**2)**0.5, fill="cyan", outline="black") # ear2

s3=s/5
canvas.create_polygon(x, y, 1/2*s3+x, y-((s3**2)-(s3/2)**2)**0.5, x+s3,y, fill="black", outline="black")  #nose

# ((s5**2)-(s5/2)**2)**0.5
# s2/3
canvas.create_oval(1/2*s2+x, y-1/2*s2, 1/2*s2+x+s2/20, y-1/2*s2+s2/20, fill="black", outline="black") #eyes
canvas.create_oval(5/8*s2+x, y-1/4*s2, 5/8*s2+x+s2/20, y-1/4*s2+s2/20, fill="black", outline="black")

x=1/2*s2+x
y=y-((s2**2)-(s2/2)**2)**0.5
s4=s/10*3
canvas.create_polygon(x, y, 1/2*s4+x, y+((s4**2)-(s4/2)**2)**0.5, x+s4,y, fill="cyan", outline="black")  #ear1
# canvas.create_polygon(x, y, 1/2*s4+x, y+((s4**2)-(s4/2)**2)**0.5, x+s4,y, fill="cyan", outline="black")



window.mainloop()
"""
# HW
# 1  Рисовалка

# Придумайте рисунок из прямоугольников и треугольников. Опишите его в классе и создайте экземпляр класса.
# Fox 
# 2  Драка

# Что нужно сделать
# Вы работаете в команде разработчиков мобильной игры, и вам досталась такая часть от ТЗ заказчика:
# Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков. Они бьют друг друга в случайном порядке.
# Тот, кто бьёт, здоровье не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. 
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья. 
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
# Реализуйте такую программу.
# ====
# Комментарий преподавателя:
# В целом, все верно.

# По хорошему, класс воина должен содержать три параметра: имя, здоровье и силу атаки:
# class Fight(name, hp, attack)

# self.score-=20  - тут 20 является "магическим числом". Таких чисел следует избегать.
# Надо было так сделать:
# self.score -= self.attack
# =====

class Fight:
    def __init__(self):
        self.score=100

    def heat(self):
        print("Атаковал «Воин» " + str(self) )
    def damage(self):
        self.score-=20
        print("У противника осталось здоровья:" +str(self.score))
         
w1=Fight()
w2=Fight()

while w1.score!=0 and w2.score!=0:
    atk=random.randint(1,2)
    # print(atk)
    if atk==1:
        w1.heat()
        w2.damage()
    
    else:
        w2.heat()
        w1.damage()
if w1.score==0:
    print("Победил «Воин» 2. Счёт " + str(w2.score))
elif w2.score==0:
    print("Победил «Воин» 1. Счёт " + str(w1.score))




"""newlines=[]
read=open('colors.txt','r')
lines=read.readlines()
for line in lines:
    line=line.split('\'', maxsplit=1)
    newlines.append(line[0])

read.close
print(newlines)"""