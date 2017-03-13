#a = [1, 2, 3]
#b = a
#b[0] = 0
#print b
#print a
class MyClass:
    def __init__(self):
        print "new Object"
        self.name = "myclass"

    def setName(self, name):
        self.name = name

    def printName(self):
        print self.name

a = MyClass()
print a.name
a.setName("Apple")
a.printName()

class MyNewClass(MyClass):
    def setAge(self, age):
        self.age = age

    def printAge(self):
        print self.age

a = MyNewClass()
print a.name
a.setName("Apple")
a.printName()
a.setAge(18)
a.printAge()