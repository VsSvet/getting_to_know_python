class NonNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.my_attr} должен быть натуральным числом")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class IsString:
    def __set__(self, instance, value):
        if not type(value) == str:
            raise TypeError(f"{self.my_attr} должен быть строкой")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    wage, bonus = NonNegative(), NonNegative()
    name, surname, position = IsString(), IsString(), IsString()

    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        """
        name - имя
        surname - фамилия
        position - должность
        wage - оклад
        bonus - премия
        """
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def get_full_name(self):
        """
        Получаем полное имя работника
        """
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        """
        Получаем общий доход работника
        """
        return self.bonus + self.wage


if __name__ == '__main__':
    person1 = Position('Светлана', 'Вострова', 'бариста', 30000, 10000)
    print(person1.get_full_name())
    print(f"{person1.position} {person1.get_total_income()}")
