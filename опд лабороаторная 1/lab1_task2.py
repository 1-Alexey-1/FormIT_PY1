from task_1 import Car, Book, BankAccount

if __name__ == "__main__":
    # Создаем экземпляры классов
    book = Book("1984", "George Orwell", 328)
    car = Car("Toyota", 220, 50.0)
    account = BankAccount("Alice", 100.0)

    # Проверка методов с обработкой исключений
    try:
        # Попытка добавить отрицательное количество страниц в книгу
        book.add_pages(-50)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        # Попытка поехать на отрицательное расстояние
        car.drive(-100)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        # Попытка снять отрицательную сумму со счета
        account.withdraw(-30)
    except ValueError:
        print('Ошибка: неправильные данные')
