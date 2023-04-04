class Road:
    """
    length - длина в метрах
    width - ширина в метрах
    """

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def get_weight(self, weight: int, thickness_canvas: float):
        """
        thickness_canvas - толщина дорожного полотна в метрах.
        weight - масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
        Нормы на расход асфальта кв метра, толщиной 1 см:
            Мелкозернистая тип А марка I  - 25,7 кг
            Мелкозернистая тип Б марка I, II — 24,5 кг
            Мелкозернистая тип В марка II — 24,9 кг
            Крупнозернистая марка I, II — 24,2 кг
            Песчаная тип Г марка II — 25,0 кг
            Песчаная тип Д марка II — 23,2 кг
            Щебеночно-мастичная-15 (ЩМА-15) — 25,8 кг
            Щебеночно-мастичная-20 (ЩМА-20)" - 25,7 кг
        """
        result = self._length * self._width * weight * thickness_canvas/1000

        print(f"Для укладки полотна длиной {self._length}, шириной {self._width} и толщиной {weight} метров, "
              f"потребуется {result} тонн асфальтобетонной смеси")
        return result


# 20м*5000м*25кг*0.05м = 125000 кг = 125 т
if __name__ == '__main__':
    road1 = Road(5000, 20)
    weight1 = road1.get_weight(25, 0.05)

