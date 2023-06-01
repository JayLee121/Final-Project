# ResultPage

import tkinter as tk

class ResultPage():

    def __init__(self, win, cb, rs_list):
        self.win = win
        self.cb = cb
        self.rs_list = rs_list
        self.result_lbs = []
        self.components = {
            'title': tk.Label(win, text='\\   聚餐結果   /', fg='black', bg='#f2d5a3', font=('Arail', 30, 'bold'), justify='center'),
            'result_num': tk.Label(win, text=f'''總共有 {len(self.rs_list)} 組最佳結果''', fg='black', bg='#f5ebe0', font=('Arial', 16), width=30, height=2),
            'more_result': tk.Button(win, text='查看更多結果', bg='#e3d5ca', fg='black', font=('Arial', 16), width=20, height=2,
                               activebackground='black', activeforeground='yellow', command=self.show_more),
            'back_to_homepage': tk.Button(win, text='回首頁', bg='#e3d5ca', fg='black', font=('Arial', 16), width=20, height=2,
                               activebackground='black', activeforeground='yellow', command=self.cb)}
        

    def layout(self):
        self.components['title'].place(anchor="center", relx=0.5, rely=0.2)
        self.components['result_num'].place(anchor="center", relx=0.5, rely=0.3)
        
        #if len(self.rs_list) <= 4 or (len(self.rs_list) > 5 and self.rs_list[-1]== []) :
        if len(self.rs_list) <= 2 or (len(self.rs_list) > 3 and self.rs_list[-1]== []) :
            self.components['back_to_homepage'].place(anchor="center", relx=0.5, rely=0.82)
        else:
            self.components['back_to_homepage'].place(anchor="center", relx=0.4, rely=0.82)
            self.components['more_result'].place(anchor="center", relx=0.6, rely=0.82)

    '''def layout(self):
        self.components['title'].place(anchor="center", relx=0.5, rely=0.2)
        self.components['result_num'].place(anchor="center", relx=0.5, rely=0.3)
        
        if len(self.rs_list) <= 4 or (len(self.rs_list) > 5 and self.rs_list[-1]== []) :
            self.components['back_to_homepage'].place(anchor="center", relx=0.5, rely=0.82)
        else:
            self.components['back_to_homepage'].place(anchor="center", relx=0.4, rely=0.82)
            self.components['more_result'].place(anchor="center", relx=0.6, rely=0.82)'''

    def create_result(self):
        # 最終結果的label

        # 約不成
        if self.rs_list  == []:
            result_lb = tk.Label(self.win, text='大家時間對不上，約不成了嗚嗚', fg='black', bg='#f8ecc9', font=('Arial', 16), width=30, height=6)
            result_lb.place(anchor="center", relx=0.5, rely=0.5)
            self.result_lbs.append(result_lb)
 
        # 約成
        else:
            for i in range(len(self.rs_list )):
                if self.rs_list [i] == []:
                    continue

                else:
                    result_lb = tk.Label(self.win, 
                                            text=f'''
第 {i+1} 組最佳結果
最佳時段：{self.rs_list [i][0]}
最佳餐廳：{self.rs_list [i][1]}
可參加者：{self.rs_list [i][2]}
''',
                                            justify='left', bg='#f8ecc9', font=('Arial',16), width=60, height=6)
                    
                    if (i+1) % 2 == 1:
                        result_lb.place(relx=0.5, rely=0.455, anchor='center')
                    elif (i+1) % 2 == 0:
                        result_lb.place(relx=0.5, rely=0.655, anchor='center')
                    
                    self.result_lbs.append(result_lb)
                    self.rs_list [i] = []  # 把已顯示過的結果轉為空的list

                if (i + 1) % 2 == 0:  # 已顯示四個結果
                    break
        
        return self.rs_list 


    """def create_result(self):
        # 最終結果的label

        # 約不成
        if self.rs_list  == []:
            result_lb = tk.Label(self.win, text='大家時間對不上，約不成了嗚嗚', fg='black', bg='#f8ecc9', font=('Arial', 16), width=30, height=6)
            result_lb.place(anchor="center", relx=0.5, rely=0.5)
            self.result_lbs.append(result_lb)
 
        # 約成
        else:
            for i in range(len(self.rs_list )):
                if self.rs_list [i] == []:
                    continue

                else:
                    result_lb = tk.Label(self.win, 
                                            text=f'''
第 {i+1} 組最佳結果
最佳時段：{self.rs_list [i][0]}
最佳餐廳：{self.rs_list [i][1]}
可參加者：{self.rs_list [i][2]}
''',
                                            justify='left', bg='#f8ecc9', font=('Arial',16), width=30, height=6)
                    
                    if (i+1) % 4 == 1:
                        result_lb.place(relx=0.25, rely=0.38+0.2*0)
                    elif (i+1) % 4 == 2:
                        result_lb.place(relx=0.535, rely=0.38+0.2*0)
                    elif (i+1) % 4 == 3:
                        result_lb.place(relx=0.25, rely=0.38+0.2*1) 
                    else:
                        result_lb.place(relx=0.535, rely=0.38+0.2*1)
                    
                    self.result_lbs.append(result_lb)
                    self.rs_list [i] = []  # 把已顯示過的結果轉為空的list

                if (i + 1) % 4 == 0:  # 已顯示四個結果
                    break
        
        return self.rs_list""" 

    def show(self):
        self.create_result()
        self.layout()
        for _, item in self.components.items():
            item.place()

    def hide(self):
        for lbs in self.result_lbs:
            lbs.place_forget()
        
        for _, item in self.components.items():
            item.place_forget()

    def show_more(self):
        self.win.update()
        self.hide()
        self.show()



if __name__ == '__main__':
    win1 = tk.Tk()
    win1.geometry('1280x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')

    # 測資
    
    '''rs_list  = [['time1', 'rest1', 'name1'], 
                     ['time2', 'rest2', 'name2'], 
                     ['time3', 'rest3', 'name3']]'''
    
    rs_list  = [['time1', 'rest1', 'name1'], 
                    ['time2', 'rest2', 'name2'], 
                    ['time3', 'rest3', 'name3'], 
                    ['time4', 'rest4', 'name4'], 
                    ['time5', 'rest5', 'name5'], 
                    #['time6', 'rest6', 'name6'], 
                    #['time7', 'rest7', 'name7'], 
                    #['time8', 'rest8', 'name8'], 
                    #['time9', 'rest9', 'name9']
                    ]

    rs_list  = [['time1', '新生南路麥當勞,順園小館,辛殿公館店,鍋in,貳樓公館店', 'name1name1name1name1name1'], 
                    ['time2', '新生南路麥當勞,順園小館,辛殿公館店', 'name2name2name2name2'], 
                    ['time3', '順園小館,辛殿公館店', 'name3name3name3name3name3name3'], 
                    ['time4', 'rest4', 'name4'], 
                    ['time5', 'rest5', 'name5'], 
                    #['time6', 'rest6', 'name6'], 
                    #['time7', 'rest7', 'name7'], 
                    #['time8', 'rest8', 'name8'], 
                    #['time9', 'rest9', 'name9']
                    ]

    #rs_list = []

    def cb():
        page.hide()
    def result_over():
        page.hide()

    page = ResultPage(win1, cb, rs_list)
    #p1 = ResultPage(win1, lambda:p1.hide())
    page.show()
    win1.mainloop()