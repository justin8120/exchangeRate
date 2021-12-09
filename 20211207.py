# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import messagebox as msgbox

def ca():
    if(gender.get()==0):
        T=aa.get()
        G=bb.get()
        AA=float(T/G)
    else:
        T=aa.get()
        G=bb.get()
        AA=float(T*G)
    messagebox = msgbox.askokcancel('台幣和美金互換',AA ,
                                    icon='info')
    lblResult['text']='a'.format(AA)
    
win=tk.Tk()
win.title('台幣和美金互換')
win.geometry('400x200')

lbl00 = tk.Label(win, text='請輸入金額', bg='white',
                 fg='black' , font=('標楷體', 12))
lbl01 = tk.Label(win, text='請輸入美金匯率', bg='white'
                 , fg='black', font=('標楷體', 12))
gender=tk.IntVar()
lblshow=tk.Label(win, text='', font=('新明細體', 14))
aa=tk.IntVar()
bb=tk.IntVar()
btnok=tk.Button(win, text='確認', command=ca)
c1=tk.Radiobutton(win, text='台幣換美金',
                  variable=gender, value=1)
c2=tk.Radiobutton(win, text='美金換台幣',
                  variable=gender, value=0)
a=tk.Entry(win, width=12, textvariable=aa)
b=tk.Entry(win, width=12, textvariable=bb)

lbl00.grid(row=0, column=0)
lbl01.grid(row=1, column=0)
a.grid(row=0, column=1)
b.grid(row=1, column=1)
c1.grid(row=2, column=1)
c2.grid(row=2, column=2)
btnok.grid(row=3, column=3)
lblResult=tk.Label(win, padx=10,pady=8)
lblResult.grid(row=4, column=1)
win.mainloop()

win.mainloop()