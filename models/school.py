from models.teacher import Teacher
from models.student import Student


class School(object):

    def __init__(self, name):
        self.name = name
        self.class_grade_list = []
        self.course_list = []

    def enroll(self):
        print("\033[6;30;42m %s学校正在招生,当前的课程有：\033[0m" % self.name)
        for i in self.course_list:
            i.show()
            #self.course_list[i].show()

    def add_course(self, course):
        self.course_list.append(course)

    def add_class_grade(self, class_grade):
        self.class_grade_list.append(class_grade)

if __name__ == "__main__":
    t_li = Teacher("li", 22, "m", 500)

    course_python = ["python", 6, 500]
    course_linux = ["linux", 6, 500]
    course_go = ["go", 6, 500]

    class_python = ["python-phase1", t_li, 5000]
    class_go = ["go-phase1", t_li, 6000]
    class_linux = ["linux-phase1", t_li, 8000]

    sh = School("shanghai", [], [])
    sh.add_course(class_python)
    sh.add_course(class_linux)
    bj = School("Beijing", [], [])
    bj.add_class_grade(class_go)
