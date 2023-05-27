# 一開始先import前端傳入的東西


# import Algorithm
from Algorithm.py import filter_proportion
from Algorithm.py import find_optimal
from Algorithm.py import match

# try
name_p = ['Amber', 'Steve', 'Jay']
time_p = [[25, 26, 27, 34, 35, 36], [28, 29, 39, 40], [24]]
site_p = [['麥當勞', '順園'], ['貳樓', '鍋in'] , ['辛殿']]


def get_time_dict(time_p, name_p):
    time_dict = {}
    for i in time_p:
        for time in i:
            if time_p[i][j] not in time_dict:
                time_dict[time_p[i][j]] = []
                time_dict[time_p[i][j]].append(name_p[i])
            else:
                time_dict[time_p[i][j]].append(name_p[i])
    return time_dict

def get_site_dict(site_p, name_p):
    site_dict = {}
    site_dict = {}
    for i in site_p:
        for site in i:
            if site_p[i][j] not in site_dict:
                site_dict[site_p[i][j]] = []
                site_dict[site_p[i][j]].append(name_p[i])
            else:
                site_dict[site_p[i][j]].append(name_p[i])
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


