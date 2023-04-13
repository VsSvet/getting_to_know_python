class IsPositiveInt:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.my_attr} должен быть натуральным числом")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    length, width = IsPositiveInt(), IsPositiveInt()

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def get_weight(self, __weight: int = 25, __thickness_canvas: float = 0.05):
        result = self.length * self.width * __weight * __thickness_canvas / 1000
        print(f"Для укладки полотна длиной {self.length}, шириной {self.width} и толщиной {__weight} метров, "
              f"потребуется {result} тонн асфальтобетонной смеси")
        return result


if __name__ == '__main__':
    road1 = Road(5000, 20)
    weight1 = road1.get_weight()
