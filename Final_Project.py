# 一開始先import前端傳入的東西

def get_restaurant_data(資料.txt):
    data_dict = {}
    讀檔案進來並記在資料的字典  # key 是餐廳 value 是營業時間（半小時為單位）（資料處理）
    return data_dict

def read_user_restaurant(person, res_data):
    while True:
        res = 點擊的餐廳  # 把介面上的東西換成能用的輸入
        if res == '選取完畢'：  # 當他點到選取完畢就結束選取
            break
        if 餐廳資料裡面沒有「餐廳名稱」這個key:
            res_data[餐廳名稱] = [人名]
        if 沒有:
            res_data[餐廳名稱].append(人名)
    return res_data


def read_user_time(person, time_data):
    如同上面，只是把key改成時間（每半小時為單位）

    return time_data

def get_best_RandT(餐廳資料, 時間資料)

    input(使用者所選的時間以及餐廳)
    for each in 時間資料的key: count amount of value
sort number of votes
    從最佳時間內，找出可以的人。（把這些人名記錄下來）
    並且從可以的人中找出最佳的餐廳。（在判斷最佳餐廳時，只計算那些人名所投的餐廳）
    if 最佳餐廳都沒有營業：
        if 人數沒有小於一半
                    找第二高票的餐廳
                    以此類推

    if 最佳時間都沒有任何餐廳營業找第二高票的時間超過幾票？就選第三高票

    return 最佳餐廳跟最佳時間
==========================================
time_dict = {'11:00':  1, '11:30': 2, '12:00': 3, '12:30': 4, '13:00': 5, '13:30':6, '14:00': 7, '14:30': 8, '15:00': 9, '17:00': 10, '17:30': 11, '18:00': 12, '18:30': 13, '19:00': 14, '19:30': 15, '20:00': 16, '20:30': 17, '21:00': 18}

start = True if 按下start else False
if start:
    people_num = 請輸入聚餐總人數的那格輸入

    # 點擊想要的餐廳（現在先用兩個之後再增加）
    res_data = dict()
    time_data = dict() 
    for person in range(people_num):
        res_data = read_user_restaurant(person, res_data)
        time_data = read_user_time(person, time_data)
    get_best_RandT(res_data, time_data)
