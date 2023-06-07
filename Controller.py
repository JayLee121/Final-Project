# Controller
import home_page, user_name, time_table, restaurant_place_image, week, result
import tkinter as tk
from PIL import Image, ImageTk
import back_end

debug = False
name_list = []
available_time = []
rest_list = []
result_list = []
day = None

def home_cb():
    home.hide()
    weekpg.show()
    if debug:print('home_cb')

def weekpg_cb():
    global day
    day = weekpg.get_result()
    name.set_name_list(name_list)
    weekpg.hide()
    name.show()

def name_cb():
    global time
    name.hide()
    time = time_table.TimePage(win, time_cb)
    time.show()
    name_list.append(name.get_result())


def time_cb():
    global rest
    time.hide()
    rest = restaurant_place_image.RestaurantPage(win, rest_cb, rest_over)
    rest.show()
    available_time.append(time.get_result())
    if debug:print('available_time:', available_time)
    if debug:print('name_list:', name_list)
    
def rest_cb():
    rest_list.append(rest.get_selected_values())
    rest.hide()
    name.set_name_list(name_list)
    name.show()
    if debug:print('rest_list:',rest_list)

def rest_over():
    global resultpg
    rest_list.append(rest.get_selected_values())
    rest.hide()
    result_list = back_end.merge_time(day, available_time , name_list, rest_list)
    resultpg = result.ResultPage(win, resultpg_cb, result_list)
    resultpg.show()
    if debug:print('rest_list:',rest_list)


def resultpg_cb():
    global name_list
    global available_time 
    global rest_list
    global result_list
    resultpg.hide()
    name_list = []
    available_time = []
    rest_list = []
    result_list = []
    home.show()






if __name__ == '__main__':
    win = tk.Tk()
    win.geometry('1280x720')
    win.title('一起聚餐吧')
    win.configure(bg='#f2d5a3')
    frame = tk.Frame(win, width=15)
    frame.grid(row=0, column=0)
    home = home_page.HomePage(win, home_cb)
    time = time_table.TimePage(win, time_cb)
    weekpg = week.WeekPage(win, weekpg_cb)
    name = user_name.UserName(win, name_cb)
    resultpg = result.ResultPage(win, resultpg_cb, result_list)

    """# 載入圖片並顯示在頁面上
    image = Image.open("底圖2.png")
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(win, image=photo)
    image_label.place(anchor="center", relx=0.5, rely=0.5)
    image_label.lower()"""
    # 載入圖片並顯示在頁面上
    image = Image.open("底圖2.png")
    # 取得視窗大小
    window_width, window_height = win.winfo_screenwidth(), win.winfo_screenheight()

    # 計算底圖等比例縮放後的大小
    image_width, image_height = image.size
    aspect_ratio = max(window_width / image_width, window_height / image_height)
    new_width = int(image_width * aspect_ratio)
    new_height = int(image_height * aspect_ratio)

    # 縮放底圖
    image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # 將圖片裁剪為視窗大小
    image = image.crop((0, 0, window_width, window_height))

    # 將圖片轉換為Tkinter的PhotoImage物件
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(win, image=photo)
    image_label.place(anchor="center", relx=0.5, rely=0.5)
    image_label.lower()

    home.show()
    win.mainloop()
    
print(result_list,'result_list')
