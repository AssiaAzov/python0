# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
# о том что машина поехала, остановилась, повернула(куда)

class TownCar:

    def __init__(self, color, name):
        self.color = color
        self._name = name
        self._speed = 100
        self._is_police = False

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Стоп!')

    def turn(self, direction):
        print('Повернули на', direction)

    def get_speed(self):
        return '{} км/ч'.format(self._speed)

    def get_is_police(self):
        return self._is_police


class SportCar:

    def __init__(self, color, name):
        self.color = color
        self._name = name
        self._speed = 435
        self._is_police = False

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Стоп!')

    def turn(self, direction):
        print('Повернули на', direction)

    def get_speed(self):
        return '{} км/ч'.format(self._speed)

    def get_is_police(self):
        return self._is_police


class WorkCar:

    def __init__(self, color, name):
        self.color = color
        self._name = name
        self._speed = 110
        self._is_police = False

    def go(self):
        print('Поехали!')

    def stop(self):
        print('Стоп!')

    def turn(self, direction):
        print('Повернули на', direction)

    def get_speed(self):
        return '{} км/ч'.format(self._speed)

    def get_is_police(self):
        return self._is_police


class PoliceCar:

    def __init__(self, color, name):
        self.color = color
        self._name = name
        self._speed = 330
        self._is_police = True


    def go(self):
        print('Поехали!')

    def stop(self):
        print('Стоп!')

    def turn(self, direction):
        print('Повернули на', direction)

    def get_speed(self):
        return '{} км/ч'.format(self._speed)

    def get_is_police(self):
        return self._is_police


car1 = WorkCar('белая', 'ЗИЛ')
car1.go()
car1.turn('лево')
car1.stop()

car2 = SportCar('красная', 'Ferrari 458')
print(car2.get_speed())

car3 = TownCar('синяя', 'Daewoo Matiz')
car3.go()
print(car3.get_speed())

car4 = PoliceCar('черная', 'Audi R8')
if car4.get_is_police():
    car4.go()







