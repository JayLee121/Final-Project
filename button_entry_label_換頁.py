### part1 ###
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.geometry('800x450')
win.title('一起聚餐吧')
win.configure(bg='#f2d5a3')


### part2 後端函式 ###


### part3 按鈕功能 ###
def bt1_go():
	conceal1()
	show2()

def bt2_go():
	conceal2()
	show3()

def bt3_go():
	conceal3()
	show4()


### part4 user輸入 ###


### part5 隱藏、顯示 ###
# show1：顯示/打開第一頁，以此類推
# conceal1：隱藏/關閉第一頁，以此類推

def show1():
    lbtitle.grid(column=1, row=0)
    bt1.grid(column=1, row=50)
    lb1.grid(column=1, row=10)

def show2():
    lbtitle.grid(column=1, row=0)
    lb2.grid(column=0, row=3)
    et2.grid(column=1, row=3)
    bt2.grid(column=1, row=50)

def show3():
	lbtitle.grid(column=1, row=0)
	lb3_1.grid(column=0, row=2)
	et3.grid(column=1, row=2)
	lb3_2.grid(column=2, row=2)
	lb3_3.grid(column=3, row=2)
	lb3_4.grid(column=0, row=3)
	bt3.grid(column=3, row=50)

def show4():
	lbtitle.grid(column=1, row=0)
	lb4.grid(column=1, row=50)

def conceal1():
    lbtitle.grid_forget()
    bt1.grid_forget()
    lb1.grid_forget()

def conceal2():
    lbtitle.grid_forget()
    lb2.grid_forget()
    et2.grid_forget()
    bt2.grid_forget()

def conceal3():
    lbtitle.grid_forget()
    lb3_1.grid_forget()
    lb3_2.grid_forget()
    lb3_3.grid_forget()
    lb3_4.grid_forget()
    et3.grid_forget()
    bt3.grid_forget()


### part6 呼叫函式 ###

# 第一頁
lbtitle = tk.Label(win, text = '\n一起聚餐吧\n', fg='black',bg ='#f2d5a3', font=('Arial', 22), width=30, height=3, justify = 'center')
bt1 = tk.Button(win, text='START', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2, activebackground='black', activeforeground='yellow', command= lambda:bt1_go())
lb1 = tk.Label(win, text = '一些功能介紹', fg='black',bg ='#f2d5a3', font=('Arial', 12), width=23, height=2)

# 第二頁：輸入總人數
lbtitle = tk.Label(win, text = '\n一起聚餐吧\n', fg='black',bg ='#f2d5a3', font=('Arial', 22), width=30, height=3, justify = 'center')
lb2 = tk.Label(win, text='請輸入聚餐總人數：', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=20, height=2)
et2 = tk.Entry(win, show = None)
bt2 = tk.Button(win, text='開始投票！', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2, activebackground='black', activeforeground='yellow', command= lambda:bt2_go())

# 第三頁：輸入名字、投票時間、投票餐廳
lbtitle = tk.Label(win, text = '\n一起聚餐吧\n', fg='black',bg ='#f2d5a3', font=('Arial', 22), width=30, height=3, justify = 'center')
lb3_1 = tk.Label(win, text='你的名字：', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=20, height=2)
et3 = tk.Entry(win, show = None)
lb3_2 = tk.Label(win, text='投時間', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=20, height=2)
lb3_3 = tk.Label(win, text='投餐廳', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=20, height=2)
lb3_4 = tk.Label(win, text='已填好的人', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=20, height=2)
bt3 = tk.Button(win, text='我填好了，換下一位！', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2, activebackground='black', activeforeground='yellow', command= lambda:bt3_go())

# 第四頁：結果
lbtitle = tk.Label(win, text = '\n一起聚餐吧\n', fg='black',bg ='#f2d5a3', font=('Arial', 22), width=30, height=3, justify = 'center')
lb4 = tk.Label(win, text='最終結果', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=20, height=2)


### part7 執行 ###
show1()
win.mainloop()
