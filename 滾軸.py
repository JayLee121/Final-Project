import tkinter as tk
#  滾動條滾動事件的處理函式
def on_mousewheel(event):
    # 使用 event.delta 取得滾動的值，並將其除以 120 來得到滾動的單位數
    # 在大部分滑鼠上，每次滾動一個單位的值約為 120
    scroll_units = int(event.delta/120)
    # 以負值乘上滾動單位數，使滾動方向與滾輪滾動方向一致
    # 使用 canvas.yview_scroll 方法將畫布垂直滾動
    canvas.yview_scroll(-1 * scroll_units, "units")

# 創建主窗口
root = tk.Tk()
root.title('一起聚餐吧')
root.geometry('600x600')

frame = tk.Frame(root, width=200, height=300)    # 使用 frame 裝載 Canvas
frame.pack()

# 設定 Canvas
canvas = tk.Canvas(frame, width=200, height=300, bg='#fff', scrollregion=(0,0,400,400))

canvas.create_rectangle(120, 10, 170, 100, width=8, fill='#f00')   # 在 Canvas 裡畫矩形

scrollY = tk.Scrollbar(frame, orient='vertical')     # 垂直捲軸放在 frame 裡
scrollY.pack(side='right', fill='y')                 # 放在右邊填滿 y 軸
scrollY.config(command=canvas.yview)                 # 綁定 Canvas y 方向

canvas.config(yscrollcommand=scrollY.set)  # Canvas 綁定捲軸
canvas.pack(side='left')                             # Canvas 放在 frame 中的左側

# 綁定滑鼠滾動事件
root.bind("<MouseWheel>", on_mousewheel)

root.mainloop()
