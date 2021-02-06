from time import sleep


class TrafficLight:
    __color = 'красный'

    def running(self, color_2, color_3):
        error = "светфор сломался!"
        while True:
            print(self.__color)
            if self.__color != "красный":
                print(error)
                break
            sleep(3)
            self.color_2 = print(color_2)
            if color_2 != "желтый":
                print(error)
                break
            sleep(2)
            self.color_3 = print(color_3)
            if color_3 != "зеленый":
                print(error)
                break
            sleep(6)
            self.color_2 = print(color_2)
            sleep(2)


a = TrafficLight()
a.running("желтый", "зеленый")
