import tkinter as tk

class UserName():
    def __init__(self, win, cb):
            self.win = win
            self.cb = cb
            self.name_list = []

            # 建立元件
            self.components = {
                #'lb3_1': tk.Label(win, text='名字', fg='black', bg='#f5ebe0', font=('Arial', 16), width=20, height=2),
                'et3': tk.Entry(win, show=None, width=20),
                'lbtitle': tk.Label(win, text='\\  輸入你的名字  /', fg='black', bg='#f2d5a3', font=('Arial', 30, "bold"), justify='center'),
                'lb3_4': tk.Label(win, text='已填好的人 (^o^)／', fg='black', bg='#f2d5a3', font=('Arial',16), width=30, height=2),
                'bt3': tk.Button(win, text='下一頁', bg='#e3d5ca', fg='black', font=('Arial', 16), width=20,
                                height=2, activebackground='black', activeforeground='yellow', command=self.cb),
            }
        
            self.components['listbox_frame'] = tk.Frame(win, bg='#f5ebe0')
            self.components['listbox'] = tk.Listbox(self.components['listbox_frame'], listvariable=tk.StringVar(value= self.name_list), width=30, height=7, font=('Arial', 16), bg='#f5ebe0')
            self.components['scrollbar'] = tk.Scrollbar(self.components['listbox_frame'], orient="vertical", command=self.components['listbox'].yview)
            self.components['listbox'].config(yscrollcommand=self.components['scrollbar'].set)
    
    # 設定所有元件在視窗的位置
    def layout(self):
        #self.components['lb3_1'].place(anchor="center", relx=0.42, rely=0.380)
        self.components['et3'].place(anchor="center", relx=0.5, rely=0.35)
        self.components['lbtitle'].place(anchor="center", relx=0.5, rely=0.25)
        self.components['lb3_4'].place(anchor="center", relx=0.5, rely=0.475)
        self.components['listbox_frame'].place(anchor="center", relx=0.5, rely=0.6) 
        self.components['bt3'].place(anchor = "center", relx= 0.5, rely = 0.8)
        self.components['listbox'].pack(side="left", fill="y")
        self.components['scrollbar'].pack(side="right", fill="y")
    

    # 在視窗上顯示所有元件
    def show(self):
        self.components['et3'].delete(0, tk.END)
        self.layout()
        self.components['listbox'].config(listvariable=tk.StringVar(value= self.name_list))


    # 在視窗上隱藏所有元件
    def hide(self):
        for _, item in self.components.items():
            item.place_forget()
        
    # 獲取選中複選框的值  
    def get_result(self):
        name = self.components['et3'].get()
        return name
    
    # 將使用者新輸入的名字加入name_list 
    def set_name_list(self, name_list):
        self.name_list = name_list.copy()
    
    # 清除name_list裡面的值
    def clear_name_list(self, name_list):
        self.name_list = []


# 為了讓頁面能夠單獨測試，且避免import時會執行以下程式碼
if __name__ == '__main__':
    name_list = ['1','2','3','4','4','4','4','4','4','4','4']
    win1 = tk.Tk()
    win1.geometry('1280x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')
    
    def call_back(): 
        name_list.append(page.get_result())
        page.hide()
   
    page = UserName(win1, call_back)
    page.show()

    win1.mainloop()
    print(name_list)