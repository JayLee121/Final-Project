#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk

def checkbutton_event(widget):
    print('checkbutton_event: ' + widget['text'])

root = tk.Tk()
root.title('my window')
root.geometry('600x600')

frame = tk.Frame(root, height=10, width=15)   # 建立 Frame

scrollbar = tk.Scrollbar(frame)               # 將 Frame 裡放入 Scrollbar
scrollbar.pack(side='right', fill='y')        # 設定位置在右側，垂直填滿



var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()


mycheckbutton1 = tk.Checkbutton(frame, text='18:00',
                                variable=var1,
                                onvalue=1, offvalue=0,
                                command=lambda: checkbutton_event(mycheckbutton1),
                                height= 3)
mycheckbutton1.pack()
mycheckbutton2 = tk.Checkbutton(frame, text='18:30',
                                variable=var2,
                                onvalue=1, offvalue=0,
                                command=lambda: checkbutton_event(mycheckbutton2))
mycheckbutton2.pack()
mycheckbutton3 = tk.Checkbutton(root, text='19:00',
                                variable=var3,
                                onvalue=1, offvalue=0,
                                command=lambda: checkbutton_event(mycheckbutton3))
mycheckbutton3.pack()
mycheckbutton4 = tk.Checkbutton(root, text='19:30',
                                variable=var4,
                                onvalue=1, offvalue=0,
                                command=lambda: checkbutton_event(mycheckbutton4))
mycheckbutton4.pack()
mycheckbutton5 = tk.Checkbutton(root, text='20:00',
                                variable=var5,
                                onvalue=1, offvalue=0,
                                command=lambda: checkbutton_event(mycheckbutton5))
mycheckbutton5.pack()
mycheckbutton6 = tk.Checkbutton(root, text='20:30',
                                variable=var6,
                                onvalue=1, offvalue=0,
                                command=lambda: checkbutton_event(mycheckbutton6))
mycheckbutton6.pack()
mycheckbutton7 = tk.Checkbutton(root, text='21:00',
                                variable=var7,
                                onvalue=1, offvalue=0,
                                command=lambda: checkbutton_event(mycheckbutton7))
mycheckbutton7.pack()

var1.set(1)

root.mainloop()