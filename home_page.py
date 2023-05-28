# HomePage

# 再改一下 button位置

import tkinter as tk

class HomePage():
    def __init__(self, win, cb):
        self.win = win
        self.cb = cb
        self.components = {
            'title': tk.Label(win, text='\n一起聚餐吧\n', fg='black', bg='#f2d5a3', font=('Arial', 22), width=30, height=3,
                              justify='center'),
            'start': tk.Button(win, text='START', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2,
                               activebackground='black', activeforeground='yellow', command=self.cb),
            'intro': tk.Label(win, text='Hey! My dear friends!!!\n和最酷的朋友一起吃飯\n當然要用最酷的方式選出最讚的時間地點啦！\n點擊start開啟你的最酷飯局', fg='black', bg='#f5ebe0', font=('Arial', 12),
                              width=50, height=6),}

    def layout(self):
        self.components['title'].place(anchor="center", relx=0.5, rely=0.069)
        self.components['start'].place(anchor="center", relx=0.5, rely=0.278)
        self.components['intro'].place(anchor="center", relx=0.5, rely=0.173)


    def show(self):
        self.layout()
        for _, item in self.components.items():
            item.place()

    def hide(self):
        for _, item in self.components.items():
            item.place_forget()


if __name__ == '__main__':
    win1 = tk.Tk()
    win1.geometry('1280x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')

    p1 = HomePage(win1, lambda:p1.hide())
    p1.show()

    win1.mainloop()
