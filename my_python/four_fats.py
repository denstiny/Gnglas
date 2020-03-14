#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageTk 
music =False
def my_app(event):
    global music
    muber = 0
    list_head = Listbox(head,bd = 10,cursor = "plus")
    if music == False: 
        for a in range(1,20,2):
            muber += a
        muber = list(str(muber))
        for nuber in muber:
            list_head.insert(a,head)
            list_head.pack()
        music = True
        Label(head,text = "请输入key").pack()
        ms = Entry(head,bd = 5)
        ms.pack()

    else:
        pass
        exit(1)
    

def main():
    global head,music 
    head = Tk()
    #指定窗口大小
    head.geometry("300x500")
    canvas = Canvas(head,bg="#7D7777",height = 120 ,width = 120)
    image_file = PhotoImage(file = "/mnt/home/chroot/image/1242205.gif")
    canvas.create_image(0,0,anchor='nw',image = image_file)
    #绑定鼠标左键
    canvas.bind("<Button-1>",my_app)
    canvas.bind("ikh")
    canvas.pack()
    head.mainloop()
    pass
main()

