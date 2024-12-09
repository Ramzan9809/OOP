class Student:
    def __init__(self, name, class_name):
        self.name = name 
        self.class_name = class_name 
        self.grades = {} 
    
    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            if subject not in self.grades:
                self.grades[subject] = []
            self.grades[subject].append(grade)
        else:
            print(f'ошибка, оценка должна быть от 1 до 100')
    
    def get_average(self, subject=None):
        if subject:
            if subject in self.grades:
                return round(sum(self.grades[subject]) / len(self.grades[subject]), 2)
            else:
                return 0.0
        else:
            all_grades = [grade for grades in self.grades.values() for grade in grades]
            return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0.0
    
    def print_student_info(self):
        print(f'Студент {self.name}')
        print(f'Класс {self.class_name}')
        print(f'Средние баллы:')
        for subject, grades in self.grades.items():
            print(f"- {subject}: {self.get_average(subject)}")


class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
    
    def assign_grade(self, student, subject, grade):
        if subject in self.subjects:
            student.add_grade(subject, grade)
        else:
            print('Ошибка, учитель по другим предметам')
    
    def print_teacher_info(self):
        print(f'Учитель {self.name}')
        print(f'Преподает предметы: ') 
        for subject in self.subjects:
            print(f"- {subject}")
    

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f'удален {student_name}')
            else:
                print("не найден")
    
    def print_class_info(self):
        print(f'класс {self.name}')
        for student in self.students:
            print(f'{student.name}: средний балл = {student.get_average()}')

class School:
    def __init__(self):
        self.teachers = []
        self.classes = []
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def add_class(self, classroom):
        self.classes.append(classroom)
    
    def find_teacher(self, name):
        for teacher in self.teachers:
            if teacher.name == name:
                teacher.print_teacher_info()
            else:
                print("не найден")
    
    def find_class(self, name):
        for classroom in self.classes:
            if classroom.name == name:
                classroom.print_class_info()
            else:
                print("не найден")
    
    def print_school_info(self):
        print(f'Школа ')
        print(f'Учителя ')
        for teacher in self.teachers:
            print(f"{teacher.name}: {','.join(teacher.subjects)}")
        print('классы:')
        for classroom in self.classes:
            print(f"{classroom.name}")

# student1 = Student('Matai', '10д')
# student2 = Student('Гена', '11а')
# student3 = Student('Бек', '11а')
# teacher1 = Teacher('Азамат Айталиев', ['Русский язык', "Литература"])
# teacher2 = Teacher('Григорий Измаилов', ['Математика', "Геометрия"])
# class10D = Classroom('10д')
# class11A = Classroom('11а')
# class10D.add_student(student1)
# class11A.add_student(student2)
# class11A.add_student(student3)
# teacher1.assign_grade(student1, 'Литература', 5)
# teacher1.assign_grade(student3, 'Литература', 66)
# teacher2.assign_grade(student2, 'Математика', 76)
# school = School()
# school.add_teacher(teacher1)
# school.add_teacher(teacher2)
# school.add_class(class10D)
# school.add_class(class11A)
# school.print_school_info()
# class11A.print_class_info()
# class10D.print_class_info()
# teacher1.print_teacher_info()
# student1.print_student_info()


 # Задача: Управление зоопарком

# Создайте программу, которая моделирует работу зоопарка. В зоопарке есть животные разных видов,
#  каждый вид имеет уникальные характеристики, а сотрудники зоопарка ухаживают за ними.

# 1. Класс Animal: name, species (вид животного, строка),
#  age,health (hp, от 0 до 100, по умолчанию 100).


#  Методы: feed(food) — увеличивает уровень здоровья животного в зависимости от типа еды:
#  “трава” добавляет 5;
#  “мясо” добавляет 10;
#  любой другой вид еды добавляет 2.
#  print_info() — выводит информацию о животном: имя, вид, возраст и уровень здоровья.

# 2. Класс ZooKeeper: name, responsibilities (список видов животных, за которыми отвечает сотрудник).

#  Методы: care_for_animal(animal, food) — ухаживает за животным: кормит его и выводит сообщение о том,
#  как улучшилось его здоровье. Если вид животного не входит в список responsibilities,
#  выводится сообщение об ошибке.
#  print_info() — выводит имя сотрудника и список животных, за которыми он отвечает.

# 3. Класс Zoo: animals (список объектов класса Animal),
#  • zookeepers (список объектов класса ZooKeeper).

#  Методы:
#   add_animal(animal) — добавляет животное в зоопарк.
#  add_zookeeper(zookeeper) — добавляет смотрителя в зоопарк.
#  feed_all_animals(food) — кормит всех животных указанной едой.
#  print_zoo_info() — выводит список всех животных с их статусами и список сотрудников с их обязанностями.

 
# class Animal:
#     def __init__(self, name, species, age, hp=100):
#         self.name = name 
#         self.species = species
#         self.age = age
#         self.hp = hp

#     def feed(self, food):
#         if food == 'Трава':
#             self.hp += 5
#         elif food == 'Мясо':
#             self.hp += 10
#         else:
#             self.hp += 2

#     def print_info(self):
#         return f'Имя: {self.name}, вид: {self.species}, возраст: {self.age}, уровень здоровья: {self.hp}'
    
