from models.schoolmember import SchoolMember


class Teacher(SchoolMember):

    def __init__(self, name, age, sex, salary):
        # People.__init__(self,name,age,sex)
        super().__init__(name, age, sex)
        self.salary = salary

    def show(self):
        print("老师的姓名:%s, 老师的年龄:%d" %(self.name,self.age))

if __name__ == '__main__':
    a = Teacher("zhang", 25, "male", 3000)
    # a.show()
    c = Teacher("li", 25, "male", 3000)
    b = []
    b.append(a)
    b.append(c)
    for i in b:
        # print(i)
        i.show()

    print("\033[6;30;42m hello \033[0m")