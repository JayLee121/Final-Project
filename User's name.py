# User's name 

name_list = []

class UserName():
    def __init__(self, win,frame):
        self.win = win
        self.frame = frame

    def create_lb3_1 (self):
        self.lb3_1 = tk.Label(self.win, text='你的名字：', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=20, height=2)
        self.lb3_1.grid(column=0, row=3)
    
    def create_et3(self):
        self.et3 = tk.Entry(self.win, show = None)
        self.et3.grid(column=1, row=3)

    def create_lbtitle(self):
        self.lbtitle = tk.Label(self.win, text='\n一起聚餐吧\n', fg='black', bg='#f2d5a3', font=('Arial', 22), width=30, height=3,
                                justify='center')
        self.lbtitle.grid(column=1, row=0)
    
    def create_lb3_4(self):
        self.lb3_4 = tk.Label(self.win, text='已填好的人', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=20, height=2)
        self.lb3_4.grid(column=0, row=2)


    def create_lb3_5(self):
        self.lb3_5 = tk.Label(self.win, text='some user name', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=30, height=5)
        self.lb3_5.grid(column=1, row=2)
    
    def create_bt3(self):
        self.bt3 = tk.Button(self.win, text='我填好了，換下一位！', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2, activebackground='black', activeforeground='yellow', command = lambda:(self.conceal2(), self.return_name()))
        self.bt3.grid(column=3, row=5)
    
    
    def show2(self):
        self.create_lb3_1 ()
        self.create_et3 ()
        self.create_lbtitle ()
        self.create_lb3_4 ()
        self.create_lb3_5 ()
        self.create_bt3 ()

    def conceal2(self):
        self.lbtitle.grid_forget()
        self.lb3_1.grid_forget()
        self.et3.grid_forget()
        self.lb3_4.grid_forget()
        self.lb3_5.grid_forget()
        self.bt3.grid_forget()
    
    def return_name(self):
        name = self.et3.get()
        name_list.append(name)
        # print(name_list) 



if __name__ == '__main__':
    import tkinter as tk
    
    win1 = tk.Tk()
    win1.geometry('1280x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')
    frame = tk.Frame(win1, width=15)  # 建立 Frame
    frame.grid(row=0, column=0)  

    p2 = UserName(win1,frame)
    p2.show2()


    win1.mainloop()