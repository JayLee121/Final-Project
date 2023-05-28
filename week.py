import tkinter as tk

class TimePage:
    def __init__(self, win, cb):
        self.win = win
        self.cb = cb
        self.radiobuttons = []  # 儲存單選按鈕的列表
        self.selected_value = tk.StringVar(value=None)  # 儲存選中按鈕的值
        self.components = {
            'bt': tk.Button(win, text='Save Selected', bg='#f2d5a3', command=self.cb),
            'lb': tk.Label(win, text='\\  請點選聚餐的時間  /', font=('Arial', 30), bg='#f2d5a3'),
        }

    def layout(self):
        self.components['bt'].place(anchor="center", x=600, y=600)


    def get_result(self):
        # 獲取選中按鈕的值
        return self.selected_value.get()

    def create_radiobuttons(self):
        # 生成時間段列表
        time_list = ['週一', '週二', '週三', '週四', '週五', '週六', '週日']
        for i in range(7):
            value = i + 1
            radiobutton = tk.Radiobutton(
                self.win,
                text=time_list[i],
                bg='#f2d5a3',
                font=('Arial', 16),
                variable=self.selected_value,
                value=value,
            )
            radiobutton.place(relx=0.2 + 0.1 * i, rely=0.285 + 0.05 * 3)  # 相對座標

            self.radiobuttons.append(radiobutton)
            self.selected_value.set(None)
    def show(self):
        for _, item in self.components.items():
            item.place(anchor="center", relx=0.5, rely=0.75)
        self.components['lb'].place(anchor="center", relx=0.5, rely=0.2)
        self.create_radiobuttons()

    def hide(self):
        for button in self.radiobuttons:
            button.place_forget()
        self.components['bt'].place_forget()
        self.components['lb'].place_forget()

if _name_ == '_main_':
    win = tk.Tk()
    win.geometry('1280x720')
    win.title('一起聚餐吧')
    win.configure(bg='#f2d5a3')

    def save_selected():
        selected_value = page.get_result()
        print('Selected value:', selected_value)

    page = TimePage(win, save_selected)
    page.show()
    win.mainloop()