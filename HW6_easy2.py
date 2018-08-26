
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Cars:

    def __init__(self, color, name):
        self.color = color
        self._name = name
        self._turn_on()

    def _turn_on(self):
        print('{} заводится...'.format(self._name))

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


class TownCar(Cars):

    def __init__(self, color, name):
        super().__init__(color, name)
        self._speed = 100
        self._is_police = False


class SportCar(Cars):

    def __init__(self, color, name):
        super().__init__(color, name)
        self._speed = 435
        self._is_police = False


class WorkCar(Cars):

    def __init__(self, color, name):
        super().__init__(color, name)
        self._speed = 110
        self._is_police = False


class PoliceCar(Cars):

    def __init__(self, color, name):
        super().__init__(color, name)
        self.speed = 330
        self._is_police = True


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




