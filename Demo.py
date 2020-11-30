# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:55:25 2020

@author: Sonwe
"""

import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import tkinter as tk
window=tk.Tk()

def read(PORT="COM1"):
    output = []
    master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,
                                                baudrate=9600, bytesize=8, parity='N', stopbits=1))
    master.set_timeout(5.0)
    master.set_verbose(True)

    #读保持寄存器
    output = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 10)  #这里可以修改需要读取的功能码
    #(从站ID; 实现功能码; 开始读取的位置; 读取的长度)
    return output  

def write(change_value, address, PORT="COM1"):
    output = []
    master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,
                                                baudrate=9600, bytesize=8, parity='N', stopbits=1))
    master.set_timeout(5.0)
    master.set_verbose(True)

    output = master.execute(1, cst.WRITE_SINGLE_REGISTER, address, output_value=change_value)
    #(从站ID; 实现功能码; 需要改变的地址位; output_vlaue改变的内容)
    return output


text_adress = tk.Label(window, text="Address")
text_register = tk.Label(window, text="Register")
text_register.place(x=183, y=22, anchor='sw')
text_adress.place(x=250, y=50, anchor='se')
#创建register控件
register = tk.Entry(window)
register.pack()
#创建address控件
address = tk.Entry(window)
address.pack()

def WRITE():
    t.delete('1.0','end')    
    register_value=register.get() #获取控件输入值  
    address_value=address.get()
    write(int(register_value), int(address_value))
    out = read()
    t.insert('insert', out)
    t.insert('insert', '\n')

def READ():
    t.delete('1.0','end')    
    out = read()
    t.insert('insert',out)
    t.insert('insert', '\n')

    
#创建按钮控件
b1=tk.Button(window,text='WRITE',width=15,height=2,command=WRITE)
b2=tk.Button(window,text='READ',width=15,height=2,command=READ)
#按钮的大小，文本显示以及按键命令
b1.pack()
b2.pack()

#创建输出显示控件
t=tk.Text(window,height=4)  #输出框的高度
t.pack()

window.mainloop()