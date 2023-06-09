import tkinter as tk
from PIL import Image, ImageTk

class TimePage:
    def __init__(self, win, cb):
        self.win = win
        self.cb = cb
        self.time_frame=tk.Frame(win, bg='#f2d5a3',pady= 0, padx = 0)
        self.checkboxes = []  # 儲存複選框的列表
        self.selected_boxes = []  # 儲存選中複選框的值的列表
        
        # 建立元件
        self.components = {'lb':tk.Label(win, text='\\  請點選你有空的時間  /', font=('Arail', 30, 'bold'), bg='#f2d5a3'),
                            'bt': tk.Button(win, text='下一頁', bg='#e3d5ca', fg='black', font=('Arial', 16), width=20,
                                height=2, activebackground='black', activeforeground='yellow', command=self.cb),                            }

    # 設定所有元件在視窗的位置
    def layout(self):
        self.components['lb'].place(anchor="center", relx=0.5, rely=0.2)
        self.components['bt'].place(anchor="center", relx=0.5, rely=0.8)
        self.create_checkboxes()
        self.time_frame.place(relx=0.2,rely =0.3, relheight=0.35, relwidth=0.6)

    # check_box再次點擊，需要視為未勾選
    def checkbox_clicked(self, checkbox_value):
        if checkbox_value in self.selected_boxes:
            self.selected_boxes.remove(checkbox_value)
        else:
            self.selected_boxes.append(checkbox_value)

    # 獲取選中複選框的值
    def get_result(self):
        selected_values = []
        for checkbox_value in self.selected_boxes:
            selected_values.append(checkbox_value)
        return selected_values

    # 生成時間的check_box
    def create_checkboxes(self):
        time_list = [
            '00:00-00:30', '00:30-01:00', '01:00-01:30', '01:30-02:00', '02:00-02:30', '02:30-03:00', 
            '03:00-03:30', '03:30-04:00', '04:00-04:30', '04:30-05:00', '05:00-05:30', '05:30-06:00', 
            '06:00-06:30', '06:30-07:00', '07:00-07:30', '07:30-08:00', '08:00-08:30', '08:30-09:00', 
            '09:00-09:30', '09:30-10:00', '10:00-10:30', '10:30-11:00', '11:00-11:30', '11:30-12:00', 
            '12:00-12:30', '12:30-13:00', '13:00-13:30', '13:30-14:00', '14:00-14:30', '14:30-15:00', 
            '15:00-15:30', '15:30-16:00', '16:00-16:30', '16:30-17:00', '17:00-17:30', '17:30-18:00', 
            '18:00-18:30', '18:30-19:00', '19:00-19:30', '19:30-20:00', '20:00-20:30', '20:30-21:00', 
            '21:00-21:30', '21:30-22:00', '22:00-22:30', '22:30-23:00', '23:00-23:30', '23:00-24:00'
        ]
        for i in range(8):
            for j in range(6):
                checkbox_value = i * 6 + j + 1
                checkbox = tk.Checkbutton(self.time_frame, text=time_list[checkbox_value-1], bg='#f2d5a3', font=('Arial',16), command=lambda value=checkbox_value: self.checkbox_clicked(value))
                
                # 設置checkbox的位置
                checkbox.place(relx=0.16*j, rely=0.15*i)  # 相對座標

                self.checkboxes.append(checkbox)

    # 在視窗上顯示所有元件 
    def show(self):
        self.layout()

    # 在視窗上隱藏所有元件
    def hide(self):
        for _, item in self.components.items():
            item.place_forget()

        self.time_frame.place_forget()
        

# 為了讓頁面能夠單獨測試，且避免import時會執行以下程式碼
if __name__ == '__main__':
    win = tk.Tk()
    win.geometry('1280x720')
    win.title('一起聚餐吧')
    win.configure(bg='#f2d5a3')
    image = Image.open('/Users/jay/Documents/GitHub/Final-Project/'+ "底圖2.png")

    def save_selected():
        selected_values = page.get_result()
        print('Selected values:', selected_values)

    page = TimePage(win, lambda:(page.hide(), save_selected()))
    page.show()

    win.mainloop()