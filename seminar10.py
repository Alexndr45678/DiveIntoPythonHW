'''Доработать задачи 5-6. Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов)
    и параметры для этого типа.
    
- Внутри класса создайте экземпляр на основе переданного типа и
    верните его из класса-фабрики.
    
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.'''

class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

class Horse(Animal):
    def __init__(self, name, age, speed) -> None:
        super().__init__(name, age)
        self.speed = speed
    
    def get_speed(self):
        return self.speed

class Bird(Animal):
    def __init__(self, name, age, wingspan) -> None:
        super().__init__(name, age)
        self.wingspan = wingspan
    
    def get_wingspan(self):
        return int(self.wingspan)
    
class Cat(Animal):
    def __init__(self, name, age, color) -> None:
        super().__init__(name, age)
        self.color = color
        
    def get_color(self):
        return self.color
    

class Fabric:
    def __init__(self, type: Animal, name, age, uniq) -> None:
        self.type = type
        self.name = name
        self.age = age
        self.uniq = uniq
        
    def class_maker(self):
        animal_list = ["Horse", "Bird", "Cat"]
        
        tmp = self.type(self.name, self.age, self.uniq)
        return tmp


test1 = Fabric(Cat, "Пушок", 7, "Серый").class_maker()
print(test1.get_name())
print(test1.get_age())
print(test1.get_color())
print()
test2 = Fabric(Bird, "Кеша", 2, 40).class_maker()
print(test2.get_name())
print(test2.get_age())
print(test2.get_wingspan())
print()
test3 = Fabric(Horse, "Версаль", 12, 60).class_maker()
print(test3.get_name())
print(test3.get_age())
print(test3.get_speed())