# ООП - объктно-ориентированное програмирование
    # класс, атрибуты, экземпляры, конструкторы, магические методы
# 1 наследование
# 2 инкапсуляция
# 3 полиморфизм

class Cat:
    def __init__(self, name, age, color, poroda): # конструктор init
        self.name = name # атрибуты класса
        self.age = age  # атрибуты класса
        self.color = color
        self.poroda = poroda

    # метод - функция внутри класса

    def sound(self):
        return 'мяу мяу'
    
    def info(self):
        return f'Имя: {self.name}, Возраст: {self.age}, {self.color}, {self.poroda}, {self.sound}'
    
cat = Cat('Murzik', 2, 'белая', 'сиамская') # экземпляр класса
cat2 = Cat('Vasyu', 2, 'рыжая', 'британская' ) # экземпляр класса

# print(cat.name, cat.age, cat.color, cat.poroda, cat.sound())
# print(cat2.info())



# class Car:
#     def __init__(self, brand, model, year, person, is_moving=False):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.person = person
#         self.is_moving = is_moving  

#     def is_going(self):
#         if self.is_moving: 
#             return 'В движении'
#         else:
#             return 'Стоит на месте'

#     def info(self):
#         return f'Марка: {self.brand}, модель: {self.model}, год выпуска: {self.year}, владелец: {self.person}, состояние: {self.is_going()}'

# car = Car('BMW', 'X5', 2017, 'Roma', True)
# print(car.info())



class Car:
    def __init__(self, brand, model, year, person, is_moving=False, mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.person = person
        self.is_moving = is_moving  
        self.mileage = mileage  

    def is_going(self):
        if self.is_moving: 
            return 'В движении'
        else:
            return 'Стоит на месте'

    def info(self):
        return f'Марка: {self.brand}, модель: {self.model}, год выпуска: {self.year}, владелец: {self.person}, состояние: {self.is_going()}, пробег: {self.mileage} км'

    def drive(self, distance):
        self.mileage += distance
        print(f'Пробег увеличен на {distance} км. Текущий пробег: {self.mileage} км')

    def stop(self):
        self.is_moving = False
        print(f'{self.brand} {self.model} остановился.')

    def rename(self, new_brand, new_model):
        self.brand = new_brand
        self.model = new_model
        print(f'Теперь автомобиль {self.brand} {self.model}.')

car = Car('BMW', 'X5', 2017, 'Roma', True)
# print(car.info())  # Информация о машине
# car.drive(100)     # Пробег увеличен
# print(car.info())  # Информация о машине после увеличения пробега

# car.stop()         # Остановка машины
# print(car.info())  # Информация о машине после остановки

# car.rename('Audi', 'Q7')  # Переименовываем машину
# print(car.info())  # Информация о машине после переименования


class Purse:
    def __init__(self, valuta, name='Неизвестный'):
        if valuta not in ('KGS', 'USD'):
            raise ValueError('Только KGS и USD')
        self.money = 0.00
        self.valuta = valuta
        self.name = name

    def info(self):
        return f'{self.name} у вас: {self.money} {self.valuta}'

    def deposit(self, amount):
        """Пополнение счета"""
        if amount <= 0:
            raise ValueError('Сумма должна быть положительной')
        self.money += amount
        print(f'Пополнено на {amount} {self.valuta}. Текущий баланс: {self.money} {self.valuta}')

    def withdraw(self, amount):
        """Снятие денег"""
        if amount <= 0:
            raise ValueError('Сумма должна быть положительной')
        if amount > self.money:
            raise ValueError('Недостаточно средств')
        self.money -= amount
        print(f'Снято {amount} {self.valuta}. Текущий баланс: {self.money} {self.valuta}')


kuma = Purse('KGS', 'Kuma')
print(kuma.info())
kuma.deposit(500)   # Пополнение на 500 KGS
kuma.withdraw(600)  # Снятие 200 KGS



