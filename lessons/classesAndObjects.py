class Myclass:
    x=5

p1 = Myclass()
print(p1.x)

#init allows us to initialize values in a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person('John', 87)
print(p2.name)
print(p2.age)

name = input('Enter your name: ')
age = int(input('Enter your age: '))
p3 = Person(name, age)
print(p3.name)
print(p3.age)

#pass allows you to bypass any error
class Sample:
    pass

del p2
#the next statement won't work because the object is deleted
print(p2)