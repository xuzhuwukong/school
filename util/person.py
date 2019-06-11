import pickle


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def show(self):
        print(self.name + "_" + str(self.age))


aa = Person("JGood", 2)
aa.show()
f = open('d:\\p.txt', 'ab')
pickle.dump(aa, f, 0)
f.close()

aa1 = Person("JGood2", 2)
aa1.show()
f = open('d:\\p.txt', 'ab')
pickle.dump(aa1, f, 0)
f.close()

# del Person
f = open('d:\\p.txt', 'rb')
bb = pickle.load(f)
f.close()
bb.show()

with open('d:\\p.txt', 'rb') as urs_file:
    while True:
        try:
            info = pickle.load(urs_file)
            info.show()
        except EOFError:
            break