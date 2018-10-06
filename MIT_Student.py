from PersonTrieal import Person
from MITPerson import MITPerson

class UG(MITPerson):
    def __init(self, name, classYear):
        MITPerson.__init(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, "+utterance)

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj, UG) or isinstance(obj, Grad)
