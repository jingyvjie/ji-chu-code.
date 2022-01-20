address="中国"
def Henan():
    msg = "河南省，简称“豫”"  # a是一个局部变量,只属于Henan函数
    print("我是%s,%s" % (address, msg))

def Hubei():
    msg = "湖北省，简称“鄂”" # a是一个局部变量,只属于Hubei函数
    print(msg)

Henan()  # 调用函数的时候,局部变量a出现了
# Henan函数调用完毕,a消失了
# 定义函数的时候局部变量并不存在,只有调用函数的时候局部变量出现了
# print(msg)