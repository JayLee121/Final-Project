# HomePage

# 再改一下 button位置

import tkinter as tk

class HomePage():
    def __init__(self, win,cb):
        self.win = win
        self.cb = cb
        self.components = {
            'title' : tk.Label(win, text='\n一起聚餐吧\n', fg='black', bg='#f2d5a3', font=('Arial', 22), width=30, height=3,
                    justify='center'),
            'start' : tk.Button(win, text='START', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2,
                    activebackground='black', activeforeground='yellow', command= self.cb),
            'intro' : tk.Label(win, text='一些功能介紹', fg='black', bg='#f2d5a3', font=('Arial', 12), width=23, height=2),
        }
        
    def layout(self):
        self.components['title'].grid(column=1, row=0)
        self.components['start'].grid(column=1, row=50)
        self.components['intro'].grid(column=1, row=10)  

    def show(self):
        for _, item in self.components.items():
            item.grid()

    def hide(self):
        for _, item in self.components.items():
            item.grid_remove()

if __name__ == '__main__':
    win1 = tk.Tk()
    win1.geometry('1280x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')

    p1 = HomePage(win1, lambda:p1.hide())
    p1.show()

    win1.mainloop()