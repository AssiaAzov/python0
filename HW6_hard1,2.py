# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Toys:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def who_am_i(self):
        print('Получился {} {} {}'.format(self.type, self.name, self.color))

class Animal(Toys):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = 'животное'
        self.who_am_i()


class Pers(Toys):

    def __init__(self, name, color):
        super().__init__(name, color)
        self.type = 'персонаж'
        self.who_am_i()


class Factory:

    def create(self, name, color):
        self.choice = input('Выберите тип игрушки: животное или персонаж (1|2)')
        self._purchase()
        self._sewing()
        self._coloring()
        if self.choice == '1':
            print(Animal(name, color))
        elif self.choice == '2':
            print(Pers(name, color))

    def _purchase(self):
        print('Закупаем сырье...')

    def _sewing(self):
        print('Шьем...')

    def _coloring(self):
        print('Окрашиваем...')


factory = Factory()
factory.create('Чебурашка', 'коричневый')




