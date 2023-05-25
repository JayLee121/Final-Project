import tkinter as tk

def click_count(button_value):
    global check
    check = button_value
    if button_value:
        var.set("True")
    else:
        var.set("False")

win = tk.Tk()
win.geometry("200x150")
var = tk.StringVar()  # 定義字串類別變數
var.set("False")  # 設定初始值
label = tk.Label(win, textvariable=var)  # 將字串類別變數綁定到標籤內容
label.pack()

button_1 = tk.Button(text="True", command=lambda: click_count(True))  # 綁定匿名函式
button_1.pack()
button_2 = tk.Button(text="False", command=lambda: click_count(False))  # 綁定匿名函式
button_2.pack()

win.mainloop()

print(check)  # 印出 check 變數的值
