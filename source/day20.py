"""
    Day20 Pandas2
    Version : 1.0
    Created : 2021.12.31
    Updated : 2021.12.31
    Author  : S.M.Lee
"""
from tkinter import *
import maps

def search_hospital(arg=None):
    sido_cd = entry1.get()
    typ_cd = entry2.get()
    label2.config(text=sido_cd + ':' + typ_cd)
    # sido_cd 와 typ_cd의 변수를 연결해준다
    maps.find_hospital(sido_cd, typ_cd)

root = Tk()

label1 = Label(root, text='Find Hospital')
# pack : 창안에 들어가게 함
label1.pack()

entry1 = Entry(root, width=20)
entry2 = Entry(root, width=20)
entry1.pack()
entry2.pack()

button1 = Button(root, text='Search', command=search_hospital, fg='#000000', bg='#EEEEEE')
button1.pack()

label2 = Label(root, text='')
label2.pack()

# 창
root.title('병원찾기')
root.geometry('300x120')
# window 작동하게 하기
root.mainloop()