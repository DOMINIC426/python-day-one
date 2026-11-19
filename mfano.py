import sample

class Animal:

    def __init__(self,name:str,age:int,books:list):
        self.name=name
        self.age=age

    def greetings()->str:
        print("Hello World Welcome to the classes issues in Python")

    #creating the object 
animal = Animal("Dominic",39,["Physics","Biology","Mathematics"])  
print(animal.name)
print(sample.greeting())
print(animal.greetings())



class Dog(Animal):
    pass

dog = Dog("Mbwa",20,["am","jas"]);

    