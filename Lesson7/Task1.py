from time import sleep


class TrafficLight:
    __color = {"\033[031m{}\033[0m".format('красный'): 7,
               "\033[033m{}\033[0m".format('желтый'): 2,
               "\033[032m{}\033[0m".format('зеленый'): 7}

    def running(self):
        for color, switching_time in self.__color.items():
            self.__color = color
            print(self.__color)
            sleep(switching_time)


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()
