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
day = '星期二'
name_p = ['Amber', 'Steve', 'Jay']
time_p = [[25, 26, 27], [25, 26, 27], [25, 26, 27]]
site_p = [['麥當勞', '順園小館'], ['麥當勞', '順園小館'] , ['麥當勞', '順園小館']]

for i in range(len(time_p)):
    for j in range(len(time_p[i])):
        time_p[i][j] = time_data_dict[time_p[i][j]]

# 這一段會產生一個dict key是餐廳 values是list 裡面裝開放的時間(用數字表示)
bus_hour_dict = {}  # business_hour
bus_hour_dict['麥當勞公館店'] = createList(15, 45)
if '四' in day:
    bus_hour_dict['順園小館'] = createList(23, 28)
    for time in createList(35, 42):
        bus_hour_dict['順園小館'].append(time)
else: bus_hour_dict['順園小館'] = []
bus_hour_dict['辛殿'] = createList(24, 28)
bus_hour_dict['鍋in'] = createList(23, 48)
if '六' in day or '日' in day: bus_hour_dict['貳樓'] = createList(19, 43)
else: bus_hour_dict['貳樓'] = createList(21, 43)

total_people = len(name_p)
time_dict = get_time_dict(time_p, name_p)
site_dict = get_site_dict(site_p, name_p)
Algorithm.get_result(time_dict, site_dict, total_people)