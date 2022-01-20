# 一个函数里面又调用另一个函数
def person(name):
    print("我是%s" % name)


def address(address):
    print("我想去%s" % address)

def bus():  # 如果不调用bus函数,那么person和address都不执行
    person("张三")  # test2内部调用了person和address
    address("驻马店")

bus()  # 程序第一条执行的语句