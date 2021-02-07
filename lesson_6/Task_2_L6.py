class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def calc_of_asphalt(self):
        weight = 25
        thickness = 5
        result_kg = self._length * self._width * weight * thickness
        result_t = result_kg / 1000
        return result_t


road_1 = Road(20, 5000)
print(road_1.calc_of_asphalt())
