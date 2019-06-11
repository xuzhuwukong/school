from models.teacher import Teacher
from models.student import Student


class School(object):

    def __init__(self, name, course_list, class_grade_list):
        self.name = name
        self.class_grade_list = class_grade_list
        self.course_list = course_list

    def enroll(self):
        print("\033[6;30;42m %s学校正在招生,当前的课程有：\033[0m" % self.name)
        for i in self.course_list:
            i.show()
            #self.course_list[i].show()

    def add_course(self, course):
        self.course_list.append(course)

    def add_class_grade(self, class_grade):
        self.class_grade_list.append(class_grade)

