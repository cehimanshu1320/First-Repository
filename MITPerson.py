from PersonTrial import Person

class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, utterance):
        return (self.getLastName() + " says: " + utternace)

m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3, 5, 14, 84)
m2 = MITPerson('Bill Gates')
Person.setBirthday(m2, 3, 4, 80)
m1 = MITPerson('Drew Houston')
Person.setBirthday(m1, 10, 28, 55)

MITPersonList = [m1, m2, m3]

#print(m2)

for e in MITPersonList:
    print(e)

MITPersonList.sort()
print('------------')
for e in MITPersonList:
    print(e)

p1 = Person('John Eric')
print("First: " + str(m1<m2))
#print("Second: " + str(p1>m1))     #calls m1.__lt__(p1) method of MITPerson class which compares using id and p1 do not have id => Attribute Error
print("Third: " + str(p1<m1))       #calls p1.__lt__(m1) method of Person class which compares using name => Pass
