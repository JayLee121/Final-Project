# 一開始先import前端傳入的東西

# try
name_p = ['Amber', 'Steve', 'Jay']
time_p = [[25, 26, 27, 34, 35, 36], [28, 29, 39, 40], [24]]
site_p = [['麥當勞', '順園'], ['貳樓', '鍋in'] , ['辛殿']]

debug = True
time_proportion = 1/2
site_proportion = 1/3
total_people = len(name_p)

def get_time_dict(time_p, name_p):
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
    site_dict = {}
    site_dict = {}
    for i in range(len(site_p)):
        for site in site_p[i]:
            if site not in site_dict:
                site_dict[site] = []
                site_dict[site].append(name_p[i])
            else:
                site_dict[site].append(name_p[i])
    return site_dict


time_data_dict = {'00:00': 1, '00:30': 2, '01:00': 3, '01:30': 4,
             '02:00': 5, '02:30':6, '03:00': 7, '03:30': 8,
             '04:00': 9, '04:30': 10, '05:00': 11, '05:30': 12,
             '06:00': 13, '06:30': 14, '07:00': 15,'07:30': 16,
             '08:00': 17, '08:30': 18, '09:00': 19, '09:30': 20,
             '10:00': 21, '10:30': 22, '11:00': 23, '11:30': 24,
             '12:00': 25, '12:30': 26, '13:00': 27, '13:30': 28,
             '14:00': 29, '14:30': 30, '15:00': 31, '15:30': 32,
             '16:00': 33, '16:30': 34, '17:00': 35, '17:30': 36,
             '18:00': 37, '18:30': 38, '19:00': 39, '19:30': 40,
             '20:00': 41, '20:30': 42, '21:00': 43, '21:30': 44,
             '22:00': 45, '22:30': 46, '23:00': 47, '23:30': 48,}


# 找出票數大於比例的 x_dict key:time or restaurant name / value :user's name 
def filter_proportion(x_dict, proportion):
    temp_x = []
    for key in x_dict.keys():
        num = len(x_dict[key])
        if num >= total_people * proportion:temp_x.append([key, num])
    return temp_x

# 找出最佳值，以及判斷是否有複數個最佳值
def find_optimal(temp_x):
    accept_x = (sorted(temp_x, key=lambda x:x[1], reverse=True))
    optimal_x = []
    optimal_x.append(accept_x[0][0])
    for i in range (1, len(accept_x)):
        if accept_x[i][0] == optimal_x[0]: optimal_x.append(accept_x[i][0])
    return optimal_x

def match(time_dict, site_dict):
    find_time, find_site = True, True
    # 可接受的時間
    accept_time = filter_proportion(time_dict, time_proportion)
    if len(accept_time) == 0: find_time = False
    if debug: print('accept_time:', accept_time)
    
    # 找出最佳的時間，並且判斷是否有複數個
    optimal_time = find_optimal(accept_time)
    if debug: print('optimal_time:', optimal_time)

    # 計算這些參加者投了哪些餐廳
    site_vote = dict()
    for time in optimal_time:
        name_list = time_dict[time]
        for name in name_list:
            site_list = site_dict[name]
            for site in site_list:
                if site not in site_vote:
                    site_vote[site] = [name]
                else:
                    site_vote[site].append(name)
    
    # 可接受的餐廳
    accept_site = filter_proportion(site_vote, site_proportion)
    if len(accept_site) == 0: find_site = False
    if debug: print('accept_site:', accept_site)

time_dict = get_time_dict(time_p, name_p)
site_dict = get_site_dict(site_p, name_p)
match(time_dict, site_dict)