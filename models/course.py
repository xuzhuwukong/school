class Course(object):

    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def show(self):
        print("课程名称%s,课程周期%d月，课程价格%d元" % (self.name, self.period, self.price))

if __name__ == '__main__':
    p = Course('python', 6, 6000)
    l = Course('linux', 3, 5000)
    g = Course('go', 3, 5000)
    #l.show()
    course_list = []
    course_list.append(p)
    course_list.append(l)
    for i in course_list:
        i.show()
