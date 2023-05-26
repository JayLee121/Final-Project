from tkinter import *
import webbrowser

def callback(url):
    webbrowser.open_new(url)

root = Tk()
link1 = Label(root, text="新生南路麥當勞", fg="blue", cursor="hand2")
link1.grid()
link1.bind("<Button-1>", lambda e: callback("https://reurl.cc/01oNN6"))

link2 = Label(root, text="順園小館", fg="blue", cursor="hand2")
link2.grid()
link2.bind("<Button-1>", lambda e: callback("https://www.facebook.com/ShunYuanXiaoGuan/"))

root.mainloop()