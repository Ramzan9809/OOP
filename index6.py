#  Реализуйте класс MyString, который будет иметь следующие методы: метод reverse(),
#  который параметром принимает строку, а возвращает ее в перевернутом виде, метод ucFirst(),
#  который параметром принимает строку, а возвращает эту же строку,
#  сделав ее первую букву заглавной и метод ucWords,
#  который принимает строку и делает заглавной первую букву каждого слова этой строки.

class MyString:
    def __init__(self, str):
        self.str = str

    def reverse(self):
        return self.str[::-1]

    def ucFirst(self):
        return self.str.capitalize()
    
    def ucWords(self):
        return ' '.join(word.capitalize() for word in self.str.split())


# string = MyString('Google')
# print(string.reverse())

# 1)  Создать класс Car в пакете com.company.vehicles, Engine в пакете com.company.details и 
# Driver в пакете com.company.professions.
# 2) Класс Driver содержит поля - ФИО, стаж вождения.
# 3) Класс Engine содержит поля - мощность, производитель.
# 4) Класс Car содержит поля - марка автомобиля, класс автомобиля, вес, водитель типа Driver,
#  мотор типа Engine. Методы start(), stop(), turnRight(), turnLeft(), которые выводят на печать: "Поехали",
#  "Останавливаемся", "Поворот направо" или "Поворот налево". А также метод toString(),
#  который выводит полную информацию об автомобиле, ее водителе и моторе. 
# 5)Создать производный от Car класс  - Lorry (грузовик), характеризуемый также грузоподъемностью кузова.
# 6) Создать производный от Car класс - SportCar, характеризуемый также предельной скоростью.
# 7) Пусть класс Driver расширяет класс Person.

class Driver:
    def __init__(self, name, staj):
        self.name = name
        self.staj = staj 

class Engine:
    def __init__(self, power, author):
        self.power = power
        self.author = author  

class Car:
    def __init__(self, brand, clas, weight, driver, engine):
        self.brand = brand
        self.clas = clas
        self.weight = weight
        self.driver = driver  
        self.engine = engine 

    def start(self):
        return "Поехали"
    
    def stop(self):
        return "Останавливаемся"

    def turnRight(self):
        return "Поворот направо"
    
    def turnLeft(self):
        return "Поворот налево"

    def toString(self):
        return f'Марка: {self.brand}, класс: {self.clas}, вес: {self.weight}, водитель: {self.driver.name}, мощность: {self.engine.power}'

class Lorry(Car):
    def __init__(self, brand, clas, weight, driver, engine, body_load_capacity):
        super().__init__(brand, clas, weight, driver, engine)
        self.body_load_capacity = body_load_capacity

    def toString(self):
        return f'Марка: {self.brand}, класс: {self.clas}, вес: {self.weight}, водитель: {self.driver.name}, мощность: {self.engine.power}, грузоподъёмность: {self.body_load_capacity}'

class SportCar(Car):
    def __init__(self, brand, clas, weight, driver, engine, max_speed):
        super().__init__(brand, clas, weight, driver, engine)
        self.max_speed = max_speed

    def toString(self):
        return f'Марка: {self.brand}, класс: {self.clas}, вес: {self.weight}, водитель: {self.driver.name}, мощность: {self.engine.power}, максимальная скорость: {self.max_speed}'


# driver1 = Driver("Иван", 10)
# driver2 = Driver("Мария", 5)
# engine1 = Engine(200, "Автор1")
# engine2 = Engine(300, "Автор2")

# car = Car("Toyota", "Седан", 1500, driver1, engine1)
# lorry = Lorry("Mercedes", "Грузовик", 5000, driver2, engine2, 10000)
# sport_car = SportCar("Ferrari", "Спортивный", 1200, driver1, engine2, 350)

# print(car.toString())  
# print(lorry.toString())  
# print(sport_car.toString())  

class Foo:
    count = 0
    def __init__(self):
        self.count += 1
    
obj = Foo()
# print(obj.count)

# Учитывая строку цифр, вы должны
# заменить любую цифру ниже 5 на "0",
# а любую цифру 5 и выше - на "1".
# Верните результирующую строку.

class Num:
    def __init__(self, num_str):
        self.num_str = num_str  

    def fun(self):
        result = ''
        for i in self.num_str:
            if int(i) < 5:
                result += '0'
            else:
                result += '1'
        return result  

num_obj = Num("1234567890")
# print(num_obj.fun())  


# Реализуйте класс Worker (Работник), который будет иметь следующие свойства: name (имя), 
# surname (фамилия), rate (ставка за день работы), days (количество отработанных дней). 
# Также класс должен иметь метод getSalary(), который будет выводить зарплату работника. 
# Зарплата - это произведение (умножение) ставки rate на количество отработанных дней days.

class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self. surname = surname
        self.rate = rate
        self.days = days

    def getSalary(self):
        return self.rate * self.days
    
rab = Worker('Sasha', 'Lohin', 3500, 5)
# print(rab.getSalary())

# Модифицируйте класс Worker из предыдущей задачи следующим образом: сделайте все его свойства приватными,
#  а для их чтения сделайте методы-геттеры

class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name        
        self.__surname = surname  
        self.__rate = rate       
        self.__days = days       

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_rate(self):
        return self.__rate

    def get_days(self):
        return self.__days

    def get_salary(self):
        return self.__rate * self.__days  

worker = Worker("Иван", "Иванов", 500, 20)

# print(worker.get_name())     
# print(worker.get_surname())  
# print(worker.get_rate())     
# print(worker.get_days())     
# print(worker.get_salary())  

