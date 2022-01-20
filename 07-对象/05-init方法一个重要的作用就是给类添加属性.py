class address:  # 不在普通方法中定义属性
    def set_country(self, country):
        self.country = country
        print(self.country)
    def show_country(self):
        print(self.country)

address().set_country("中国")

class address:
    def __init__(self, country = "中国"):
        self.country = country
    def set_country(self, country):
        self.country = country
    def show_country(self):
        print(self.country)

c = address("日本")  # init自动已经调用了,所以name属性已经有了
c.show_country()