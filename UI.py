# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:18:35 2020

@author: Sonwe
"""

import tkinter as tk
window=tk.Tk()

#创建entry控件
e=tk.Entry(window)
e.pack()
 

#创建radiobutton控件
var = tk.IntVar()
MPT = [("01 COIL STATUS",1),("02 INPUT STATUS",2),("03 HOLIDING REGISTER",3),("04 INPUT REGISTER",4)]
for mptype, num in MPT:
    pointtype_list = tk.Radiobutton(text=mptype, variable=var,value=num)
    pointtype_list.pack()

################核心代码##################
#获取控件值通过text控件输出
def entry_enter():
    var1=e.get() #获取控件输入值     
    t.insert('insert',var1)

# 创建button控件
b1=tk.Button(window,text='entry',width=15,height=2,command=entry_enter)
b1.pack()

#创建text控件
t=tk.Text(window,height=2)     
t.pack()

window.mainloop()