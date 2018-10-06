from PersonTrial import Person
from MITPerson import MITPerson

class Student(MITPerson):               #Used to inherit from proper place
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, "+utterance)

class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    #return isinstance(obj, UG) or isinstance(obj, Grad) or isinstance(obj, TransferStudent)
    return isinstance(obj, Student) #Student class created to organise the hierarchy for diff types of students (instead of using above stmt we can use this)

print('-------Student-------')
s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2015)
s3 = UG('Lin Manuel', 2016)
s4 = Grad('Leonardo Di Caprio')

studentList = [s1, s2, s3, s4]

print(s1)
print(s1.getClass())
print(s2.speak('Where is the quiz?'))
