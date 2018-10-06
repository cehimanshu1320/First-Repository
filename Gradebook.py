from MIT_Student import *

class Grades(object):
    def __init__(self):
        #"Create Empty Gradebook"
        self.students = []
        self.grades = {}
        self.isSorted = True
    
    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    
    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')
    
    def getGrades(self, student):
        try:
            return self.grades[student.getIdNum()][:]        #[:] used to return a copy whitout editing original
        except KeyError:
            raise ValueError('Student not in grade book')
            
    def allStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]     #return copy of students
		
def gradeReport(course):
    """Assumes course is of type grades"""
    report = []
    for s in course.allStudents():
        total = 0
        numGrades = 0
        for g in course.getGrades(s):
            total += g
            numGrades += 1
        try:
            avg = total/numGrades
            report.append(str(s)+ '\'s grade is ' +str(avg))
        except ZeroDivisionError:
            report.append(str(s) + 'has no grades')
    return '\n'.join(report)
	
print('--------Grades---------')
ug1 = UG('Matt Damon', 2018)
ug2 = UG('Ben Affleck', 2019)
ug3 = UG('Drew Houston', 2017)
ug4 = UG('Mark Zuckerberg', 2017)
g1 = Grad('Bill Gates')
g2 = Grad('Steve Wozniak')

six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
six00.addStudent(ug4)
six00.addStudent(ug3)

six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addGrade(ug1, 95)
six00.addGrade(ug2, 85)
six00.addGrade(ug3, 75)

print(gradeReport(six00))

six00.addGrade(g1, 90)
six00.addGrade(g2, 45)
six00.addGrade(ug1, 80)
six00.addGrade(ug2, 75)

print(gradeReport(six00))
