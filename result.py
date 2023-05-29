# ResultPage

import tkinter as tk

class ResultPage():

    def __init__(self, win, cb, over):
        # more_result 的 command 還要改
        self.win = win
        self.cb = cb
        self.over = over
        self.result_lbs = []
        self.components = {
            'title': tk.Label(win, text='\n 最終結果！\n', fg='black', bg='#f2d5a3', font=('Arial', 22), width=30, height=3,
                              justify='center'),
            'result_num': tk.Label(win, text=f'''總共有 {len(result_list)} 組最佳結果''', fg='black', bg='#f5ebe0', font=('Arial', 16), width=30, height=2),
            'more_result': tk.Button(win, text='查看更多結果', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2,
                               activebackground='black', activeforeground='yellow', command=self.show_more),
            'back_to_homepage': tk.Button(win, text='回首頁', bg='#e3d5ca', fg='black', font=('Arial', 12), width=20, height=2,
                               activebackground='black', activeforeground='yellow', command=self.cb)}

    def layout(self):
        self.components['title'].place(anchor="center", relx=0.5, rely=0.069)
        self.components['result_num'].place(anchor="center", relx=0.5, rely=0.15)
        if result_list == [] or result_list[-2] == []:
            self.components['back_to_homepage'].place(anchor="center", relx=0.5, rely=0.8)
        else:
            self.components['back_to_homepage'].place(anchor="center", relx=0.4, rely=0.8)
            self.components['more_result'].place(anchor="center", relx=0.6, rely=0.8)


    def create_result(self):
        # 最終結果的label

        # 約不成
        if result_list == []:
            result_lb = tk.Label(self.win, text='大家時間對不上，約不成了嗚嗚', fg='black', bg='#f8ecc9', font=('Arial', 16), width=30, height=6)
            result_lb.place(anchor="center", relx=0.5, rely=0.5)
            self.result_lbs.append(result_lb)  # 好像是隱藏時要用的 參考time_table.py!

        # 約成
        else:
            for i in range(len(result_list)):
                if result_list[i] == []:
                    continue

                else:
                    result_lb = tk.Label(self.win, 
                                            text=f'''第 {i+1} 組最佳結果\n\n最佳時段：{result_list[i][0]}\n最佳餐廳：{result_list[i][1]}\n可參加者：{result_list[i][2]}''', 
                                            bg='#f8ecc9', font=('Arial',16), width=30, height=6)
                    
                    if (i+1) % 4 == 1:
                        result_lb.place(relx=0.25, rely=0.285+0.2*0)
                    elif (i+1) % 4 == 2:
                        result_lb.place(relx=0.55, rely=0.285+0.2*0)
                    elif (i+1) % 4 == 3:
                        result_lb.place(relx=0.25, rely=0.285+0.2*1) 
                    else:
                        result_lb.place(relx=0.55, rely=0.285+0.2*1)
                    
                    self.result_lbs.append(result_lb)
                    result_list[i] = []  # 把已顯示過的結果轉為空的list

                if (i + 1) % 4 == 0:  # 已顯示四個結果
                    break
        
        return result_list

    def show(self):
        self.layout()
        for _, item in self.components.items():
            item.place()
        self.create_result()

    def hide(self):
        for lbs in self.result_lbs:
            lbs.place_forget()
        
        for _, item in self.components.items():
            item.place_forget()

    def show_more(self):
        print('more_result button clicked')
        self.hide()
        self.show()



if __name__ == '__main__':
    win1 = tk.Tk()
    win1.geometry('1280x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')

    # 測資
    '''result_list = [['time1', 'rest1', 'name1'], 
                    ['time2', 'rest2', 'name2'], 
                    ['time3', 'rest3', 'name3']]'''

    result_list = [['time1', 'rest1', 'name1'], 
                    ['time2', 'rest2', 'name2'], 
                    ['time3', 'rest3', 'name3'], 
                    ['time4', 'rest4', 'name4'], 
                    ['time5', 'rest5', 'name5'], 
                    ['time6', 'rest6', 'name6'], 
                    ['time7', 'rest7', 'name7'], 
                    ['time8', 'rest8', 'name8'], 
                    ['time9', 'rest9', 'name9']]
    #result_list = [['18:00-20:00', '麥當勞公館店', 'Amber, Rowan, Jay'], ['11:00-15:00', '辛殿', 'Rowan, Jay, Celest'], ['17:00-21:00', '順園小館', 'Celest, Rowan'],['15:00-18:00', '貳樓', 'Amber, Celest']]
    result_list = []
    print(result_list)



    def cb():
        page.hide()
    def result_over():
        page.hide()

    page = ResultPage(win1, cb, result_over)
    #p1 = ResultPage(win1, lambda:p1.hide())
    page.show()

    win1.mainloop()