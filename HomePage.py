# HomePage

# 再改一下 button位置

class HomePage():
    def __init__(self, win):
        self.win = win

    def create_lb1 (self):
        self.lb1 = tk.Label(self.win, text='一些功能介紹', fg='black', bg='#f2d5a3', font=('Arial', 12), width=23, height=2)
        self.lb1.grid(column=1, row=10)  
    
    def create_start(self):
        self.start = tk.Button(self.win, text='START', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2,
                activebackground='black', activeforeground='yellow', command=self.conceal1)
        self.start.grid(column=1, row=50)

    def create_lbtitle(self):
        self.lbtitle = tk.Label(self.win, text='\n一起聚餐吧\n', fg='black', bg='#f2d5a3', font=('Arial', 22), width=30, height=3,
                   justify='center')
        self.lbtitle.grid(column=1, row=0)


    def show1(self):
        self.create_lb1()
        self.create_lbtitle()
        self.create_start()

    def conceal1(self):
        self.lbtitle.grid_remove()
        self.start.grid_remove()
        self.lb1.grid_remove()
    

if __name__ == '__main__':
    import tkinter as tk

    win1 = tk.Tk()
    win1.geometry('1280x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')

    p1 = HomePage(win1)
    p1.show1()

    win1.mainloop()