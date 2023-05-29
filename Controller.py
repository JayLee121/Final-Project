# Controller
import home_page, user_name, time_table, restaurant_place_image, week, result
import tkinter as tk

name_list = []
available_time = []
rest_list = []
rs_list = []

def home_cb():
    home.hide()
    weekpg.show()
    print('home_cb')

def weekpg_cb():
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
    print('available_time:',available_time)
    print('name_list:', name_list)
    
def rest_cb():
    
    rest_list.append(rest.get_selected_values())
    rest.hide()
    name.set_name_list(name_list)
    name.show()
    print('rest_list:',rest_list)

def rest_over():
    rest.hide()
    resultpg.show()

def resultpg_cb():
    resultpg.hide()
    home.show()




if __name__ == '__main__':
    win = tk.Tk()
    win.geometry('1280x720')
    win.title('一起聚餐吧')
    win.configure(bg='#f2d5a3')
    frame = tk.Frame(win, width=15)
    frame.grid(row=0, column=0)

    home = home_page.HomePage(win, home_cb)
    weekpg = week.WeekPage(win, weekpg_cb)
    name = user_name.UserName(win, name_cb)
    resultpg = result.ResultPage(win, resultpg_cb, rs_list)

    home.show()
    win.mainloop()