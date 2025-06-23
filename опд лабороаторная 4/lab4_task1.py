class Vehicle:
    """Базовый класс для всех транспортных средств."""

    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства
        :param model: Модель
        :param year: Год выпуска
        """
        self._brand = brand  # Защищенный атрибут (инкапсуляция для возможного наследования)
        self._model = model
        self.year = year
        self._mileage = 0  # Пробег в км (инкапсулирован, т.к. изменяется только через методы)

    @property
    def brand(self) -> str:
        """Возвращает марку транспортного средства."""
        return self._brand

    @property
    def model(self) -> str:
        """Возвращает модель транспортного средства."""
        return self._model

    def drive(self, distance: int) -> None:
        """
        Увеличивает пробег транспортного средства.

        :param distance: Расстояние в км
        :raises ValueError: Если расстояние отрицательное
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        self._mileage += distance

    def get_mileage(self) -> int:
        """Возвращает текущий пробег."""
        return self._mileage

    def __str__(self) -> str:
        """Строковое представление для пользователя."""
        return f"{self._brand} {self._model} ({self.year})"

    def __repr__(self) -> str:
        """Строковое представление для разработчика."""
        return f"Vehicle(brand='{self._brand}', model='{self._model}', year={self.year})"


class ElectricCar(Vehicle):
    """Класс электромобиля, наследуется от Vehicle."""

    def __init__(self, brand: str, model: str, year: int, battery_capacity: float):
        """
        Инициализация электромобиля.

        :param battery_capacity: Емкость батареи в кВт·ч
        """
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self._current_charge = 100.0  # Текущий заряд в % (инкапсулирован)

    @property
    def battery_capacity(self) -> float:
        """Возвращает емкость батареи."""
        return self._battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, value: float) -> None:
        """Устанавливает емкость батареи с проверкой."""
        if value <= 0:
            raise ValueError("Емкость батареи должна быть положительной")
        self._battery_capacity = value

    def charge(self, percent: float) -> None:
        """
        Заряжает электромобиль.

        :param percent: Процент заряда (0-100)
        :raises ValueError: Если процент вне допустимого диапазона
        """
        if not 0 <= percent <= 100:
            raise ValueError("Процент заряда должен быть от 0 до 100")
        self._current_charge = percent

    # Перегрузка метода drive (расширяет функциональность)
    def drive(self, distance: int) -> None:
        """
        Увеличивает пробег и уменьшает заряд батареи.

        Перегружен, потому что для электромобиля нужно учитывать расход заряда.
        На каждые 10 км расходуется 1% заряда.
        """
        super().drive(distance)  # Используем родительский метод
        charge_used = distance / 10
        self._current_charge = max(0, self._current_charge - charge_used)

    def get_charge(self) -> float:
        """Возвращает текущий заряд батареи."""
        return self._current_charge

    def __str__(self) -> str:
        """Строковое представление с информацией о заряде."""
        return f"{super().__str__()} (Заряд: {self._current_charge}%)"

    def __repr__(self) -> str:
        """Строковое представление для разработчика."""
        return (f"ElectricCar(brand='{self._brand}', model='{self._model}', "
                f"year={self.year}, battery_capacity={self._battery_capacity})")

# проверка:
if __name__ == "__main__":
    # Создаем обычное транспортное средство
    car = Vehicle("Toyota", "Camry", 2020)
    car.drive(150)
    print(car)
    print(repr(car))

    # Создаем электромобиль
    tesla = ElectricCar("Tesla", "Model S", 2022, 100)
    tesla.drive(50)
    print(tesla)
    print(repr(tesla))