# class ZooKeeper(Animal):
#     def __init__(self, name, responsibilities):
#         self.name = name
#         self.responsibilities = [Animal]

#     def care_for_animal(self, animal, food, hp):
#         for animal in self.responsibilities:
#             if self.hp < 100:
#                 return animal.feed()
#             else:
#                 print('Ошибка') 
#             return f'У {self.name} вырос уровень здоровья: {self.hp}'
        
#     def print_info(self):
#          return f'Сотрудник: {self.name}, животные: {self.responsibilities}'
    
# class Zoo(Animal, ZooKeeper):
#     def __init__(self, animals, zookeepers):
#         self.animals = [Animal]
#         self.zookeepers = [ZooKeeper]
        
#     def add_animal(self, name, species, animal, age, hp):
#         animal = {
#             'name': name,
#             'species': species,
#             'age': age,
#             'hp': hp
#         }
#         self.animals.append(animal)
#         print(f'Животное {self.name} {self.species} {self.age} {self.hp} добавлено в зоопарк.')

#     def add_zookeepers(self, name, responsibilities, zookeeper):
#         zookeeper = {
#             'name': name,
#             'responsibilities': responsibilities
#         }
#         self.zookeepers.append(zookeeper)
#         print(f'Сотрудник {self.name} {self.responsibilities} добавлено в зоопарк.')

#     def feed_all_animals(self, responsibilities):
#         return self.responsibilities.feed()
    
#     def print_zoo_info(self):
#         return f'{self.animals.print_info()}. {self.zookeepers.print_info()}'


class Animal:
    def __init__(self, name, species, age, hp=100):
        self.name = name
        self.species = species
        self.age = age
        self.hp = hp

    def feed(self, food):
        """Метод для кормления животного и увеличения его уровня здоровья."""
        if food == 'Трава':
            self.hp += 5
        elif food == 'Мясо':
            self.hp += 10
        else:
            self.hp += 2

    def print_info(self):
        """Метод для вывода информации о животном."""
        return f'Имя: {self.name}, вид: {self.species}, возраст: {self.age}, уровень здоровья: {self.hp}'
    
class ZooKeeper:
    def __init__(self, name, responsibilities=None):
        if responsibilities is None:
            responsibilities = []
        self.name = name
        self.responsibilities = responsibilities  # Список животных, за которыми ухаживает смотритель

    def care_for_animal(self, animal, food):
        """Метод для кормления животного и восстановления его здоровья."""
        animal.feed(food)
        print(f'{self.name} покормил {animal.name} {food}. Уровень здоровья: {animal.hp}')
        
    def print_info(self):
        """Метод для вывода информации о смотрителе."""
        return f'Сотрудник: {self.name}, животные под его заботой: {[animal.name for animal in self.responsibilities]}'

class Zoo:
    def __init__(self):
        self.animals = []  # Список животных в зоопарке
        self.zookeepers = []  # Список смотрителей

    def add_animal(self, name, species, age, hp=100):
        """Метод для добавления животного в зоопарк."""
        animal = Animal(name, species, age, hp)
        self.animals.append(animal)
        print(f'Животное {name} {species} {age} лет добавлено в зоопарк.')

    def add_zookeeper(self, name, responsibilities=None):
        """Метод для добавления смотрителя в зоопарк."""
        if responsibilities is None:
            responsibilities = []
        zookeeper = ZooKeeper(name, responsibilities)
        self.zookeepers.append(zookeeper)
        print(f'Сотрудник {name} добавлен в зоопарк.')

    def feed_all_animals(self, food):
        """Метод для кормления всех животных в зоопарке."""
        for animal in self.animals:
            animal.feed(food)
            print(f'{animal.name} покормлен. Текущий уровень здоровья: {animal.hp}')

    def print_zoo_info(self):
        """Метод для вывода информации обо всех животных и смотрителях в зоопарке."""
        animals_info = "\n".join([animal.print_info() for animal in self.animals])
        zookeepers_info = "\n".join([zookeeper.print_info() for zookeeper in self.zookeepers])
        return f'Животные в зоопарке:\n{animals_info}\n\nСмотрители:\n{zookeepers_info}'

# Пример использования

zoo = Zoo()

# Добавление животных
zoo.add_animal("Лев", "Плотоядное", 5)
zoo.add_animal("Слон", "Млекопитающее", 10)
zoo.add_animal("Попугай", "Птица", 3)

# Добавление смотрителей
zoo.add_zookeeper("Иван", responsibilities=[zoo.animals[0], zoo.animals[1]])  # Иван ухаживает за Львом и Слоном
zoo.add_zookeeper("Мария", responsibilities=[zoo.animals[2]])  # Мария ухаживает за Попугаем

# Кормление животных
zoo.feed_all_animals("Трава")  # Все животные получат траву

# Вывод информации о зоопарке
print(zoo.print_zoo_info())

# Смотрители кормят животных по отдельности
zoo.zookeepers[0].care_for_animal(zoo.animals[0], "Мясо")  # Иван кормит Льва мясом
zoo.zookeepers[1].care_for_animal(zoo.animals[2], "Трава")  # Мария кормит Попугая травой
