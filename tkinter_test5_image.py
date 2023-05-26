# 顯示圖片（參考網址 https://steam.oxxostudio.tw/category/python/tkinter/photoimage.html）
# 執行程式前電腦中要先有菜單圖片且取名為 menu_鍋in.png

# 方法一：Label
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('鍋in菜單')
root.geometry('1300x1000')

img = Image.open('menu_鍋in.png')
img = img.resize((1228,600), Image.ANTIALIAS)  # 等比例調整圖片大小
tk_img = ImageTk.PhotoImage(img)

label = tk.Label(root, image=tk_img, width=1300, height=1000, anchor='center')  # 設定 anchor
label.pack()

root.mainloop()


'''
# 方法二：Canvas
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('鍋in菜單')
root.geometry('1300x1000')

img = Image.open('menu_鍋in.png')
img = img.resize((1228,600), Image.ANTIALIAS)  # 等比例調整圖片大小
tk_img = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root, width=1300, height=1000)  # 跟介面設定同大小即可
canvas.create_image(0, 0, anchor='nw', image=tk_img)   # 在 Canvas 中放入圖片、anchor可調圖片在畫布中的位置
canvas.pack()

root.mainloop()'''
