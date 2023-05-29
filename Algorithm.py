debug = True
time_proportion = 1/2
site_proportion = 1/3

# 找出票數大於比例的 x_dict key:time or restaurant name / value :user's name 
def filter_proportion(x_dict, proportion, total_people):
    temp_x = []
    for key in x_dict.keys():
        num = len(x_dict[key])
        if num >= total_people * proportion: temp_x.append([key, num])
    return temp_x

# 找出最佳值，以及判斷是否有複數個最佳值
def find_optimal(temp_x):
    accept_x = (sorted(temp_x, key=lambda x:x[1], reverse=True))
    optimal_x = []
    optimal_x.append(accept_x[0][0])
    for i in range (1, len(accept_x)):
        if accept_x[i][1] == accept_x[0][1]: optimal_x.append(accept_x[i][0])
    return optimal_x

def get_result(time_dict, site_dict, total_people):
    accept_time = filter_proportion(time_dict, time_proportion, total_people)  # 可接受的時間
    if len(accept_time) == 0: return []
    if debug: print('accept_time:', accept_time)
    optimal_time = find_optimal(accept_time)  # 找出最佳的時間
    if debug: print('optimal_time:', optimal_time)
    
    # 計算這些參加者投了哪些餐廳
    site_vote = {}
    for time in optimal_time:
        name_list = time_dict[time]
        for name in name_list:
            site_list = site_dict[name]
            for site in site_list:
                if site not in site_vote:
                    site_vote[site] = [name]
                else:
                    site_vote[site].append(name)
    
    if debug: print('site_vote:', site_vote)
    accept_site = filter_proportion(site_vote, site_proportion, total_people)  # 可接受的餐廳
    if debug: print('accept_site:', accept_site)
    
    # 只有一個最佳時間 餐廳一個或多個
    if len(optimal_time) == 1:
        optimal_time = optimal_time[0]
        result_list = []
        result_list.append([optimal_time])  # 時間
        
        # 餐廳
        result_list[0].append(accept_site[0][0])
        for i in range(1, len(accept_site)):
            if accept_site[i][1] == accept_site[0][1]:
                result_list[0][1] += ', '
                result_list[0][1] += accept_site[i][0]
        result_list[0].append(time_dict[optimal_time][0])
        for i in range(1, len(time_dict[optimal_time])):
            result_list[0][2] += ', '
            result_list[0][2] += time_dict[optimal_time][1]
    
    # 有多個最佳時間 
    else:
        result_list = []
    if debug: print('result_list:', result_list)

