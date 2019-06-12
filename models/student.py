from models.schoolmember import SchoolMember


class Student(SchoolMember):
    costs = 0
    num_student = 0

    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.num_student += 1
        self.class_grade = []
        self.score = 0
        print("学生%s加入，学生总数是:%d" % (self.name, self.num_student))

    def show(self):
        print("我是学生%s:" % self.name)

    def pay_tuition(self,num):
        self.tuition += num

    def select_class(self, class_grade):
        self.class_grade.append(class_grade)

    def __del__(self):
        self.num_student -= 1
        print("学生%s离开，学生总数是:%d" % (self.name, self.num_student))

    def __str__(self):
        pass

if __name__ == '__main__':
    s = Student("lisi", 25, "male")
    s.show()
