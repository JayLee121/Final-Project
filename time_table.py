# Time_table
import tkinter as tk

class TimePage:
    def __init__(self, win, cb):
        self.win = win
        self.cb = cb
        self.checkboxes = []  # 儲存複選框的列表
        self.selected_boxes = []  # 儲存選中複選框的值的列表
        self.components = {'bt': tk.Button(win, text='Save Selected', command=self.cb),
                            }

    
    def layout (self):
        self.components['bt'].grid(column=50, row=50)


    def checkbox_clicked(self, checkbox_value):
        # 複選框點擊事件處理函數
        if checkbox_value in self.selected_boxes:
            self.selected_boxes.remove(checkbox_value)
        else:
            self.selected_boxes.append(checkbox_value)
        
    def get_result(self):
        # 獲取選中複選框的值
        selected_values = []
        for checkbox_value in self.selected_boxes:
            selected_values.append(checkbox_value)
        return selected_values

    def create_checkboxes(self):
        # 生成時間段列表
        time_list=['00:00-00:30', '00:30-01:00', '01:00-01:30', '01:30-02:00', '02:00-02:30', '02:30-03:00', '03:00-03:30', '03:30-04:00', '04:00-04:30', '04:30-05:00', '05:00-05:30', '05:30-06:00', '06:00-06:30', '06:30-07:00', '07:00-07:30', '07:30-08:00', '08:00-08:30', '08:30-09:00', '09:00-09:30', '09:30-10:00', '10:00-10:30', '10:30-11:00', '11:00-11:30', '11:30-12:00', '12:00-12:30', '12:30-13:00', '13:00-13:30', '13:30-14:00', '14:00-14:30', '14:30-15:00', '15:00-15:30', '15:30-16:00', '16:00-16:30', '16:30-17:00', '17:00-17:30', '17:30-18:00', '18:00-18:30', '18:30-19:00', '19:00-19:30', '19:30-20:00', '20:00-20:30', '20:30-21:00', '21:00-21:30', '21:30-22:00', '22:00-22:30', '22:30-23:00', '23:00-23:30', '23:00-24:00']
        for i in range(8):
            row = []
            for j in range(6):
                checkbox_value = i * 6 + j + 1  # 計算複選框對應的值
                checkbox = tk.Checkbutton(self.win, text=time_list[checkbox_value-1], command=lambda value=checkbox_value: self.checkbox_clicked(value))
                checkbox.grid(row=i+3, column=j+3)  # 將複選框放置到指定的行和列
                row.append(checkbox)
            self.checkboxes.append(row)


    def show(self):
        for _, item in self.components.items():
            item.grid()
        self.create_checkboxes()
    
    def hide(self):
        for row in self.checkboxes:
            for box in row:
                box.grid_remove()
        
        for _, item in self.components.items():
            item.grid_remove()

if __name__ == '__main__':
    import tkinter as tk

    win = tk.Tk()
    win.geometry('1280x720')
    win.title('一起聚餐吧')
    
    win.configure(bg='#f2d5a3')
    page = TimePage(win, lambda:page.hide())
    page.show()

    win.mainloop()