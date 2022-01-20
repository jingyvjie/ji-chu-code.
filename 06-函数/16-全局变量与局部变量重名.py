country="中国"
num=11
def Henan():
    num=333 # 这里不是为全局变量赋值, 这里是定义了一个局部变量, 名字和全局变量重名
    msg = "河南省，简称“豫”"
    print(num) # 打印的是局部变量num的值
    num+= 1   # 这里改的是局部变量num的值

def Tokyo():
    country="日本" # 这里不是为全局变量赋值, 这里是定义了一个局部变量, 名字和全局变量重名
    print(country) # 打印的是局部变量country的值


Henan()
Tokyo()
print(num) # 打印的是全局变量num1的值