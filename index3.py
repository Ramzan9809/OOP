# Задача: Симулятор библиотеки 
# создать класс Book, с атрибутами:  title (название книги, строка), author (автор книги, строка),
#  year (год издания, число), is_available (доступна ли книга для выдачи, булево, по умолчанию True).
#  Методы: 
#     borrow(): если книга доступна, отмечает её как взятую (is_available = False) 
# и возвращает сообщение: "Вы взяли книгу <название>". Если недоступна, выводит: "Книга <название> сейчас недоступна.".
#  return_book(): отмечает книгу как доступную (is_available = True) и выводит: "Книга <название> возвращена.".
# создать класс Library, с атрибутами:
#  books (список объектов класса Book).
#  Методы:add_book(book): добавляет книгу в библиотеку.
#  remove_book(title): удаляет книгу по названию (если она есть в библиотеке).
#  list_available_books(): выводит список всех доступных книг с их названиями и авторами.
#  find_book(title): ищет книгу по названию и выводит информацию о ней (название, автор, год, доступность).


class Book:
    def __init__(self, title, author, year, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    def borrow(self):
        if self.is_available:  # RATATYPE
            self.is_available = False
            return f'Вы взяли книгу "{self.title}"!'
        else:
            return f'Книга "{self.title}" сейчас недоступна.'
        
    def return_book(self):
        self.is_available = True
        return f'Книга "{self.title}" возвращена.'

class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return f'Книга "{title}" удалена из библиотеки.'
        return f'Книги с названием "{title}" нет в библиотеке!'

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            return [f'"{book.title}" ({book.author})' for book in available_books]
        else:
            return 'Нет доступных книг.'

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                availability = 'доступна' if book.is_available else 'недоступна'
                return f'Книга "{book.title}" автор: {book.author}, год: {book.year}, доступность: {availability}'
        return f'Книги с названием "{title}" нет в библиотеке!'

book1 = Book('Гарри Поттер', 'Дж.К. Роулинг', 1997)
book2 = Book('Мастер и Маргарита', 'Михаил Булгаков', 1967)
bib = Library()

bib.add_book(book1)
bib.add_book(book2)

# print(bib.list_available_books())  # Список доступных книг
# print(bib.find_book('Гарри Поттер'))  # Поиск книги
# print(bib.remove_book('Гарри Поттер'))  # Удаление книги
# print(bib.list_available_books())  # Список доступных книг после удаления
# print(book1.borrow())  # Заимствование книги
# print(bib.list_available_books())  # Список доступных книг после заимствования



# Задача: Магазин покупок
# Создайте классы, которые симулируют процесс работы онлайн-магазина.
# Класс Product ,name (название товара, строка),price (цена товара, число), quantity (количество товара в наличии, число).
#  Методы: update_quantity(amount): обновляет количество товара (прибавляет или вычитает amount). 
#     is_available(): возвращает True, если товар в наличии (количество больше 0), иначе False.
# Класс ShoppingCart, items (список кортежей (product, quantity), представляющий товары в корзине).
#  Методы: add_product(product, quantity): добавляет товар в корзину, если он доступен в нужном количестве.
#  Уменьшает количество товара в product.quantity. Если товара недостаточно, выводит сообщение.
#  remove_product(product_name): удаляет товар из корзины и возвращает его количество обратно на склад.
#  get_total_price(): возвращает общую стоимость всех товаров в корзине.
#  checkout(): завершает покупку, выводит итоговую стоимость и очищает корзину.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount
        return self.quantity > 0

    def is_available(self):
        return self.quantity > 0
    
class ShoppingCart:
    def __init__(self):
        self.items = []  

    def add_product(self, product, quantity):
        if product.is_available() and product.quantity >= quantity:
            self.items.append((product, quantity))
            product.update_quantity(-quantity)
            return f'Товар "{product.name}" добавлен в корзину, количество: {quantity}'
        else:
            return f'Товара "{product.name}" недостаточно в наличии.'

    def remove_product(self, product_name):
        for item in self.items:
            product, quantity = item
            if product.name == product_name:
                self.items.remove(item)
                product.update_quantity(quantity)
                return f'Товар "{product_name}" удален из корзины, количество: {quantity} возвращено на склад.'
        return f'Товара с названием "{product_name}" нет в корзине.'

    def get_total_price(self):
        total_price = sum(product.price * quantity for product, quantity in self.items)
        return total_price

    def checkout(self):
        total_price = self.get_total_price()
        self.items.clear()  
        return f'Покупка завершена! Итоговая стоимость: {total_price}'

product1 = Product("Ноутбук", 50000, 10)
product2 = Product("Смартфон", 20000, 5)

cart = ShoppingCart()

# print(cart.add_product(product1, quantity=2))  
# print(cart.add_product(product2, quantity=3))  

# print(f"Общая стоимость товаров в корзине: {cart.get_total_price()}")

# print(cart.remove_product("Смартфон"))

# print(cart.checkout())
