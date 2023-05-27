# restaurant
# 修改自維哲的 time-table.py

# 還沒：「放餐廳首圖」、「餐廳名加連結」

class RestaurantPage:
    def __init__(self, win):
        self.win = win
        self.checkboxes = []  # 儲存複選框的列表
        self.selected_boxes = []  # 儲存選中複選框的值的列表

    def checkbox_clicked(self, checkbox_value):
        # 複選框點擊事件處理函數
        if checkbox_value in self.selected_boxes:
            self.selected_boxes.remove(checkbox_value)
        else:
            self.selected_boxes.append(checkbox_value)

    def get_selected_values(self):
        restaurant_list = ['新生南路麥當勞','順園小館','辛殿公館店','鍋in','貳樓公館店']

        # 獲取選中複選框的值
        selected_values = []
        for checkbox_value in self.selected_boxes:
            # selected_values.append(checkbox_value)
            selected_values.append(restaurant_list[checkbox_value - 1])
        print("Selected values:", selected_values)

    def create_checkboxes(self):
        # 生成時間段列表
        restaurant_list = ['新生南路麥當勞','順園小館','辛殿公館店','鍋in','貳樓公館店']
        for i in range(5):
            row = []
            for j in range(1):
                checkbox_value = i + 1  # 計算複選框對應的值
                checkbox = tk.Checkbutton(self.win, text=restaurant_list[checkbox_value-1], command=lambda value=checkbox_value: self.checkbox_clicked(value))
                checkbox.place(x=20, y=30 + i * 30)  # 將複選框放置到指定的行和列
                row.append(checkbox)
            self.checkboxes.append(row)

    def create_bt(self):
        # 創建按鈕
        self.bt5 = tk.Button(self.win, text='Save Selected', command=lambda :(self.get_selected_values(), self.conceal()))
        self.bt5.place(x=20, y=200)  # 將按鈕放置到指定的行和列
        
    def create_menu(self):
        # 創建菜單超連結
        links = [
    {"text": "新生南路麥當勞", "url": "https://www.mcdonalds.com/tw/zh-tw/full-menu/extra-value-meals.html"},
    {"text": "順園小館", "url": "https://www.facebook.com/media/set/?set=a.2412078992198401&type=3"},
    {"text": "辛殿公館店", "url": "https://inline.app/booking/-LDKPhTT6bNhwjRVHpC2/-MWbDrcVGUuDMkYvCrz7"},
    {"text": "鍋in", "url": "https://images.app.goo.gl/2kgAHR8RuKyQtQ118"},
    {"text": "貳樓公館店", "url": "https://www.secondfloorcafe.com/menu/"}]
        for i, link in enumerate(links):
            label = tk.Label(win1, text=link["text"], fg="black", cursor="hand2", bg='#f2d5a3', font=('Arial', 12,"bold"), width=23, height=2)
            label.place(x=200, y=60 + i * 30)
            label.bind("<Button-1>", lambda e, url=link["url"]: webbrowser.open_new(url))

    def create_label(self):
        # 創建label
        menulabel = tk.Label(win1, text="點選餐廳看菜單！",fg='black', bg='#f2d5a3', font=('Arial', 20,"bold"), width=23, height=2)
        menulabel.place(x=150 , y=10)

    def show(self):
        self.create_checkboxes()
        self.create_bt()
        self.create_menu()
        self.create_label()
    
    def conceal(self):
        for row in self.checkboxes:
            for box in row:
                box.place_forget()
        
        self.bt5.place_forget()

if __name__ == '__main__':
    import tkinter as tk
    import webbrowser
    win1 = tk.Tk()
    win1.geometry('720x720')
    win1.title('一起聚餐吧')
    
    win1.configure(bg='#f2d5a3')
    page = RestaurantPage(win1)
    page.show()

    win1.mainloop()

