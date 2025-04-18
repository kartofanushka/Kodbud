from tkinter import *
from tkinter import ttk
# import tkinter as tk
import bs4 as bs
import random
# # from bs4 import *
import requests


window =Tk()
window.geometry('700x600')
style = ttk.Style()
style.configure("BW.TLabel", foreground="white", background="orange", font = 'Arial, 24', justify='center')
style.configure("a.TLabel", foreground="black", font = 'Arial, 16', justify='center')
ttk.Style().configure("TButton", padding=6, relief="flat", background="orange")

#===== functions
def head():

    menu_title = ttk.Label(text="    Не знаешь во что поиграть?", style="BW.TLabel")
    menu_title.place (width=700, height=50)
    
def draw_menu():
    clear()
    head()
    b_1= Button(text='Жми меня', font = 'Arial, 16', fg='black',command=make_btns)
    b_1.place(x=25,y=75,width=300)
    b_2= Button(text='Clear', font = 'Arial, 16', fg='black',command=clear)
    b_2.place(x=375,y=75,width=300)

    
def clear():
    #get all obj position
    all_wigets=window.place_slaves()
    for wid in all_wigets:
        wid.destroy()

    draw_exit_btn ()

def draw_home_button():
    
    b_home= Button(text='home', font = 'Arial, 24', fg='black', command=draw_menu)
    b_home.place(x=25,y=500,width=150)
def draw_exit_btn():
    b_exit = Button(text="Exit",font = 'Arial, 24', fg='black', command=window.destroy)
    # b_exit.pack(side=BOTTOM)
    # b_exit= Button(text='Exit', font = 'Arial, 24', fg='black', command=draw_menu)
    b_exit.place(x=425,y=500,width=150)


#Display a Label
def print_text(text):
   Label(window, text=text,font=('Helvetica 13 bold')).pack()

    
    
def list():
    listbox = Listbox(window)

# fill option added to make widget fill entire frame.
# expand option added to expand widget, if user resizes frame.
    listbox.pack(fill=BOTH, expand=1)

    for z in range(5):
        listbox.insert(END, str(z))

# ===End functions

def get_genres():
    
    # divs = soup.find_all("div", class_="row")
    # div class="ecomerce-items-ajax"
    url ='https://store.steampowered.com/'
    source=requests.get(url)
    source =source.content
    soup=bs.BeautifulSoup(source,'html.parser')
    # file=open('9test.txt', "a",encoding="utf-8")
    lt=str(soup)
    url_dict={}

    divs = soup.find_all("div", class_="popup_genre_expand_header")
    for i in divs:
        if i.text!='':
            gnr = i.find_all("a", class_="popup_menu_item")
            for ii in gnr:
                gnr_n=ii.text.strip()
                gnr_n=gnr_n.replace('-',' ')
                gnr_url=ii.attrs['href']
                url_dict[gnr_n] = gnr_url
                # print(gnr_n)
                # print(gnr_url)
    print(url_dict)
    print(url_dict.keys())
    return(url_dict)

def make_btns():
    clear()
    menu_title = ttk.Label(text="    Выбери жанр", style="BW.TLabel")
    menu_title.place (width=700, height=50)
    global url_dict

    url_dict= get_genres()
    # number of buttons
    n=url_dict.keys()

    #Defining the row and column
    i=0
    x=25
    y=150
    w=50
    row=len(url_dict.keys())//3
    r=1
    for j in url_dict.keys():
        if r <=3 or i==row:
            w=len(j)*12
            b_gnr= Button(text=j, font = 'Arial, 16', fg='black', command= lambda: get_game_by_genr(j))
            b_gnr.place(x=x,y=y,width=w)
            x+=(w+25)
            r+=1
            i+=1
        else:
            r=0
            y+=100
            x=25
            b_gnr= Button(text=j, font = 'Arial, 16', fg='black', command= lambda: get_game_by_genr(j))
            b_gnr.place(x=x,y=y,width=w)
            x+=(w+25)
    draw_home_button()
    draw_exit_btn()


def get_game_by_genr(key):
    urll='https://store.steampowered.com/tags/en/Racing/?snr=1_4_4__125'
    url=url_dict.get(key,urll)
    source=requests.get(url)
    source =source.content
    soup=bs.BeautifulSoup(source,'html.parser')
    div=[]
    div=soup.find('div', id="application_config").attrs['data-ch_main_list_data']
    import ast
    dvlst = ast.literal_eval(div)

    # print(type(dvlst))
    dd='top_sellers'
    for tag in dvlst:
        
        if tag.get('id')==dd:
            # print(tag.get('apps'))
            games=tag.get('apps')

    g=str(random.choice(games).get('id'))
    game_url='https://store.steampowered.com/app/'+g
    source=requests.get(game_url)
    source =source.content
    soup=bs.BeautifulSoup(source,'html.parser')
    answer_text=soup.find('meta', property="twitter:description").attrs['content']
    answer_url=soup.find('link', rel="canonical").attrs['href']
    answer_head=answer_url.rsplit("/")[-2]
    answer_head=answer_head.replace('_',' ')
    # <meta property="twitter:description" content="Human: Fall Flat is a hilarious, light-hearted platformer set in floating dreamscapes that can be played solo or with up to 8 players online. Free new levels keep its vibrant community rewarded.">
	# <link rel="canonical" href="https://store.steampowered.com/app/477160/Human_Fall_Flat/">
    clear()
    print('Предлагаю поиграть в:')
    print(soup.title.string, game_url, answer_text, answer_url, answer_head)
    result_title = ttk.Label(text=" Предлагаю: "+answer_head, style="BW.TLabel")
    result_title.place (width=700, height=50,x=0,y=0)
    result_text = Message(text="Описание:  " +answer_text, justify=LEFT, font=("Arial", 14), width=600)
    result_text.place (width=700, height=150,x=25, y=150)
    link1 = Label(window, text=answer_url, fg="blue", cursor="hand2", font=("Arial", 14))
    link1.place(x=50, y=300)

    print('==============================================================')
    draw_home_button()
    draw_exit_btn()


draw_menu()

window.mainloop()