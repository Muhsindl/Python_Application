class Student(object):
    
    def __init__(self,firstName,lastName,studentNumber):
        self.firstName=firstName
        self.lastName=lastName
        self.studentNumber=studentNumber
        self.grades=[]
    def add_grade(self,grade):
        self.grades.append(grade)
    def average_grade(self):
        if not self.grades:
            average=0
        else:
            average =sum(self.grades)/len(self.grades)
        return average
    def __str__(self):
        return f"Student: {self.firstName} {self.lastName}, ID: {self.studentNumber}, Average Grade: {self.average_grade():.2f}"

class Teacher:
    def __init__(self, firstName, lastName, teacherNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.teacherNumber = teacherNumber
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def number_of_courses(self):
        return len(self.courses)

    def __str__(self):
        return f"Teacher: {self.firstName} {self.lastName}, ID: {self.teacherNumber}, Number of Courses: {self.number_of_courses()}"

student1 = Student("Fernando", "MUSLERE", "125")
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(92)

teacher1 = Teacher("Mauro", "ICARDI", "999")
teacher1.add_course("Matematik")
teacher1.add_course("Fizik")

print(student1)
print(teacher1)