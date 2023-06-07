# Back_end
debug = False
time_proportion, restaurant_proportion = 2/3, 1/3

    # 取得每個時間的投票情況（處理前端傳進來的資料）
def get_time_votes(time_p, name_p):
    time_dict = {}
    for i in range(len(name_p)):
        user_name = name_p[i]
        for time in time_p[i]:
                if time not in time_dict: time_dict[time] = [user_name]
                else: time_dict[time].append(user_name)
    return time_dict

    # 取得每個餐廳的投票情況 （處理前端傳進來的資料）           
def get_restaurant_votes(name_p, site_p):
    res_data_dict = {1: '新生南路麥當勞',2: '順園小館',3: '辛殿公館店',4: '鍋in',5: '貳樓公館店'}
    restaurant_dict = {}
    for i in range(len(name_p)):
        user_name = name_p[i]
        for site in site_p[i]:
                restaurant = res_data_dict[site]
                if restaurant not in restaurant_dict: restaurant_dict[restaurant] = [user_name]
                else: restaurant_dict[restaurant].append(user_name)
    return restaurant_dict

    # 查詢在指定日期以及時間(user選擇的）有營業的餐廳
def query_restaurants(time_p, day):
    bus_hour = {}  # business_hour
    bus_hour['新生南路麥當勞'] = [[15, 45]]
    if day == 6 or day == 7:
        bus_hour['順園小館'] = [[23, 29], [35, 42]]
    else: bus_hour['順園小館'] = [[23,28], [35, 42]]
    bus_hour['辛殿公館店'] = [[1, 3], [24, 48]]
    bus_hour['鍋in'] = [[23, 48]]
    if day == 6 or day == 7 : bus_hour['貳樓公館店'] = [[19, 43]]
    else: bus_hour['貳樓公館店'] = [[21, 42]]
    open_restaurants = {}
    for restaurant, hours in bus_hour.items():
        for time in time_p:
            for hour_range in hours:
                if hour_range[0] <= time <= hour_range[1]:
                    if time not in open_restaurants.keys():open_restaurants[time] = [restaurant]
                    else:open_restaurants[time].append(restaurant)
    return open_restaurants
    
    # 建議聚餐時間和餐廳
def suggest_party(day, time_p, name_p, site_p):
    total_people = len(name_p)
    all_time_users = get_time_votes(time_p, name_p)
    if debug:print('all_time_users:', all_time_users)
    
    # 產生最佳時間(opt_time)
    time_vote, opt_time = [], []
    find_opt_time = True
    for key in all_time_users.keys():
        num = len(all_time_users[key])
        if num >= total_people * time_proportion: time_vote.append([key,num])
    if len(time_vote) == 0 : find_opt_time = False
    else:
        time_vote.sort(key=lambda x: x[1], reverse=True)
        opt_time.append(time_vote[0][0])
        most_time_vote = time_vote[0][1]
        for i in range (1, len(time_vote)):
            # 判斷是否有同樣票數的時間
            if time_vote[i][1] == most_time_vote: opt_time.append(time_vote[i][0])

    restaurants_candidates = query_restaurants(opt_time, day)
    if debug:print('restaurants_candidates:', restaurants_candidates)
    all_restaurant_users = get_restaurant_votes(name_p, site_p)
    if debug: print('all_restaurant_users:', all_restaurant_users)

    # 計算最佳餐廳，以及將最佳時間，最佳餐廳，以及參與者放入 time_rest_name 裡
    # (最佳餐廳是由會參加的人中選擇出來的，並不是所有人)
    time_rest_name =[]
    for time in opt_time: # (opt_time)[1,2,3,....]
        user_list = all_time_users[time] # all_time_users = dict{time:[users]}
        restaurant_num_vote = []
        for restaurant in restaurants_candidates[time]: # restaurants_candidates = dict{time:[有營業的餐廳]}

            if restaurant in all_restaurant_users:
                restaurant_users_vote = len(all_restaurant_users[restaurant])
                if restaurant_users_vote >= most_time_vote * restaurant_proportion: restaurant_num_vote.append([restaurant, restaurant_users_vote])
                else:continue

        restaurant_num_vote.sort(key = lambda x: x[1], reverse = True)
        restaurant_list = []
        for i in range (len(restaurant_num_vote)):
                if restaurant_num_vote[i][1] == restaurant_num_vote[0][1]:restaurant_list.append(restaurant_num_vote[i][0])
        time_rest_name.append([time, restaurant_list, user_list])

    return time_rest_name


time_data = {1: '00:00-00:30', 2: '00:30-01:00', 3: '01:00-01:30', 4: '01:30-02:00',
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

    # 判斷time_rest_name的時間是否有連續，有的話合併
def merge_time(data):
    data = [[[item[0]], item[1], item[2]] for item in data]
    new = []
    time_rest_name = None

    for row in data:
        time = row[0][0]
        users_name = row[2]
        if time_rest_name is None or (time != time_rest_name[0][-1] + 1 or users_name != time_rest_name[2]):
            time_rest_name = [[row[0][0], row[0][0]], row[1], row[2]]
            new.append(time_rest_name)
        else:time_rest_name[0][-1] = row[0][0]

    # 將格式改為前端要的([[time,[restaurant1,...], [name1,nmae2..]].....])
    result = [[time_data[row[0][0]].split('-')[0] + "-" + time_data[row[0][-1]].split('-')[1], row[1], row[2]] for row in new]
    for item in result:
        item[1] = ','.join(item[1])  
        item[2] = ','.join(item[2])  
    return result


