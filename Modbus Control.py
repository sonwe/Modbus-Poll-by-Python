# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

#设置所需要使用的端口
def mod(PORT="COM1"):
    output = []
    master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,
                                                baudrate=9600, bytesize=8, parity='N', stopbits=1))
    master.set_timeout(5.0)
    master.set_verbose(True)

    #读保持寄存器
    master.execute(1, cst.WRITE_SINGLE_REGISTER, 0, output_value = 2)
    output = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 10)  #这里可以修改需要读取的功能码

    #(从站ID; 实现功能码; 需要改变的地址位; output_vlaue改变的内容)
    #(从站ID; 实现功能码; 开始读取的位置; 读取的长度)
    print(output)
    return output  

if __name__ == "__main__":
    mod()
    
'''
功能代码cst
    1～255中1～21是常用的，以下是读写专用的功能码
    READ_COILS = 01 读线圈，位操作
    READ_DISCRETE_INPUTS = 02 读离散输入状态，位操作
    READ_HOLDING_REGISTERS = 03 读保持寄存器，字操作
    READ_INPUT_REGISTERS = 04 读输入寄存器，字操作
    WRITE_SINGLE_COIL = 05 写单线圈，位操作
    WRITE_SINGLE_REGISTER = 06 写单一寄存器，字操作
    WRITE_MULTIPLE_COILS = 15 写多个线圈【强制多点线圈】，位操作
    WRITE_MULTIPLE_REGISTERS = 16 写多寄存器【写乘法寄存器】，字操作
'''