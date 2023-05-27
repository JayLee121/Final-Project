# Controller
import home_page, user_name, time_table
import tkinter as tk

name_list = []
available_time = []

def p1_cb():
    p1.conceal()
    p2.show()
    print('p1_cb')

def p2_cb():
    p2.conceal()
    p3.show()
    name_list.append(p2.get_result())

def p3_cb():
    p3.conceal()
    available_time.append(p3.get_result())
    print(available_time)
    print(name_list)
    
if __name__ == '__main__':

    win = tk.Tk()
    win.geometry('1280x720')
    win.title('一起聚餐吧')
    win.configure(bg='#f2d5a3')
    p1 = home_page.HomePage(win,p1_cb)
    p2 = user_name.UserName(win,p2_cb)
    p3 = time_table.TimePage(win,p3_cb)

    p1.show()
    win.mainloop()