# Реализуйте класс Validator, который будет проверять строки. 
# К примеру, у него будет метод isEmail параметром принимает строку и проверяет, 
# является ли она корректным емейлом или нет. Если является - возвращает true, если не является - то false.
#  Кроме того, класс будет иметь следующие методы: метод isDomain для проверки домена, 
# метод isDate для проверки даты и метод isPhone для проверки телефона

import re

class Validator:
    def __init__(self, text):
        self.text = text  

    def isEmail(self):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, self.text):
            return True
        else:
            return False
        
    def isDomain(self):
        pattern = r'^[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, self.text):
            return True
        else:
            return False
    
    def isDate(self):
        pattern = r'^\d{2}-\d{2}-\d{4}$'
        if re.match(pattern, self.text):
            return True
        else:
            return False
    
    def isPhone(self):
        pattern = r'^\+996 \d{3} \d{3} \d{3}$'
        if re.match(pattern, self.text):
            return True
        else:
            return False
        
v1 = Validator('ramzan@gmail.com')
v2 = Validator('gmail.com')
v3 = Validator('10-12-2024')
v4 = Validator('+996 554 977 013')

# print(v1.isEmail())
# print(v2.isDomain())
# print(v3.isDate())
# print(v4.isPhone())


# 1)  Создайте пример наследования, реализуйте класс Student и класс Aspirant, 
# аспирант отличается от студента наличием некой научной работы.
# 2) Класс Student содержит переменные: String firstName, lastName, group.
# А также, double averageMark, содержащую среднюю оценку.
# 3) Создать метод getScholarship() для класса Student, который возвращает сумму стипендии. 
# Если средняя оценка студента равна 5, то сумма 100 грн, иначе 80. Переопределить этот метод в классе Aspirant. 
# Если средняя оценка аспиранта равна 5, то сумма 200 грн, иначе 180.
# 4) Создать массив типа Student, содержащий объекты класса Student и Aspirant. 
# Вызвать метод getScholarship() для каждого элемента массива

class Student:
    def __init__(self, firstName, lastName, group, averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark

    def getScholarship(self):
        if self.averageMark == 5:
            return 100
        else:
            return 80

    def __str__(self):
        return f"Студент: {self.firstName} {self.lastName}, Группа: {self.group}, Средняя оценка: {self.averageMark}"

class Aspirant(Student):
    def __init__(self, firstName, lastName, group, averageMark, scientificWork):
        super().__init__(firstName, lastName, group, averageMark)
        self.scientificWork = scientificWork  # Добавляем научную работу

    def getScholarship(self):
        if self.averageMark == 5:
            return 200
        else:
            return 180

    def __str__(self):
        return f"Аспирант: {self.firstName} {self.lastName}, Группа: {self.group}, Средняя оценка: {self.averageMark}, Научная работа: {self.scientificWork}"

students = [
    Student("Иван", "Иванов", "1A", 4.8),
    Student("Мария", "Петрова", "1B", 5.0),
    Aspirant("Алексей", "Сидоров", "2A", 4.5, "Исследование в области физики"),
    Aspirant("Екатерина", "Смирнова", "2B", 5.0, "Научная работа по математике")
]

for student in students:
    print(student)
    print(f"Стипендия: {student.getScholarship()} грн\n")


# 1) Создать класс Animal и расширяющие его классы Dog, Cat, Horse.
# 2)Класс Animal содержит переменные food, location и методы makeNoise, eat, sleep.
# Метод makeNoise, например, может выводить на консоль "Такое-то животное спит". 
# 3)Dog, Cat, Horse переопределяют методы makeNoise, eat.
# 4)Добавьте переменные в классы Dog, Cat, Horse, характеризующие только этих животных.
# 5)Создайте класс Ветеринар, в котором определите метод void treatAnimal(Animal animal). 
# Пусть этот метод распечатывает food и location пришедшего на прием животного.
# 6)В методе main создайте массив типа Animal, в который запишите животных всех имеющихся у вас типов. 
# В цикле отправляйте их на прием к ветеринару.


class Animal:
    def __init__(self, food, location):
        self.food = food      
        self.location = location

    def makeNoise(self):
        print(f"Это животное издает звук.")

    def eat(self):
        print(f"Это животное ест {self.food}.")

    def sleep(self):
        print(f"Это животное спит.")

class Dog(Animal):
    def __init__(self, food, location, breed):
        super().__init__(food, location) 
        self.breed = breed  

    def makeNoise(self):
        print("Собака гавкает.")

    def eat(self):
        print(f"Собака ест {self.food}.")

class Cat(Animal):
    def __init__(self, food, location, color):
        super().__init__(food, location)  
        self.color = color  

    def makeNoise(self):
        print("Кошка мяукает.")

    def eat(self):
        print(f"Кошка ест {self.food}.")

class Horse(Animal):
    def __init__(self, food, location, speed):
        super().__init__(food, location) 
        self.speed = speed  

    def makeNoise(self):
        print("Лошадь ржет.")

    def eat(self):
        print(f"Лошадь ест {self.food}.")

class Veterinarian:
    def treatAnimal(self, animal):
        print(f"Лечение животного с едой: {animal.food} и местом: {animal.location}")


animals = [
    Dog("корм", "дом", "лабрадор"),
    Cat("рыбу", "квартира", "черный"),
    Horse("сено", "стадо", "60 км/ч")
]

vet = Veterinarian()

for animal in animals:
    vet.treatAnimal(animal)
    animal.makeNoise()
    animal.eat()
    animal.sleep()
    print("")  







