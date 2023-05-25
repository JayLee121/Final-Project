import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

class MainPage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root, width=400, height=400)
        self.page.pack_propagate(0)  # 禁止自動調整大小
        self.page.pack()

        # 載入圖片
        image = Image.open("C:/Users/a0955/Desktop/下載.jpg")
        # 調整圖片大小
        image = image.resize((300, 300), Image.ANTIALIAS)
        # 將圖片轉換為Tkinter的PhotoImage物件
        photo = ImageTk.PhotoImage(image)

        # 在頁面中顯示圖片
        self.label = tk.Label(self.page, image=photo)
        self.label.image = photo  # 保持對PhotoImage物件的引用，防止被垃圾回收
        self.label.place(relx=0.5, rely=0.55, anchor=tk.CENTER)  # 使用place()方法手動放置圖片

        self.button = tk.Button(self.page, text=u'切換視窗', command=self.switch_window, width=10, height=2)
        self.button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # 使用place()方法手動放置按鈕

    def switch_window(self):
        self.page.destroy()
        SecondPage(self.root)

class SecondPage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root, width=400, height=400)
        self.page.pack_propagate(0)  # 禁止自動調整大小
        self.page.pack()

        # 載入圖片
        image = Image.open("C:/Users/a0955/Desktop/風間.png")
        # 調整圖片大小
        image = image.resize((300, 300), Image.ANTIALIAS)
        # 將圖片轉換為Tkinter的PhotoImage物件
        photo = ImageTk.PhotoImage(image)

        # 在頁面中顯示圖片
        self.label = tk.Label(self.page, image=photo)
        self.label.image = photo  # 保持對PhotoImage物件的引用，防止被垃圾回收
        self.label.place(relx=0.5, rely=0.55, anchor=tk.CENTER)  # 使用place()方法手動放置圖片

        self.button = tk.Button(self.page, text=u'切換視窗', command=self.switch_window, width=10, height=2)
        self.button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # 使用place()方法手動放置按鈕

    def switch_window(self):
        self.page.destroy()
        MainPage(self.root)

MainPage(root)
root.mainloop()
