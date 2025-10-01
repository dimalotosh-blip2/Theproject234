#class Parent
 #  classmethods and attrs
#class Child(Parent):
# classmethods and attrs

#class Human:
#   height = 170
#   saliely - 50
#class Student(Human):
#saliely = 0
 #class Worker(Human):
    #saliely = 160

 #nick = Student()
 #ann = Worker()
 #print(nick. saliely)
 #print(ann. saliely)


 #class Class1:
   #var = 20
   #def __init__(self):
       #self.var = 10
 #class Class2(Class1):
   #def __init__(self):
       #print(self.var)
       #super().__init__()
       #print(self.var)
       #print(super().var)

 #obj = Class2()

class Computer:
    def calculate(self):
        print("I can calculate")
class Display:
    def display(self):
        print("I can show")
class Smartphone(Computer, Display):
    pass

phone = Smartphone()
phone.calculate()
phone.display()