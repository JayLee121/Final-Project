import tkinter as tk

class UserName():
    def __init__(self, win, cb):
            self.win = win
            self.cb = cb
            self.name_list = []
            self.components = {
                #'lb3_1': tk.Label(win, text='名字', fg='black', bg='#f5ebe0', font=('Arial', 16), width=20, height=2),
                'et3': tk.Entry(win, show=None, width=20),
                'lbtitle': tk.Label(win, text='\\  輸入你的名字  /', fg='black', bg='#f2d5a3', font=('Arial', 30, "bold"), width=30, height=3, justify='center'),
                'lb3_4': tk.Label(win, text='已填好的人 (^o^)／', fg='black', bg='#f2d5a3', font=('Arial',16), width=30, height=2),
                'bt3': tk.Button(win, text='下一頁', bg='#e3d5ca', fg='black', font=('Arial', 16), width=20,
                                height=2, activebackground='black', activeforeground='yellow', command=self.cb),
            }
            
            self.components['listbox_frame'] = tk.Frame(win, bg='#f5ebe0')
            self.components['listbox'] = tk.Listbox(self.components['listbox_frame'], listvariable=tk.StringVar(value= self.name_list), width=30, height=7, font=('Arial', 16), bg='#f5ebe0')
            self.components['scrollbar'] = tk.Scrollbar(self.components['listbox_frame'], orient="vertical", command=self.components['listbox'].yview)
            self.components['listbox'].config(yscrollcommand=self.components['scrollbar'].set)
    
    
    def layout(self):
        #self.components['lb3_1'].place(anchor="center", relx=0.42, rely=0.380)
        self.components['et3'].place(anchor="center", relx=0.5, rely=0.3)
        self.components['lbtitle'].place(anchor="center", relx=0.5, rely=0.2)
        self.components['lb3_4'].place(anchor="center", relx=0.5, rely=0.425)
        self.components['listbox_frame'].place(anchor="center", relx=0.5, rely=0.55) 
        self.components['bt3'].place(anchor = "center", relx= 0.5, rely = 0.8)
        self.components['listbox'].pack(side="left", fill="y")
        self.components['scrollbar'].pack(side="right", fill="y")
    

 
    def show(self):
        self.components['et3'].delete(0, tk.END)
        self.layout()
        self.components['listbox'].config(listvariable=tk.StringVar(value= self.name_list))



    def hide(self):
        for _, item in self.components.items():
            item.place_forget()
        
            
    def get_result(self):
        name = self.components['et3'].get()
        return name
    
    def set_name_list(self, name_list):
        self.name_list = name_list.copy()
    
    def clear_name_list(self):
        self.name_list = []



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