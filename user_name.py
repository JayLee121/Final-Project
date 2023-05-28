# User's name 
import tkinter as tk


class UserName():
    def __init__(self, win,cb):
        self.win = win
        self.cb = cb
        
        self.components = {
            'lb3_1' : tk.Label(win, text='你的名字：', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=20, height=2),
            'et3' : tk.Entry(win, show = None),
            'lbtitle' : tk.Label(win, text='\n一起聚餐吧\n', fg='black', bg='#f2d5a3', font=('Arial', 22), width=30, height=3,
                                justify='center'),
            'lb3_4' : tk.Label(win, text='已填好的人', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=20, height=2),
            'lb3_5' : tk.Label(win, text='some user name', fg='black',bg ='#f5ebe0', font=('Arial', 12), width=30, height=5),
            'bt3': tk.Button(win, text='我填好了，換下一位！', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2, activebackground='black', activeforeground='yellow', command = self.cb),
        }
    
    def latout(self):
        self.components['lb3_1'].grid(column=0, row=3)
        self.components['et3'].grid(column=1, row=3)
        self.components['lbtitle'].grid(column=1, row=0)
        self.components['lb3_4'].grid(column=0, row=2)
        self.components['lb3_5'].grid(column=1, row=2)
        self.components['bt3'].grid(column=3, row=5)

    
    def show(self):
        for _, item in self.components.items():
            item.grid()
    
    def hide(self):
        for _, item in self.components.items():
            item.grid_remove()
    
    def get_result(self):
        name = self.et3.get()
        return name



if __name__ == '__main__':
    import tkinter as tk
    
    win1 = tk.Tk()
    win1.geometry('1280x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')
    frame = tk.Frame(win1, width=15)  # 建立 Frame
    frame.grid(row=0, column=0)  

    p2 = UserName(win1, lambda:p2.hide())
    p2.show()


    win1.mainloop()