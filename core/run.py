from models.school import School
from models.course import Course
from models.class_grade import Class
from models.teacher import Teacher


def manage():
    info = """
    学校管理请按1
    教师功能请按2
    学生功能请按3
    """
    while True:
        m_input = input(info).strip()
        if m_input == "1":
            school()
        if m_input == "2":
            teacher()
        if m_input == "3":
            student()


def school():
    info = """
    增加课程请按1
    增加教师请按3
    增加班级请按2
    退出请按q
    """
    print(info)

    while True:
        m_input = input("请输入功能:").strip()
        if m_input == "1":
            pass
        if m_input == "2":
            pass
        if m_input == "3":
            pass
        if m_input == "q":
            break


def student():
    info = """
    注册请按1
    交学费请按2
    选择班级请按3
    退出请按q
    """
    print(info)
    while True:
        m_input = input("请输入功能:").strip()
        if m_input == "1":
            pass
        if m_input == "2":
            pass
        if m_input == "3":
            pass
        if m_input == "q":
            break


def teacher():
    info = """
    管理班级请按1，
    上课时选择班级请按2
    查看班级学员列表请按3
    修改学员的成绩请按4
    退出请按q
    """
    print(info)
    while True:
        m_input = input("请输入功能:").strip()
        if m_input == "1":
            pass
        if m_input == "2":
            pass
        if m_input == "3":
            pass
        if m_input == "q":
            break

if __name__ == '__main__':
    """
    print("学校介绍：")
    school_shanghai = School("上海", [], [])
    school_beijing = School("北京", [], [])

    python = Course('python', 6, 6000)
    linux = Course('linux', 3, 5000)
    go = Course('go', 3, 5000)

    alex = Teacher("alex", 20, "male", 5000)
    zs = Teacher("zs", 18, "female", 6000)

    school_shanghai.add_course(go)
    school_beijing.add_course(python)
    school_beijing.add_course(linux)
    class_grade_1 = Class('python-7期', python, alex)
    school_beijing.add_class_grade(class_grade_1)

    school_shanghai.enroll()
    school_beijing.enroll()
    """
    manage()
