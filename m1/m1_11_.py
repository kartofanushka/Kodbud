"""
from fpdf import FPDF
# to add date
from datetime import datetime

# create pdf page
pdf =FPDF('P','mm','A4')
pdf.add_page()

# Place image
pdf.image ('11_bg.jpg', h=297, w=210, x=0, y=0)

# add and use font
pdf.add_font('comic', '', 'C:\Windows\Fonts\comic.ttf', uni=True)
pdf.set_font('comic', size=50)

pdf.set_text_color(0,150,150)
# color fill  for text fields  (only if fill=1)
pdf.set_fill_color(250,250,250)
# color fill  for line fields (only if fill=1) lines, rectangles and cell borders)
pdf.set_draw_color(150,0,150)

#add line
pdf.cell (0,95, ln=1, fill=1)

# name = input("Happy DoG")
name='Vasia'
pdf.cell (0,20, txt="Dear, "+ name+"!", ln=1, align='C', fill=1, border=1)


text='Congratulation my dear hairy friend'
pdf.set_font('comic', size=20)
pdf.set_text_color(150,0,150)
pdf.set_right_margin (50)
pdf.set_left_margin (50)
pdf.multi_cell(0,20, txt=text, align='C', fill=True, border=1)

#add line
# Line(float x1, float y1, float x2, float y2)
pdf.line(20,80,190,80)
# adding date
pdf.set_margins (25,25,10)
today=datetime.today().strftime('%d.%m.%y')
pdf.cell (0,10, txt=today, ln=1, align='R', fill=1)

author_name='Big Dog'
pdf.cell (0,10, txt=author_name, ln=1, align='L', fill=1)




# last line/ Save pdf file
pdf.output('11_postcar.pdf')
"""

from tkinter import *

window =Tk()
window.geometry('700x600')

#===== functions
def draw_menu():
    clear ()
    menu_title = Label(text="what?", font = 'Arial, 24', fg='white', bg='orange')
    menu_title.place (width=700, height=50)
    #  в кнопках clear надо заменить на другую функцию, которая отобрает инфу
    b_1= Button(text='whant to know?', font = 'Arial, 16', fg='black', command=clear)
    b_1.place(x=25,y=75,width=300)

    b_2= Button(text='Open cat photos?', font = 'Arial, 16', fg='black',command=clear)
    b_2.place(x=375,y=75,width=300)
    
def clear():
    #get all obj position
    all_wigets=window.place_slaves()
    for wid in all_wigets:
        wid.destroy()
    draw_home_button()

def draw_home_button():
    b_home= Button(text='home', font = 'Arial, 24', fg='black', command=draw_menu)
    b_home.place(x=25,y=500,width=150)

# ===End functions

draw_menu()



window.mainloop()