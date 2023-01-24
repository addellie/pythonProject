class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Name: {self.fullname}, age: {self.age}, is married: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def get_ball(self):
        return sum(self.marks.values()) / len(self.marks)


class Teacher(Person):
    salary = 10000

    def __init__(self, fullname, age, is_married, experience=0):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def bonus(self):
        if self.experience > 3:
            experience = self.experience - 3
            one_year = (Teacher.salary/100)*5
            return (one_year + Teacher.salary) * experience


def create_students():
    alex = Student('Alex', 19, 'He is not', {'math': 3, 'Literature': 10, 'English': 10, 'art': 7})
    michael = Student('Michael', 24, 'Mary', {'math': 3, 'Literature': 10, 'English': 10, 'art': 7})
    alice = Student('Alice', 26, 'John', {'math': 8, 'literature': 10, 'English': 9, 'art': 10})
    students = [alex, michael, alice]
    return students


create_students()
for student in create_students():
    print(f'name: {student.fullname}, age: {student.age}, married: {student.is_married},'
          f'marks: {student.marks}, ball: {student.get_ball()}')


teacher = Teacher('Natali', 50, 'Alex', 15)
print(f'name:{teacher.fullname}, age: {teacher.age}, married {teacher.is_married}, '
      f'experience {teacher.experience}, bonus {teacher.bonus()}')
