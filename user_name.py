# User's name 
import tkinter as tk


class UserName():
    def __init__(self, win,cb):
        self.win = win
        self.cb = cb
        
        self.components = {
            'lb3_1': tk.Label(win, text='你的名字：', fg='black', bg='#f5ebe0', font=('Arial', 12), width=20, height=2),
            'et3': tk.Entry(win, show=None),
            'lbtitle': tk.Label(win, text='\n一起聚餐吧\n', fg='black', bg='#f2d5a3', font=('Arial', 22, "bold"), width=30,
                                height=3, justify='center'),
            'lb3_4': tk.Label(win, text='已填好的人', fg='black', bg='#f2d5a3', font=('Arial',12, "bold"), width=30, height=2),
            'lb3_5': tk.Label(win, text='other username', fg='grey', bg='#f5ebe0', font=('Arial', 10), width=30,
                              height=5),
            'bt3': tk.Button(win, text='我填好了，換下一位！', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20,
                             height=2, activebackground='black', activeforeground='yellow', command=self.cb),
        }

    def layout(self):
        self.components['lb3_1'].place(anchor="center", relx=0.42, rely=0.380)
        self.components['et3'].place(anchor="center", relx=0.56, rely=0.380)
        self.components['lbtitle'].place(anchor="center", relx=0.5, rely=0.278)
        self.components['lb3_4'].place(anchor="center", relx=0.5, rely=0.44)
        self.components['lb3_5'].place(anchor="center", relx=0.5, rely=0.5)
        self.components['bt3'].place(anchor = "center", relx= 0.5, rely = 0.65)


    def show(self):
        self.layout()
        for _, item in self.components.items():
            item.place()

    def hide(self):
        for _, item in self.components.items():
            item.place_forget()
            
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
