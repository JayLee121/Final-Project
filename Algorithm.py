
# Algorithm

# input(使用者所選的時間,餐廳) 以dict()的方式傳輸，
# 幫我整理好 time_dict 的 key = time  value = list.append(user's name)
# 在傳入 time_dict 的時候要先切成每半小時為單位，key存成約的時間“點”（例如18:00)
# site_dict key = use's name / value = list.append(site_name)

debug = True
time_proportion = 1/2
site_proportion = 1/3
total_people = 3

# test data 
time_dic = {'6:00':['Justin', 'Jay', 'Mary'], '6:10':['Mary']}
site_dic = {'Justin': ['abc','cde'], 'Jay':['abc','okl'],'Mary':['abc','opl'] }


# 找出票數大於比例的 x_dict key:time or restaurant name / value :user's name 
def filter_porportion(x_dict, people, porportion):
    temp_x = []
    for key in x_dict.keys():
        num = len(x_dict[key])
        if num >= total_people * time_proportion:temp_x.append([key, num])
    accept_x = (sorted(temp_x, key=lambda x:x[1], reverse=True))
    return accept_x

# 找出最佳值，以及判斷是否有複數個最佳值
def find_optimal(accept_x):
    optimal_x = []
    optimal_x.append(accept_x[0][0])
    for i in range (1, len(accept_x)):
        if accept_x[i][0] == optimal_x[0]: optimal_x.append(accept_x[i][0])
    return optimal_x

def match(time_dict, site_dict):
    find_time, find_site = True, True
    # 可接受的時間
    accept_time = filter_porportion(time_dict, total_people, time_proportion)
    if len(accept_time) == 0: find_time = False
    num_participant = accept_time[0][1]
    if debug: print('accept_time:', accept_time)
    if debug: print('num_participants:', num_participant)
    
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
    if debug:print('site_vote:', site_vote)
    
    # 可接受的餐廳
    accept_site = filter_porportion(site_vote, num_participant, site_proportion)
    if len(accept_site) == 0: find_site = False
    if debug: print('accept_site:', accept_site)

match (time_dic, site_dic)