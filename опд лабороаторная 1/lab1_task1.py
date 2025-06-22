# TODO: Подробно описать три произвольных класса


# TODO: описать класс

class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание объекта "Книга".

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages

    def is_long_book(self, threshold: int = 300) -> bool:
        """
        Проверяет, является ли книга длинной (по количеству страниц).

        :param threshold: Порог, после которого книга считается длинной (по умолчанию 300).
        :return: True, если книга длинная, иначе False.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.is_long_book()
        True
        """
        return self.pages > threshold

    def add_pages(self, additional_pages: int) -> None:
        """
        Добавляет страницы к книге.

        :param additional_pages: Количество добавляемых страниц.
        :raise ValueError: Если добавляемое количество страниц отрицательное.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.add_pages(50)
        """
        if not isinstance(additional_pages, int) or additional_pages <= 0:
            raise ValueError("Количество добавляемых страниц должно быть положительным целым числом")
        self.pages += additional_pages
# TODO: описать ещё класс
class Car:
    def __init__(self, brand: str, max_speed: int, fuel_level: float = 100.0):
        """
        Создание объекта "Автомобиль".

        :param brand: Марка автомобиля.
        :param max_speed: Максимальная скорость (км/ч).
        :param fuel_level: Уровень топлива в % (по умолчанию 100%).

        Примеры:
        >>> car = Car("Toyota", 220)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(max_speed, int) or max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным целым числом")
        if not isinstance(fuel_level, (int, float)) or fuel_level < 0 or fuel_level > 100:
            raise ValueError("Уровень топлива должен быть от 0 до 100%")

        self.brand = brand
        self.max_speed = max_speed
        self.fuel_level = float(fuel_level)

    def drive(self, distance: float) -> float:
        """
        Симуляция поездки. Уменьшает уровень топлива.

        :param distance: Расстояние в км.
        :return: Оставшийся уровень топлива.
        :raise ValueError: Если расстояние отрицательное или топлива недостаточно.

        Примеры:
        >>> car = Car("Toyota", 220, 50.0)
        >>> car.drive(100)
        30.0
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        fuel_consumption = distance * 0.2  # Условный расход топлива (20% на 100 км)
        if fuel_consumption > self.fuel_level:
            raise ValueError("Недостаточно топлива для поездки")
        self.fuel_level -= fuel_consumption
        return self.fuel_level

    def refuel(self, amount: float = 100.0) -> None:
        """
        Заправка автомобиля.

        :param amount: Количество добавляемого топлива (по умолчанию полный бак).
        :raise ValueError: Если количество топлива выходит за допустимые пределы.

        Примеры:
        >>> car = Car("Toyota", 220, 30.0)
        >>> car.refuel(20)
        """
        if amount <= 0:
            raise ValueError("Количество топлива должно быть положительным числом")
        if self.fuel_level + amount > 100:
            raise ValueError("Нельзя заправить больше 100%")
        self.fuel_level += amount
# TODO: и ещё один
class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0):
        """
        Создание объекта "Банковский счет".

        :param account_holder: Владелец счета.
        :param balance: Начальный баланс (по умолчанию 0.0).

        Примеры:
        >>> account = BankAccount("Alice")
        """
        if not isinstance(account_holder, str):
            raise TypeError("Имя владельца счета должно быть строкой")
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Баланс не может быть отрицательным")

        self.account_holder = account_holder
        self.balance = float(balance)

    def deposit(self, amount: float) -> float:
        """
        Внесение денег на счет.

        :param amount: Сумма для внесения.
        :return: Новый баланс.
        :raise ValueError: Если сумма отрицательная.

        Примеры:
        >>> account = BankAccount("Alice", 100.0)
        >>> account.deposit(50)
        150.0
        """
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия.
        :return: Новый баланс.
        :raise ValueError: Если сумма превышает баланс.

        Примеры:
        >>> account = BankAccount("Alice", 100.0)
        >>> account.withdraw(30)
        70.0
        """
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount
        return self.balance