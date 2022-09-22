#declear class
class Dog:
    #attribute
    attr1 = 'Mammal'
    attr2 = 'Dog'

    #method
    def fun(self):
        print(" I am a ", self.attr1)
        print(" This is a ", self.attr2)
#initialized a class - this called object
obj = Dog()
#access method of a class
obj.fun()

#access attribute of class
print(obj.attr2)

#self and constractor used class
class Person:
    #init constractor
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def desc(self):
        a = f"Hi, I'am {self.name}, I am  { self.age } years old. thank You"
        return a

person = Person('Ismail','27')
print(person.desc())
