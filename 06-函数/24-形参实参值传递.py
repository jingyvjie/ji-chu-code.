a = [1, 2, 3]

def my_test1(a):  # 这里的a是一个形参,也是一个属于my_test1的局部变量
    a[0] = 10  # 修改的是形参a的值
    # 如果形参的类型为列表,集合和字典,修改形参的值会直接影响实参的值

print(a)  # 显示的是全局变量a的值
my_test1(a) # 把全局变量做为实参,来调用my_test1
print(a)