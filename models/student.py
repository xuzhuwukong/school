from models.schoolmember import SchoolMember


class Student(SchoolMember):
    costs = 0
    num_student = 0

    def __init__(self, name, age, sex, tuition):
        super().__init__(name, age, sex)
        self.tuition = tuition
        self.num_student += 1
        print("学生%s加入，学生总数是:%d" % (self.name, self.num_student))

    def show(self):
        print("我是学生%s:" % self.name)

    def __del__(self):
        self.num_student -= 1
        print("学生%s离开，学生总数是:%d" % (self.name, self.num_student))

if __name__ == '__main__':
    s = Student("lisi", 25, "male", 9000)
    s.show()
