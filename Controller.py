# Controller
import home_page, user_name, time_table, restaurant_place_image
import tkinter as tk

name_list = []
available_time = []

def p1_cb():
    p1.hide()
    p2.show()
    print('p1_cb')

def p2_cb():
    p2.hide()
    p3.show()
    name_list.append(p2.get_result())
    print(name_list)
def p3_cb():
    p3.hide()
    p4.show()
    available_time.append(p3.get_result())
    print(available_time)
    print(name_list)
    
def p4_cb():
    p4.hide()
    p2.show()
    
def p4_over():
    p4.hide()


if __name__ == '__main__':
    win = tk.Tk()
    win.geometry('1280x720')
    win.title('一起聚餐吧')
    win.configure(bg='#f2d5a3')
    frame = tk.Frame(win, width=15)
    frame.grid(row=0, column=0)
    # 還在想 name_list 要怎麼不傳入name_list 但仍可work    
    p1 = home_page.HomePage(win, p1_cb)
    p2 = user_name.UserName(win, p2_cb, frame, name_list)
    p3 = time_table.TimePage(win, p3_cb)
    p4 = restaurant_place_image.RestaurantPage(win, p4_cb, p4_over)
    p1.show()
    win.mainloop()