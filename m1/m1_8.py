from tkinter import *
import time
window=Tk() # open window
window.geometry('900x300') #window size
window.resizable(height=False, width=False)
window.config(bg='black')
text=Label(text='Ваш комп заражен ...', fg='green', bg='black', font=('Courier', 16), justify='center')
text.place(x=100, y=100, width=700, height=100)

count= Label(text='5', fg='green', bg='black', font=('Courier', 36))

# count.place(x=100, y=200,width=100,height=100)
def count_start():
    if int(count['text'])>0:
        count['text']= int(count['text']) -1
        count.place(x=70, y=180,width=700,height=70)
        window.after(1000, count_start) # (милисек, что делать)
    else:
        count['text']=0
        width=window.winfo_screenwidth()
        height=window.winfo_screenheight()
        window.geometry(str(width) +'x'+str(height))
        photo=PhotoImage(file='m1_8_skelet.gif')
        label=Label(image = photo, bg='black')
        label.image = photo
        label.place(width=width, height=height,x=0,y=0) # типа должно на полный экран,  но не  коректно открывает
        print('END')
        

def on_close():
    count_start()
    # time.sleep(5) # задержка перед закрытием
    # window.destroy()

        
window.protocol('WM_DELETE_WINDOW', on_close)
# window.tool window True
window.mainloop()

# Make .exe file
# 1.  run in python terminal
# # pip install pyinstaller
# 2. python -m PyInstaller 8.py ( в повершеле в дир где нужный скрипт лежить запустить , 8.py  это  имя файла для созд exe)
