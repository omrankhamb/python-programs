class Student:
    def __init__(self, name):
        self.__name = name

    def show(self):
        print(self.__name)

s = Student("Jake")
s.show()
print(s.__name)