from tkinter import *
from random import randint

window = Tk()
window.geometry("600x600")
window.title("Alchemy")
path="m3/7/imgs/"
class Fire:
    image = PhotoImage(file=path+"fire.png").subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay
        elif isinstance(other, Water):
            return Steam
        elif isinstance(other, Air):
            return Fire


class Earth:
    image = PhotoImage(file="m3/7/imgs/ground.png").subsample(4,4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay
        elif isinstance(other, Air):
            return Dust
        elif isinstance(other, Water):
            return Air
        elif isinstance(other, Earth):
            return Earth

class Water:
    image = PhotoImage(file=path+"water.png").subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam
        elif isinstance(other, Air):
            return Water
        elif isinstance(other, Earth):
            return Earth
        elif isinstance(other, Water):
            return Water
    
class Air:
    image = PhotoImage(file=path+"wind.png").subsample(4,4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Fire
        elif isinstance(other, Air):
            return Air
        elif isinstance(other, Earth):
            return Dust
        elif isinstance(other, Water):
            return Steam
    
class Clay:
    image = PhotoImage(file=path+"clay.png").subsample(4,4)
    def __add__(self, other):
        return None
class Steam:
    image = PhotoImage(file=path+"aroma.png").subsample(4,4)
    def __add__(self, other):
            if isinstance(other, Fire):
                return Steam
            elif isinstance(other, Air):
                return Water
            elif isinstance(other, Earth):
                return Earth
            elif isinstance(other, Water):
                return Water
class Dust:
    image = PhotoImage(file=path+"dust.png").subsample(4,4)
    def __add__(self, other):
        return None

    
canvas=Canvas(window,width=600, height=600)
canvas.pack(fill=BOTH,expand=True)

imgs = [Fire(), Earth(), Water()]

for elem in imgs:
    canvas.create_image(randint(50, 550), randint(50, 550), image = elem.image) # elem.image - атрибут экспемляра класса из списка

def move(event):
    #print(event.x, event.y, event)
    images_id = canvas.find_overlapping(event.x - 10, event.y - 10, event.x + 10, event.y + 10) # возвращает tuple из id всех объектов пересечния с заданным прямоугольничком
    #print(images_id)
    # id задается согласно порядку добавления на canvas
    if len(images_id) == 2:
        element_1_id, element_2_id = images_id
   

        print(element_1_id, element_2_id)
        # т.к. мы знаем, что id элемента это его индекс + 1
        # то мы можем получить элемент, зная его id на экране
        element_1 = imgs[element_1_id - 1]
        element_2 = imgs[element_2_id - 1]
        new_element = element_1 + element_2
        print('new_element   ',new_element )
        # элемент может создасться, а может выпасть и ошибка (вернется None)
        if new_element: # если он существует (не None), то выполниться, если не существует (None) - то не выполнится
            canvas.create_image(event.x, event.y, image = new_element.image)
            imgs.append(new_element)
            print(element_1_id,element_2_id)
            # canvas.delete(element_1_id,element_2_id)
            # imgs.remove(element_2)
            # imgs.remove(element_1)
            # add_elem()
            print( 'alch imgs: ',imgs)
            
    canvas.coords(images_id, event.x, event.y)
# def add_fire()            

# add random element button
def add_elem():
    init_imgs = [Fire(), Earth(), Water()]
    elem=init_imgs[randint(0,2)]
    imgs.append(elem)
    canvas.create_image(randint(50, 550), randint(50, 550), image = elem.image) # elem.image - атрибут экспемляра класса из списка
    # print(imgs)

elem_button = Button(canvas, text='Add element', command=add_elem)
elem_button.pack(side=TOP)
window.bind("<B1-Motion>", move) # движение с зажатой левой клавишой мыши
window.mainloop()