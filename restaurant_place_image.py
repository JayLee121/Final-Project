import tkinter as tk
import webbrowser
from PIL import Image, ImageTk

class RestaurantPage:
    def __init__(self, win):
        self.win = win
        self.checkboxes = []  # 儲存複選框的列表
        self.selected_boxes = []  # 儲存選中複選框的值的列表
        self.images = []

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
                checkbox.place(x=20, y=60 + i * 110)  # 將複選框放置到指定的行和列
                row.append(checkbox)
            self.checkboxes.append(row)

    def create_bt(self):
        # 創建按鈕
        self.bt5 = tk.Button(self.win, text='Save Selected', command=lambda :(self.get_selected_values(), self.conceal()))
        self.bt5.place(x=20, y=650)  # 將按鈕放置到指定的行和列

    def load_images(self):
        #image_paths = ["餐廳首圖_麥當勞(780x585).jpeg", "餐廳首圖_順園(4000 x 2925).webp", "餐廳首圖_辛殿(2280 x912).webp", "餐廳首圖_鍋in(600x600).jpeg", "餐廳首圖_貳樓(1920x1280).jpeg"]
        image_paths = ["餐廳首圖_麥當勞.jpg", "餐廳首圖_順園.jpg", "餐廳首圖_辛殿.jpg", "餐廳首圖_鍋in.jpg", "餐廳首圖_貳樓.jpg"]
        for path in image_paths:
            image = Image.open(path)
            image = self.resize_and_crop_image(image)
            self.images.append(ImageTk.PhotoImage(image))

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
            label.place(x=400, y=60 + i * 110)

    def create_menu(self):
        # 創建菜單超連結
        links = [
            {"text": "新生南路麥當勞", "url": "https://www.mcdonalds.com/tw/zh-tw/full-menu/extra-value-meals.html"},
            {"text": "順園小館", "url": "https://www.facebook.com/media/set/?set=a.2412078992198401&type=3"},
            {"text": "辛殿公館店", "url": "https://inline.app/booking/-LDKPhTT6bNhwjRVHpC2/-MWbDrcVGUuDMkYvCrz7"},
            {"text": "鍋in", "url": "https://images.app.goo.gl/2kgAHR8RuKyQtQ118"},
            {"text": "貳樓公館店", "url": "https://www.secondfloorcafe.com/menu/"}]
        for i, link in enumerate(links):
            label = tk.Label(self.win, text=link["text"], fg="black", cursor="hand2", bg='#f2d5a3', font=('Arial', 12,"bold"), width=23, height=2)
            label.place(x=200, y=60 + i * 110)
            label.bind("<Button-1>", lambda e, url=link["url"]: webbrowser.open_new(url))

    def create_label(self):
        # 創建label
        menulabel = tk.Label(self.win, text="點選餐廳看菜單！", fg='black', bg='#f2d5a3', font=('Arial', 20,"bold"), width=23, height=2)
        menulabel.place(x=150 , y=10)

    def show(self):
        self.create_checkboxes()
        self.create_bt()
        self.load_images()
        self.display_images()
        self.create_menu()
        self.create_label()

    def conceal(self):
        for row in self.checkboxes:
            for box in row:
                box.place_forget()

        self.bt5.place_forget()

if __name__ == '__main__':
    win1 = tk.Tk()
    win1.geometry('720x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')

    page = RestaurantPage(win1)
    page.show()

    win1.mainloop()
