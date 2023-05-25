# -*- coding: utf-8 -*-

import tkinter as tk

root = tk.Tk()

class MainPage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root)  # 建立主頁面的Frame元件
        self.page.pack()  # 將主頁面的Frame元件放置於視窗中
        
        self.label = tk.Label(self.page, text=u'這是主頁')  # 文字視窗
        self.label.pack(pady=10)  # 將文字視窗放置於主頁面的Frame元件中並設定垂直間距
        
        self.button = tk.Button(self.page, text=u'跳頁', command=self.switch_to_second_page)  # 按鈕
        self.button.pack(pady=10)  # 將按鈕放置於主頁面的Frame元件中並設定垂直間距

    def switch_to_second_page(self):
        self.page.destroy()  # 銷毀主頁面的Frame元件
        SecondPage(self.root)  # 建立並顯示第二頁面
    
  
class SecondPage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root)  # 建立第二頁面的Frame元件
        self.page.pack()  # 將第二頁面的Frame元件放置於視窗中
        
        self.label = tk.Label(self.page, text=u'這是第二頁')  # 文字視窗
        self.label.pack(pady=10)  # 將文字視窗放置於第二頁面的Frame元件中並設定垂直間距
        
        self.button = tk.Button(self.page, text=u'主頁', command=self.switch_to_main_page)  # 按鈕
        self.button.pack(pady=10)  # 將按鈕放置於第二頁面的Frame元件中並設定垂直間距
        
    def switch_to_main_page(self):
        self.page.destroy()  # 銷毀第二頁面的Frame元件
        MainPage(self.root)  # 建立並顯示主頁面    
        
MainPage(root)  # 建立並顯示主頁面
root.mainloop()  # 啟動主迴圈，等待事件處理

