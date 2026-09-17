#Getter and Setter
class Student:
    def __init__(self,name,age):
        self.__name =name
        self.__age =age
    def get_name(self):    #getter
        return self.__name
    def set_name(self,name):    #setter
        self.__name = name 
    def set_age(self,age):
        if isinstance(age,int):
            self.__age=age
        else:
            print("Age error")

s=Student("Pragathi",21)
print(s.get_name())
s.set_name("Prajwal")
print(s.get_name())
s.set_age(100)
print("Updated age:", s.get_age())


#Method Overloading
class Calculator:
    def add(self,a,b,c=0):
        print(a+b+c)
c=Calculator()
c.add(1,2)
c.add(1,2,3)


#Method Overrinding
class Animal:
    def make_sound(self):
        print("Animal is making sound")
class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        super().make_sound()
        print(f"{self.name} is Barking")
    def get_angry(self):
        super().make_sound()
        self.make_sound()

d = Dog("doggy")
d.make_sound()


#Abstract
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class Bike(Vehicle):
    def __init__(self,name):
        self.name=name
    def start_engine(self):
        print("starting engine")
b=Bike("Royal Enfield")
print(b.name)
