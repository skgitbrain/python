class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"Машина марки {self.name} поехала")

    def stop(self):
        print(f"Машина марки {self.name} остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"Машина марки {self.name} повернула {self.direction}")

    def show_speed(self):
        print(f"Скорость машины марки {self.name} составляет {self.speed}")


class TownCar(Car):

    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Машина марки {self.name} {self.color} цвета превысила допустимую скорость в 60 км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Машина марки {self.name} {self.color} цвета превысила допустимую скорость в 40 км/ч")


class PoliceCar(Car):
    pass


r = PoliceCar("bmw", "black", 70, True)
r.go()
r.stop()
r.turn("Направо")
r.show_speed()
