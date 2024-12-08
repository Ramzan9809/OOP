# ООП - объктно-ориентированное програмирование
    # класс, атрибуты, экземпляры, конструкторы, магические методы
# 1 наследование
# 2 инкапсуляция
# 3 полиморфизм

class Student():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.books = []
        self.knowledge = 0
        self.is_ready_to_work = False
        self.launguages = {}

    def add_points(self, points):
        self.knowledge += points
        if self.knowledge >= 1000:
            # print('Студент готов к работе')
            self.is_ready_to_work = True


    def read_book(self, book):
       self.books.append(book)
       self.add_points(100)


    def do_homework(self):
        self.add_points(10)


    def do_project(self):
        self.add_points(50)


    def learn_new_language(self, lang, points):
        if points < 1 or points > 100:
            raise ValueError
        else:
            self.launguages[lang] = points
            self.add_points(points)


    def info_about(self):
        return f'Меня зовут {self.name} {self.lastname}\nЯ прочитал: {self.books}\nМои баллы: {self.knowledge}\nЯ знаю: {self.launguages}\nГотовность к работе: {self.is_ready_to_work}'


kuma = Student('Kuma', 'Baltozar')
kuma.read_book('Основы веб разроботки')
kuma.read_book('Python 2023')
kuma.read_book('Чистая архетектура')
kuma.read_book('Основы JS')
kuma.do_homework()
kuma.do_homework()
kuma.do_project()
kuma.do_project()
kuma.do_project()
kuma.learn_new_language('JS', 100)
kuma.learn_new_language('Python', 100)
kuma.learn_new_language('HTML', 50)
kuma.learn_new_language('CSS', 50)
kuma.learn_new_language('Boostrap 4', 50)
kuma.learn_new_language('Django', 100)
kuma.learn_new_language('SQL', 100)
# print(kuma.info_about())


# Наследование


class Animal:  # родительский класс
    def __init__(self, name, age, color, hp=100, damage=0):
        self.name = name
        self.age = age
        self.color = color
        self.hp = hp
        self.damage = damage

    def set_damage(self):
        return self.damage
    
    def get_damage(self, value):
        self.hp -= value
        if self.hp <= 0:  
            self.hp = 0  
            print(f'{self.name} сдохл(-a)')

    def info(self):
        return f'{self.name} {self.age} {self.color}'
    
    def edit_age(self, newAge):
        if newAge < 0 or newAge > 20:
            raise ValueError('Возраст только от 1 до 20')
        else:
            self.age = newAge 

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value > 0 and value < 21:
            self.__age = value

class Cat(Animal):  # дочерний класс
    def sound(self):
        return 'мяу мяу'
    
    def get_damage(self, value):
        super().get_damage(value)
        if self.hp > 0:  
            print(f"Ах ты сабака сутулая! У меня осталось hp: {self.hp}")

class Dog(Animal):  # дочерний класс
    def sound(self):
        return 'гав гав'
    
    def get_damage(self, value):
        super().get_damage(value)
        if self.hp > 0:  
            print(f"Кот блохастый! У меня осталось hp: {self.hp}")


cat1 = Cat('Murzik', 2, 'orange', damage=20)
dog1 = Dog('Recks', 5, 'brown', damage=30)

print(cat1.info())
print(dog1.info())

cat1.get_damage(dog1.set_damage())  
cat1.get_damage(dog1.set_damage())  

dog1.get_damage(cat1.set_damage())  
dog1.get_damage(cat1.set_damage())  
dog1.get_damage(cat1.set_damage())  
dog1.get_damage(cat1.set_damage())  
dog1.get_damage(cat1.set_damage())  




