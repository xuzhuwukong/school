from models.people import People
class SchoolMember(People):
    sum_member = 0

    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.sum_member += 1
        print("欢迎新成员:", self.name)
        print("成员数:", self.sum_member)

    def say_hello(self):
        print("我是新成员:", self.name)

    def __del__(self):
        self.sum_member -= 1
        print("%s成员已经离开,还有成员数%d" % (self.name, self.sum_member))
