# 一開始先import前端傳入的東西

import Algorithm


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


time_data_dict = {1: '00:00', 2: '00:30', 3: '01:00', 4: '01:30',
             5: '02:00', 6: '02:30', 7: '03:00', 8: '03:30',
             9: '04:00', 10: '04:30', 11: '05:00', 12: '05:30',
             13: '06:00', 14: '06:30', 15: '07:00', 16: '07:30',
             17: '08:00', 18: '08:30', 19: '09:00', 20: '09:30',
             21: '10:00', 22: '10:30', 23: '11:00', 24: '11:30',
             25: '12:00', 26: '12:30', 27: '13:00', 28: '13:30',
             29: '14:00', 30: '14:30', 31: '15:00', 32: '15:30',
             33: '16:00', 34: '16:30', 35: '17:00', 36: '17:30',
             37: '18:00', 38: '18:30', 39: '19:00', 40: '19:30',
             41: '20:00', 42: '20:30', 43: '21:00', 44: '21:30',
             45: '22:00', 46: '22:30', 47: '23:00', 48: '23:30'}

# try these
# 之後這三個資料由前端傳入 現在還缺星期幾
day = '星期二'
name_p = ['Amber', 'Steve', 'Jay']
time_p = [[25, 26, 27, 34, 35, 36], [28, 29, 39, 40], [25, 26, 27]]
site_p = [['麥當勞', '順園'], ['貳樓', '鍋in'] , ['辛殿']]

for i in range(len(time_p)):
    for j in range(len(time_p[i])):
        time_p[i][j] = time_data_dict[time_p[i][j]]

# 這一段會產生一個dict key是餐廳名稱 values是list裡面裝開放的時間(用數字表示)
bus_hour_dict = {}  # business_hour
bus_hour_dict['麥當勞'] = createList(15, 45)
if '四' in day:
    bus_hour_dict['順園'] = createList(23, 28)
    for time in createList(35, 42):
        bus_hour_dict['順園'].append(time)
else: bus_hour_dict['順園'] = []
bus_hour_dict['辛殿'] = createList(24, 28)
bus_hour_dict['鍋in'] = createList(23, 48)
if '六' in day or '日' in day: bus_hour_dict['貳樓'] = createList(19, 43)
else: bus_hour_dict['貳樓'] = createList(21, 43)

total_people = len(name_p)
time_dict = get_time_dict(time_p, name_p)
site_dict = get_site_dict(site_p, name_p)
Algorithm.match(time_dict, site_dict, total_people)