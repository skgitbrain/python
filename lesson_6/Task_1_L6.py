from time import sleep


class TrafficLight:
    __color = 'Красный'

    def running(self):
        while True:
            error = "светофор сломался!"
            self.__color = "Красный"
            print(self.__color)
            if self.__color != "Красный":
                print(error)
                break
            sleep(3)
            self.__color = "Жёлтый"
            print(self.__color)
            if self.__color != "Жёлтый":
                print(error)
                break
            sleep(2)
            self.__color = "Зелёный"
            print(self.__color)
            if self.__color != "Зелёный":
                print(error)
                break
            sleep(6)
            self.__color = "Жёлтый"
            print(self.__color)
            if self.__color != "Жёлтый":
                print(error)
                break
            sleep(2)


a = TrafficLight()
a.running()
