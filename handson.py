class Person:
    def __init__(self, std1, std2, std3, pre, mid, fin):
        self.__std1 = std1
        self.__std2 = std2
        self.__std3 = std3
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

    def Grade(self):
        return (self.__pre + self.__mid + self.__fin) / 3

    def display1(self):
        print(self.__std1, self.Grade(), "\n")

    def display2(self):
        print(self.__std2, self.Grade(), "\n")

    def display3(self):
        print(self.__std3, self.Grade())


class student1(Person):
    term_grade = Person("Emin D. Imura =", 0, 0, float(input("Prelim Grade: ")), float(input("Midterm Grade: ")),
                        float(input("Final Grade: ")))
    term_grade.display1()


class student2(Person):
    term_grade = Person(0, "James Dayao =", 0, float(input("Prelim Grade: ")), float(input("Midterm Grade: ")),
                        float(input("Final Grade: ")))
    term_grade.display2()


class student3(Person):
    term_grade = Person(0, 0, "Robert Victor Callorina =", float(input("Prelim Grade: ")),
                        float(input("Midterm Grade: ")), float(input("Final Grade: ")))
    term_grade.display3()