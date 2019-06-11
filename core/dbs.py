import pickle
from cfgs import settings

class Dbs(object):
    def __init__(self, filename):
        self._config = None
        self.filename = settings.DB_PATH + filename

    def __getattr__(self, name):
        pass

    def load(self):
        """ Load pickle file
        """
        with open(self.filename, 'rb') as usrs_file:
            while True:
                try:
                    info = pickle.load(usrs_file)
                    info.show()
                except EOFError:
                    break

    def save(self, info):
        """Write the object into a pickle file."""
        usrs_file = open(self.filename, 'ab')
        pickle.dump(info, usrs_file, 0)
        usrs_file.close()

if __name__ == "__main__":
    from models.student import Student
    name = input("请输入姓名：")
    age = int(input("请输入年龄："))
    sex = input("请输入性别：")
    tuition = int(input("请输入学费："))

    s1 = Student(name, age, sex, tuition)
    dbs = Dbs("student")
    dbs.save(s1)
