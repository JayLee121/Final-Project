# Controller
import home_page, user_name, time_table, restaurant_place_image, week
import tkinter as tk

name_list = []
available_time = []

def home_cb():
    home.hide()

    weekpg.show()
    print('home_cb')

def weekpg_cb():
    weekpg.hide()
    name.show()

def name_cb():
    name.hide()
    time.show()
    name_list.append(name.get_result())

    print(name_list)
def time_cb():
    time.hide()
    rest.show()
    available_time.append(time.get_result())
    print(available_time)
    print(name_list)
    
def rest_cb():
    rest.hide()
    name.set_name_list(name_list)
    name.show()
    
def rest_over():
    rest.hide()


if __name__ == '__main__':
    win = tk.Tk()
    win.geometry('1280x720')
    win.title('一起聚餐吧')
    win.configure(bg='#f2d5a3')
    frame = tk.Frame(win, width=15)
    frame.grid(row=0, column=0)
    home = home_page.HomePage(win, home_cb)
    weekpg = week.WeekPage(win, weekpg_cb)
    name = user_name.UserName(win, name_cb, frame)
    time = time_table.TimePage(win, time_cb)
    rest = restaurant_place_image.RestaurantPage(win, rest_cb, rest_over)
    home.show()
    win.mainloop()