# Controller
import home_page, user_name, time_table, restaurant_place_image, week, result
import tkinter as tk
from PIL import Image, ImageTk

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
    result_list = algorithm (day,available_time , name_list, rest_list)
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

def algorithm (day ,time_p ,name_p ,site_p):
    restaurant_data_dict = {
        1: '麥當勞公館店',
        2: '順園小館',
        3: '辛殿',
        4: '鍋in',
        5: '貳樓'
    }






    def get_time_dict(time_p, name_p):
        '''產出key是時間字串 value是list裡面是人名的dict'''
        time_dict = {}
        for i in range(len(time_p)):
            for time in time_p[i]:
                if time not in time_dict:
                    time_dict[time] = []
                    time_dict[time].append(name_p[i])
                else:
                    time_dict[time].append(name_p[i])
        return time_dict


    def get_site_dict(site_p, name_p):
        '''產出key是人名 value是list裡面是餐廳的dict'''
        site_dict = {}
        for i in range(len(name_p)):
            site_dict[name_p[i]] = site_p[i]
        return site_dict


    def createList(r1, r2):
        b_hour = []
        while(r1 < r2 + 1):
            b_hour.append(r1)
            r1 += 1
        return b_hour


    def filter_proportion(x_dict, proportion, total_people):
        temp_x = []
        for key in x_dict.keys():
            num = len(x_dict[key])
            if num >= total_people * proportion: temp_x.append([key, num])
        print('tempx:',temp_x)
        return temp_x


    def find_optimal(temp_x):
        '''找出最佳值，以及判斷是否有複數個最佳值'''
        accept_x = (sorted(temp_x, key=lambda x:x[1], reverse=True))
        optimal_x = []
        optimal_x.append(accept_x[0][0])
        best_num_vote = accept_x[0][1]
        for i in range (1, len(accept_x)):
            if accept_x[i][1] == accept_x[0][1]: optimal_x.append(accept_x[i][0])
        print('best_num_vote', best_num_vote)
        return optimal_x


    def merged(result_list,time_data_dict):
        i = 0
        while True:
            try:
                if result_list[i][0][-5:] == result_list[i+1][0][0:5] and\
                result_list[i][1] == result_list[i+1][1] and\
                result_list[i][2] == result_list[i+1][2]:
                    result_list[i][0] = result_list[i][0][0:5]
                    result_list[i][0] += '-'
                    result_list[i][0] += result_list[i+1][0][-5:]
                else:
                    break
                result_list.pop(i+1)
            except IndexError:
                break
        return result_list


    def get_result_time(time_dict, total_people):
        result_list = []
        accept_time = filter_proportion(time_dict, time_proportion, total_people)
        if len(accept_time) == 0: return [['沒有能聚的時間']], []
        if debug: print('accept_time:', accept_time)
        optimal_time = find_optimal(accept_time)
        if debug: print('optimal_time:', optimal_time)
        
        if len(optimal_time) == 1:
            result_list.append([optimal_time[0]])
        else:
            for i in range(len(optimal_time)):
                result_list.append([])
                # 時間
                result_list[i].append(optimal_time[i])
        return result_list, optimal_time
        
    best_num_vote = 0
    def get_result_site(result_list, optimal_time, time_dict, site_dict, total_people, bus_hour_dict, time_data_dict):
        if result_list == [['沒有能聚的時間']]: return [['沒有能聚的時間', '']]
        site_vote = {}
        
        name_list = time_dict[optimal_time[0]]
        for name in name_list:
                site_list = site_dict[name]
                for site in site_list:
                    if site not in site_vote:
                        site_vote[site] = [name]
                    else:
                        site_vote[site].append(name)
        if debug: print('site_vote:', site_vote)
        accept_site = filter_proportion(site_vote, site_proportion, best_num_vote)  # 可接受的餐廳
        if debug: print('accept_site:', accept_site)

        # 只有一個最佳時間
        if len(optimal_time) == 1:
            key = [k for k, v in time_data_dict.items() if v == optimal_time[0]][0]
            while True:
                try:
                    restaurant_name = restaurant_data_dict[(accept_site[0][0])]
                    if key in bus_hour_dict[restaurant_name]:
                        break
                    else:
                        accept_site.pop(0)
                except IndexError:
                    result_list[0].append('想要的餐廳剛好都沒有在此時段營業，請考慮其他餐廳～')
                    return result_list
            restaurant_name = restaurant_data_dict[accept_site[0][0]]
            result_list[0].append( restaurant_name)
            for i in range(1, len(accept_site)):
                if accept_site[i][1] == accept_site[0][1]:
                    result_list[0][1] += ', '
                    restaurant_name = restaurant_data_dict[accept_site[i][0]]
                    result_list[0][1] += restaurant_name
            return result_list

        # 有多個最佳時間 
        else:
            for i in range(len(optimal_time)):
                key = [k for k, v in time_data_dict.items() if v == optimal_time[i]][0]
                for j in range(len(accept_site)):
                    restaurant_name = restaurant_data_dict[(accept_site[j][0])]
                    if key in bus_hour_dict[restaurant_name]:
                        if accept_site[j][1] == accept_site[0][1]:
                            restaurant_name = restaurant_data_dict[accept_site[j][0]]
                            result_list[i].append(restaurant_name)
                        for k in range(j+1, len(accept_site)):
                            if accept_site[k][1] == accept_site[0][1]:  # 票數與第一個餐廳的票數相同
                                result_list[i][1] += ', '
                                restaurant_name = restaurant_data_dict[accept_site[k][0]]
                                result_list[i][1] += restaurant_name
            
            
            for i in range(len(result_list)):
                if len(result_list[i]) == 1:
                    result_list[i].append('想要的餐廳剛好都沒有在此時段營業，請考慮其他餐廳～')
            return result_list
        
        
    def get_result_name(result_list, optimal_time, time_dict, site_dict, total_people, bus_hour_dict, time_data_dict):
        if result_list == [['沒有能聚的時間', '']]: return []
        
        # 只有一個最佳時間
        if len(optimal_time) == 1:
            if result_list[0][1] == '想要的餐廳剛好都沒有在此時段營業，請考慮其他餐廳～':
                result_list[0].append('')
            else:
                result_list[0].append(time_dict[optimal_time[0]][0])
                for i in range(1, len(time_dict[optimal_time[0]])):
                    result_list[0][2] += ', '
                    result_list[0][2] += time_dict[optimal_time[0]][i]
            return result_list
        
        # 有多個最佳時間
        else:
            for i in range(len(optimal_time)):
                if result_list[i][1] == '想要的餐廳剛好都沒有在此時段營業，請考慮其他餐廳～':
                    result_list[i].append('')
                else:
                    result_list[i].append(time_dict[optimal_time[0]][0])
                    for j in range(1, len(time_dict[optimal_time[0]])):
                        result_list[i][2] += ', '
                        result_list[i][2] += time_dict[optimal_time[0]][j]
            return result_list


    time_data_dict = {1: '00:00-00:30', 2: '00:30-01:00', 3: '01:00-01:30', 4: '01:30-02:00',
                5: '02:00-02:30', 6: '02:30-03:00', 7: '03:00-03:30', 8: '03:30-04:00',
                9: '04:00-04:30', 10: '04:30-05:00', 11: '05:00-05:30', 12: '05:30-06:00',
                13: '06:00-06:30', 14: '06:30-07:00', 15: '07:00-07:30', 16: '07:30-08:00',
                17: '08:00-08:30', 18: '08:30-09:00', 19: '09:00-09:30', 20: '09:30-10:00',
                21: '10:00-10:30', 22: '10:30-11:00', 23: '11:00-11:30', 24: '11:30-12:00',
                25: '12:00-12:30', 26: '12:30-13:00', 27: '13:00-13:30', 28: '13:30-14:00',
                29: '14:00-14:30', 30: '14:30-15:00', 31: '15:00-15:30', 32: '15:30-16:00',
                33: '16:00-16:30', 34: '16:30-17:00', 35: '17:00-17:30', 36: '17:30-18:00',
                37: '18:00-18:30', 38: '18:30-19:00', 39: '19:00-19:30', 40: '19:30-20:00',
                41: '20:00-20:30', 42: '20:30-21:00', 43: '21:00-21:30', 44: '21:30-22:00',
                45: '22:00-22:30', 46: '22:30-23:00', 47: '23:00-23:30', 48: '23:30-24:00'}
    # try these
    # 之後這四個資料由前端傳入
    
    # name_p = ['Amber', 'Steve', 'Jay']
    # name_p = ['123', '45678']
    # time_p = [[25, 26], [26, 25, 27], [26, 25, 27]]
    # time_p = [[14, 15, 21, 27, 28, 34, 40], [39, 34, 35, 23, 27]]
    # site_p = [['麥當勞公館店'], ['麥當勞公館店', '順園小館'] , ['辛殿']]





    debug = True
    time_proportion = 2/3
    site_proportion = 1/3

    for i in range(len(time_p)):
        for j in range(len(time_p[i])):
            time_p[i][j] = time_data_dict[time_p[i][j]]

    # 這一段會產生一個dict key是餐廳 values是list 裡面裝開放的時間(用數字表示)
    bus_hour_dict = {}  # business_hour
    bus_hour_dict['麥當勞公館店'] = createList(15, 45)
    if 4==  day:
        bus_hour_dict['順園小館'] = createList(23, 28)
        for time in createList(35, 42):
            bus_hour_dict['順園小館'].append(time)
    else: bus_hour_dict['順園小館'] = []
    bus_hour_dict['辛殿'] = createList(24, 28)
    bus_hour_dict['鍋in'] = createList(23, 48)
    if day==6 in day ==7 : bus_hour_dict['貳樓'] = createList(19, 43)
    else: bus_hour_dict['貳樓'] = createList(21, 43)

    total_people = len(name_p)
    time_dict = get_time_dict(time_p, name_p)
    site_dict = get_site_dict(site_p, name_p)
    result_list, optimal_time = get_result_time(time_dict, total_people)
    result_list = get_result_site(result_list, optimal_time, time_dict, site_dict, total_people, bus_hour_dict, time_data_dict)
    result_list = get_result_name(result_list, optimal_time, time_dict, site_dict, total_people, bus_hour_dict, time_data_dict)
    result_list = merged(result_list, time_data_dict)
    return result_list
    if debug: print('result_list:', result_list)









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
    resultpg = result.ResultPage(win, resultpg_cb, result_list)

    """# 載入圖片並顯示在頁面上
    image = Image.open("底圖2.png")
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(win, image=photo)
    image_label.place(anchor="center", relx=0.5, rely=0.5)
    image_label.lower()"""

    home.show()
    win.mainloop()
    
