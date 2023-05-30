import tkinter as tk
import webbrowser
from PIL import Image, ImageTk

class RestaurantPage:
    def __init__(self, win, cb, over):
        self.win = win
        self.cb = cb
        self.over = over
        self.checkboxes = []  # 儲存複選框的列表
        self.selected_boxes = []  # 儲存選中複選框的值的列表
        self.images = []
        self.labels = []  # 儲存超連結菜單的列表
        self.image_labels = []  # 儲存圖片的列表
        self.components = {'bt5':tk.Button(self.win, text='下一位', font=('Arial', 16), width=20,
                                height=2, activebackground='black', activeforeground='yellow', command=self.cb),
                           'bt6':tk.Button(self.win, text='產生結果', font=('Arial', 16), width=20,
                                height=2, activebackground='black', activeforeground='yellow', command=self.over),
                           'lbtitle':tk.Label(self.win, text='\\   點餐廳名看菜單  /', fg='black', bg='#f2d5a3', font=('Arial', 30, "bold")),
                           }
        self.links = [
            {"text": "新生南路麥當勞", "url": "https://www.mcdonalds.com/tw/zh-tw/full-menu/extra-value-meals.html"},
            {"text": "順園小館", "url": "https://www.facebook.com/media/set/?set=a.2412078992198401&type=3"},
            {"text": "辛殿公館店", "url": "https://inline.app/booking/-LDKPhTT6bNhwjRVHpC2/-MWbDrcVGUuDMkYvCrz7"},
            {"text": "鍋in", "url": "https://images.app.goo.gl/2kgAHR8RuKyQtQ118"},
            {"text": "貳樓公館店", "url": "https://www.secondfloorcafe.com/menu/"}]
        
        self.load_images()
    
    def load_images(self):
        image_paths = ["餐廳首圖_麥當勞.jpg", "餐廳首圖_順園.jpg", "餐廳首圖_辛殿.jpg", "餐廳首圖_鍋in.jpg", "餐廳首圖_貳樓.jpg"]
        for path in image_paths:
            image = Image.open(path)
            image = self.resize_and_crop_image(image)
            self.images.append(ImageTk.PhotoImage(image))
    
    def checkbox_clicked(self, checkbox_value):
        # 複選框點擊事件處理函數
        if checkbox_value in self.selected_boxes:
            self.selected_boxes.remove(checkbox_value)
        else:
            self.selected_boxes.append(checkbox_value)
                    
    def create_checkboxes(self):
        # 生成餐廳列表
        restaurant_list = ['新生南路麥當勞','順園小館','辛殿公館店','鍋in','貳樓公館店']
        for i in range(5):
            row = []
            for j in range(1):
                checkbox_value = i + 1  # 計算複選框對應的值
                checkbox = tk.Checkbutton(self.win, text=restaurant_list[checkbox_value-1], font=('Arial', 16), command=lambda value=checkbox_value: self.checkbox_clicked(value))
                checkbox.place(relx=0.25, rely=0.15 + i * 0.14)  # 將複選框放置到指定的行和列
                row.append(checkbox)
            self.checkboxes.append(row)

    def layout(self):
        self.components['lbtitle'].place(relx=0.5, rely=0.1, anchor='center')
        self.components['bt5'].place(relx=0.4, rely=0.9, anchor='center')
        self.components['bt6'].place(relx=0.6, rely=0.9, anchor='center')
        self.create_checkboxes()
    


    def resize_and_crop_image(self, image):
        new_width = 160
        width_ratio = new_width / image.width
        new_height = int(image.height * width_ratio)
        image = image.resize((new_width, new_height))

        crop_width = 160
        crop_height = 90
        crop_x = (new_width - crop_width) // 2
        crop_y = (new_height - crop_height) // 2
        image = image.crop((crop_x, crop_y, crop_x + crop_width, crop_y + crop_height))

        return image

    def display_images(self):
        for i, image in enumerate(self.images):
            label = tk.Label(self.win, image=image)
            label.place(relx=0.63, rely=0.15 + i * 0.14)
            self.image_labels.append(label)

    def create_menu(self):
        # 創建菜單超連結
        for i, link in enumerate(self.links):
            label = tk.Label(self.win, text=link["text"], fg="black", cursor="hand2", bg='#f2d5a3', font=('Arial', 16, "bold"))
            label.place(relx=0.45, rely=0.15 + i * 0.14)
            label.bind("<Button-1>", lambda e, url=link["url"]: webbrowser.open_new(url))
            self.labels.append(label)
    
    def get_selected_values(self):
        restaurant_list = ['新生南路麥當勞','順園小館','辛殿公館店','鍋in','貳樓公館店']
        # 獲取選中複選框的值
        selected_values = []
        if len(self.selected_boxes) != 0:
            for checkbox_value in self.selected_boxes:
                selected_values.append(checkbox_value)
 
        return selected_values
            
    def show(self):
        self.create_checkboxes()
        self.display_images()
        self.create_menu()
        self.layout()


    def hide(self):
        for row in self.checkboxes:
            for box in row:
                box.place_forget()
        
        for label in self.labels:
            label.place_forget()

        for image_label in self.image_labels:
            image_label.place_forget()
        
        for _, item in self.components.items():
            item.place_forget()




if __name__ == '__main__':
    win1 = tk.Tk()
    win1.geometry('720x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')

    def cb():
        page.hide()
        page.get_selected_values()
        print(page.get_selected_values())
    def rest_over():
        page.hide()

    page = RestaurantPage(win1, cb, rest_over)
    page.show()

    win1.mainloop()