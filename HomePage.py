# HomePage

# 再改一下 button位置

class HomePage():
    def __init__(self, win):
        self.win = win
        self.lbtitle = tk.Label(self.win, text='\n一起聚餐吧\n', fg='black', bg='#f2d5a3', font=('Arial', 22), width=30, height=3,
                   justify='center')
        self.start = tk.Button(win, text='START', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2,
                activebackground='black', activeforeground='yellow', command= self.conceal1)
        self.lb1 = tk.Label(win, text='一些功能介紹', fg='black', bg='#f2d5a3', font=('Arial', 12), width=23, height=2)

    def show1(self):
        self.lbtitle.grid(column=1, row=0)
        self.start.grid(column=1, row=50)
        self.lb1.grid(column=1, row=10)  
    
    def conceal1(self):
        self.lbtitle.grid_forget()
        self.start.grid_forget()
        self.lb1.grid_forget()
    

import tkinter as tk

if __name__ == '__main__':

    win1 = tk.Tk()
    win1.geometry('1280x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')

    p1 = HomePage(win1)
    p1.show1()

    win1.mainloop()