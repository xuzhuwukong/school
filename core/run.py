from models.school import School
from models.course import Course
from models.class_grade import Class
from models.teacher import Teacher
if __name__ == '__main__':
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

