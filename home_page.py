# HomePage

import tkinter as tk

class HomePage():
    def __init__(self, win, cb):
        self.win = win
        self.cb = cb
        self.components = {
            'title': tk.Label(win, text='\\   一起聚餐吧！  /', fg='black', bg='#f2d5a3', font=('Arial', 30, 'bold'), justify='center'),
            'start': tk.Button(win, text='START', bg='#e3d5ca', fg='black', font=('Arial', 14), width=20, height=2,
                               activebackground='black', activeforeground='yellow', command=self.cb),
            'intro': tk.Label(win, text=f'''

Hey! My dear friends!!!

和最酷的朋友們一起吃飯
當然要用最酷的方式選出最讚的時間和地點啦！

召集你的朋友過來
輪流輸入名字、填選方便的時間和想去的餐廳
就能得到最佳的聚餐結果囉！

點擊下方 START 按鈕
開啟你的最酷飯局！(ง •ૅ౪•᷄)ว 

''', fg='black', bg='#f5ebe0', font=('Arial', 18), justify='left', width=50),}

    def layout(self):
        self.components['title'].place(anchor="center", relx=0.5, rely=0.2)
        self.components['start'].place(anchor="center", relx=0.5, rely=0.8)
        self.components['intro'].place(anchor="center", relx=0.5, rely=0.5)


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

    p1 = HomePage(win1)
    p1.show()

    win1.mainloop()