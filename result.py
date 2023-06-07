# ResultPage

import tkinter as tk

class ResultPage():


    def __init__(self, win, cb, rs_list):
        self.win = win
        self.cb = cb
        self.rs_list = rs_list
        self.result_lbs = []

        # 建立元件
        self.components = {
            'title': tk.Label(win, text='\\   聚餐結果   /', fg='black', bg='#f2d5a3', font=('Arail', 30, 'bold'), justify='center'),
            'result_num': tk.Label(win, text=f'''總共有 {len(self.rs_list)} 組最佳結果''', fg='black', bg='#f5ebe0', font=('Arial', 16), width=30, height=2),
            'more_result': tk.Button(win, text='查看更多結果', bg='#e3d5ca', fg='black', font=('Arial', 16), width=20, height=2,
                               activebackground='black', activeforeground='yellow', command=self.show_more),
            'back_to_homepage': tk.Button(win, text='回首頁', bg='#e3d5ca', fg='black', font=('Arial', 16), width=20, height=2,
                               activebackground='black', activeforeground='yellow', command=self.cb)}
        
    # 設定所有元件在視窗的位置
    def layout(self):
        self.components['title'].place(anchor="center", relx=0.5, rely=0.2)
        if self.rs_list  != []:
            self.components['result_num'].place(anchor="center", relx=0.5, rely=0.3)
    
        if len(self.rs_list) <= 2 or (len(self.rs_list) >= 3 and self.rs_list[-1]== []) :
            self.components['back_to_homepage'].place(anchor="center", relx=0.5, rely=0.82)
        else:
            self.components['back_to_homepage'].place(anchor="center", relx=0.4, rely=0.82)
            self.components['more_result'].place(anchor="center", relx=0.6, rely=0.82)

    def create_result(self):
        # 最終結果的label

        # 顯示約不成的結果
        if self.rs_list  == []:
            result_lb = tk.Label(self.win, text='大家時間對不上，約不成了嗚嗚', fg='black', bg='#f8ecc9', font=('Arial', 16), width=60, height=12)
            result_lb.place(anchor="center", relx=0.5, rely=0.5)
            self.result_lbs.append(result_lb)

        # 顯示約成的結果
        else:
            for i in range(len(self.rs_list )):
                if self.rs_list [i] == []:continue

                else:
                    result_lb = tk.Label(self.win, 
                                            text=f'''
第 {i+1} 組最佳結果
最佳時段：{self.rs_list [i][0]}
最佳餐廳：{self.rs_list [i][1]}
可參加者：{self.rs_list [i][2]}
''',
                                            justify='left', bg='#f8ecc9', font=('Arial',16), width=60, height=6)
                    # 每次顯示兩個結果在視窗
                    if (i+1) % 2 == 1:
                        result_lb.place(relx=0.5, rely=0.455, anchor='center')
                    elif (i+1) % 2 == 0:
                        result_lb.place(relx=0.5, rely=0.655, anchor='center')
                    
                    self.result_lbs.append(result_lb)
                    self.rs_list [i] = []  # 把已顯示過的結果轉為空的list

                if (i + 1) % 2 == 0:  # 已顯示兩個結果
                    break
        
        return self.rs_list 


    # 在視窗上顯示所有元件
    def show(self):
        self.create_result()
        self.layout()
        for _, item in self.components.items():
            item.place()

    # 在視窗上隱藏所有元件
    def hide(self):
        for lbs in self.result_lbs:
            lbs.place_forget()
        
        for _, item in self.components.items():
            item.place_forget()

    # 結果大於兩個的話，先隱藏畫面上的元件，再顯示另外兩組結果
    def show_more(self):
        self.win.update()
        self.hide()
        self.show()


# 為了讓頁面能夠單獨測試，且避免import時會執行以下程式碼
if __name__ == '__main__':
    win1 = tk.Tk()
    win1.geometry('1280x720')
    win1.title('一起聚餐吧')
    win1.configure(bg='#f2d5a3')

    # 測資
    rs_list = [['00:00-01:30', ['辛殿公館店'], ['Jay', 'Justin', 'Amber']], ['17:00-17:30', ['辛殿公館店', '貳樓公館店'], ['Jay', 'Justin', 'Amber']]]
    
    def cb():
        page.hide()
    def result_over():
        page.hide()

    page = ResultPage(win1, cb, rs_list)
    page.show()
    win1.mainloop()