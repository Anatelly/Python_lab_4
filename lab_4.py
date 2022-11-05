from tkinter import *
from random import *
from time import *
from pygame import *

mixer.init()
mixer.music.load('sound.mp3')
mixer.music.play()


down=2
up=40
def key():
    s='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0'.split()
    otv=''
    for i in range(3):
        x=''
        d=4
        for i in range(4):
            c=randrange(up-d)
            if i == 0: d = 0
            x+=s[c]
            d+=c
        otv+=x+'-'
    ent.delete(0,END)
    ent.insert(0,otv[:-1])

window=Tk()
window.title('key')
window.geometry('1024x576')
window.resizable(width=False, height=False)

bg=PhotoImage(file='1.png')
bg_img=Label(window, image=bg)
bg_img.place(relx=0,rely=0)

ent=Entry(window, width=18, font='Arial 30')
ent.place(relx=0.5, rely=0.3, anchor='center')

bt=Button(window, width=10,text='Generate', font='Arial 20', command=key)
bt.place(relx=0.5, rely=0.7, anchor='center')

img=PhotoImage(file='smile.png')
img1=Label(window, image=img)

for i in range(5):
    for i in range(5,95):
        img1.place(relx=i/100,rely=0.9,anchor='center')
        window.update()
        sleep(0.05)
    for i in range(95,5,-1):
        img1.place(relx=i / 100, rely=0.9, anchor='center')
        window.update()
        sleep(0.05)

window.mainloop()