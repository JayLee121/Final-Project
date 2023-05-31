def algorithm (day ,time_p ,name_p ,site_p):
    res_data_dict = {
        1: '新生南路麥當勞',
        2: '順園小館',
        3: '辛殿公館店',
        4: '鍋in',
        5: '貳樓公館店'
    }


    def get_time_dict(time_p, name_p):
        ''' 產出key是時間字串 
            value是list裡面是人名的dict'''

        time_dict = {}
        for i in range(len(time_p)):
            for time in time_p[i]:

                # 如果還沒有time這個key 創一個新的list並且丟進去
                if time not in time_dict:
                    time_dict[time] = []
                    time_dict[time].append(name_p[i])

                # 已經有了就直接丟進去
                else:
                    time_dict[time].append(name_p[i])
        return time_dict


    def get_site_dict(site_p, name_p):
        ''' 產出key是人名
            value是list裡面是餐廳的dict'''

        site_dict = {}
        for i in range(len(name_p)):
            site_dict[name_p[i]] = site_p[i]
        return site_dict


    def cr_bus(r1, r2):
        ''' 產生營業時間的list
            之後用來檢驗最佳時間是否在此內'''

        # 把介在r1跟r2的數字全部丟進b_hour
        b_hour = []
        while(r1 < r2 + 1):
            b_hour.append(r1)
            r1 += 1
        return b_hour


    def filter_prop(x_dict, prop, total_people):
        ''' 看（時間或是人數）是否過一定比例'''

        accept_x = []  # 可被接受的（時間或餐廳）
        for key in x_dict.keys():
            num = len(x_dict[key])
            if num >= total_people * prop: accept_x.append([key, num])  # 有過比例就加入accept_x
        return accept_x


    def find_opt(accept_x):
        ''' 從accept_x找出最佳值
            以及判斷是否有複數個最佳值'''

        accept_x = (sorted(accept_x, key=lambda x: x[1], reverse=True))
        opt_x = []
        opt_x.append(accept_x[0][0])  # 先加入最大的
        best_num_vote = accept_x[0][1]  # 記住他的人數
        for i in range (1, len(accept_x)):
            if accept_x[i][1] == accept_x[0][1]: opt_x.append(accept_x[i][0])  # 如果人數一樣就加入
        return opt_x


    def get_result_time(time_dict, total_people):
        ''' 產生result_list的第一步
            先產出最佳時間（可能一個或多個）
            如果多個的話就放在不同的list'''

        result_list = []
        accept_time = filter_prop(time_dict, time_prop, total_people)  # 可接受的時間
        if len(accept_time) == 0: return [['沒有能聚的時間']], []  # 沒有可以聚的時間 直接回傳
        if debug: print('accept_time:', accept_time)
        opt_time = find_opt(accept_time)  # 最佳時間
        if debug: print('opt_time:', opt_time)
        
        # 只有一個最佳時間 直接加到result_list
        if len(opt_time) == 1:
            result_list.append([opt_time[0]])

        # 有多個最佳時間 在result_list創多個list 分別加入
        else:
            for i in range(len(opt_time)):
                result_list.append([])
                result_list[i].append(opt_time[i])
        return result_list, opt_time


    def get_result_site(result_list, opt_time, time_dict, site_dict, total_people, bus_hour, time_data):
        ''' 產生result_list的第二步
            找出票數最高的餐廳（可能有多個）'''

        if result_list == [['沒有能聚的時間']]: return [['沒有能聚的時間', '']]  # 沒有能聚的時間 餐廳直接回傳空字串

        # 產出每個餐廳有哪些人投的dict
        site_vote = {}
        name_list = time_dict[opt_time[0]]
        for name in name_list:
                site_list = site_dict[name]
                for site in site_list:
                    if site not in site_vote:
                        site_vote[site] = [name]
                    else:
                        site_vote[site].append(name)
        # -------------------------------------------
        if debug: print('site_vote:', site_vote)
        best_num_vote = 0
        accept_site = filter_prop(site_vote, site_prop, best_num_vote)  # 可接受的餐廳
        if debug: print('accept_site:', accept_site)

        # 只有一個最佳時間
        if len(opt_time) == 1:
            key = [k for k, v in time_data.items() if v == opt_time[0]][0]  # 找到時間對應的key 為了做營業時間比對
            while True:
                ''' 檢查最佳時間是否營業 '''
                try:
                    res_name = res_data_dict[(accept_site[0][0])]  # 最多票餐廳的名字

                    # 如果在營業時間 檢驗完畢
                    if key in bus_hour[res_name]:
                        break

                    # 如果沒有 這個餐廳就不是最好的餐廳 刪掉
                    else:
                        accept_site.pop(0)
                # 如果拿光光了 就代表都沒開 直接return
                except IndexError:
                    result_list[0].append('想要的餐廳剛好都沒有在此時段營業，請考慮其他餐廳～')
                    return result_list

            # 將結果弄到result_list
            res_name = res_data_dict[accept_site[0][0]]
            result_list[0].append(res_name)  # 第一個先加進去
            for i in range(1, len(accept_site)):
                # 後面的如果票數一樣就加', 餐廳名'

                if accept_site[i][1] == accept_site[0][1]:
                    result_list[0][1] += ', '
                    res_name = res_data_dict[accept_site[i][0]]
                    result_list[0][1] += res_name
            # -------------------------------------------------
            return result_list

        # 有多個最佳時間 
        else:
            for i in range(len(opt_time)):
                ''' 每個最佳時間都要跑 所以要迴圈 '''

                key = [k for k, v in time_data.items() if v == opt_time[i]][0]  # 找到時間對應的key 為了做營業時間比對
                res_name = res_data_dict[(accept_site[0][0])]  # 最佳餐廳的名字

                # 如果有在營業時間 就開始加入
                if key in bus_hour[res_name]:
                    result_list[i].append(res_name)  # 第一個先加進去
                    for j in range(1, len(accept_site)):
                        # 後面的如果票數一樣就加', 餐廳名'

                        if accept_site[j][1] == accept_site[0][1]:
                            result_list[i][1] += ', '
                            res_name = res_data_dict[accept_site[j][0]]
                            result_list[i][1] += res_name

            # 如果都沒有餐廳加入 就是沒有符合營業時間
            for i in range(len(result_list)):
                if len(result_list[i]) == 1:
                    result_list[i].append('想要的餐廳剛好都沒有在此時段營業，請考慮其他餐廳～')
            return result_list


    def get_result_name(result_list, opt_time, time_dict):
        ''' 產生result_list的第三步：
            找出能出席的人'''
        if result_list == [['沒有能聚的時間', '']]: return []  # 沒有能聚的時間 人直接回傳空字串
        
        # 只有一個最佳時間
        if len(opt_time) == 1:

            # 如果餐廳沒有開 人直接回傳空字串
            if result_list[0][1] == '想要的餐廳剛好都沒有在此時段營業，請考慮其他餐廳～':
                result_list[0].append('')

            # 有開的話 就加入人
            else:
                result_list[0].append(time_dict[opt_time[0]][0])  # 第一個先加入
                for i in range(1, len(time_dict[opt_time[0]])):
                    # 後面的加', 名字'

                    result_list[0][2] += ', '
                    result_list[0][2] += time_dict[opt_time[0]][i]
            return result_list

        # 有多個最佳時間
        else:
            for i in range(len(opt_time)):

                # 如果餐廳沒有開 人直接回傳空字串
                if result_list[i][1] == '想要的餐廳剛好都沒有在此時段營業，請考慮其他餐廳～':
                    result_list[i].append('')

                # 有開的話 就加入人
                else:
                    result_list[i].append(time_dict[opt_time[0]][0])  # 第一個先加入
                    for j in range(1, len(time_dict[opt_time[0]])):
                        # 後面的加', 名字'

                        result_list[i][2] += ', '
                        result_list[i][2] += time_dict[opt_time[0]][j]
            return result_list


    def merged(result_list,time_data):
        ''' 最後一步：檢查是否有
            連續的時間（如11:00-11:30, 11:30-12:00)
            如果人都一樣就合併'''

        i = 0
        while True:
            try:
                ''' 條件的第一行：時間連續
                         第二行：餐廳一樣
                         第三行：人一樣'''
                if result_list[i][0][-5:] == result_list[i+1][0][0:5] and\
                result_list[i][1] == result_list[i+1][1] and\
                result_list[i][2] == result_list[i+1][2]:

                    '''改成連續'''
                    result_list[i][0] = result_list[i][0][0:5]
                    result_list[i][0] += '-'
                    result_list[i][0] += result_list[i+1][0][-5:]

                # 沒有連續就跳出迴圈
                else:
                    break
                result_list.pop(i+1)  # 把合併完沒用的時間（後面的）刪掉

            # 沒有下一個 跳出迴圈
            except IndexError:
                break
        return result_list

    # 由於前端傳進來的是數字 所以將數字和實際時間做對應 以便輸出
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
    # -------------------------------------------------------------------------------------
    debug = True
    time_prop = 2/3  # 時間接受的比例
    site_prop = 1/3  # 餐廳接受的比例

    # 把time_p 從數字改成字串
    for i in range(len(time_p)):
        for j in range(len(time_p[i])):
            time_p[i][j] = time_data[time_p[i][j]]

    # 這一段會產生一個dict key是餐廳 value是list 裡面裝開放的時間(用數字表示)
    bus_hour = {}  # business_hour
    bus_hour['新生南路麥當勞'] = cr_bus(15, 45)
    if 4 == day:
        bus_hour['順園小館'] = cr_bus(23, 28)
        for time in cr_bus(35, 42):
            bus_hour['順園小館'].append(time)
    else: bus_hour['順園小館'] = []
    bus_hour['辛殿公館店'] = cr_bus(24, 28)
    bus_hour['鍋in'] = cr_bus(23, 48)
    if day == 6 in day == 7 : bus_hour['貳樓公館店'] = cr_bus(19, 43)
    else: bus_hour['貳樓公館店'] = cr_bus(21, 43)
    # --------------------------------------------------------------

    total_people = len(name_p)
    time_dict = get_time_dict(time_p, name_p)
    site_dict = get_site_dict(site_p, name_p)
    result_list, opt_time = get_result_time(time_dict, total_people)
    result_list = get_result_site(result_list, opt_time, time_dict, site_dict, total_people, bus_hour, time_data)
    result_list = get_result_name(result_list, opt_time, time_dict)
    result_list = merged(result_list, time_data)
    return result_list

print(algorithm(4, time_p = [[22, 23, 24, 25], [23, 24, 25]], name_p = ['Amber', 'Steve'],site_p = [[1,2,3], [1,2,3,4,]]))
