# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


import random

class Person:

    def __init__(self, name):
        self._name = name

    def go(self):                                                   #пишет нам чей ход
        print('Ходит {}'.format(self._name))

    def get_person_armor(self):                                    #возвращает показатель брони персонажа
        return self._armor

    def get_min_person_damade(self):                               #минимальное значение из диапазона урона
        return min(self._damage)

    def _calculate_damage(self, who_def):
        self._fortune = random.choice([0.5, 1, 2])                  #показатель удачи: повезло *2,никак *1, не повезло *0,5
        self.new_damage = random.choice(self._damage)               #вызываем рандомное значение урона из диапазона персоны
        self.damage_fortune = self.new_damage * self._fortune      #считаем удар с учетом удачи
        self.real_damage = round(self.damage_fortune / who_def.get_person_armor(), 2)#считаем нанесенный урон с учетом
        return self.real_damage                                                      # удачи и брони


    def attack(self, who_def, who_att):                             # сколько ед жизни осталось у атакованного
        self._attack = who_att._calculate_damage(who_def)
        print('{} нанес {} ед. урона'.format(who_att._name, self._attack))
        who_def._health = round(who_def._health - self._attack, 2)
        print('У {} осталось {} ед.жизни'.format(who_def._name, who_def._health))


class Player(Person):

    def __init__(self, name):
        super().__init__(name)
        self._health = 130
        self._armor = 1.2
        self._damage = [int(i) for i in range(55, 71)] #заводим диапазон значений урона


class Enemy(Person):

    def __init__(self, name):
        super().__init__(name)
        self._health = 160
        self._armor = 3.5
        self._damage = [int(i) for i in range(15, 26)]  #заводим диапазон значений урона


class Fight:

    def __init__(self, name1, name2 ):
        self.player = Player(name1)
        self.enemy = Enemy(name2)
        print('{} vs {}'.format(self.player._name, self.enemy._name))


    def battle(self):
        self.last_att = self.player
        while self.player._health > 0 and self.enemy._health > 0:
            if self.last_att == self.player:
                self.last_att.attack(self.enemy, self.player)
                # добавляем условие: если совсем не повезло и удар оказался меньше минимального, даем шанс еще раз ударить
                if self.player._calculate_damage(self.enemy) < self.player.get_min_person_damade():
                    self.last_att.attack(self.enemy, self.player)
                self.last_att = self.enemy
            else:
                self.last_att.attack(self.player, self.enemy)
                # добавляем условие: если совсем не повезло и удар оказался меньше минимального, даем шанс еще раз ударить
                if self.enemy._calculate_damage(self.enemy) < self.enemy.get_min_person_damade():
                    self.last_att.attack(self.player, self.enemy)
                self.last_att = self.player

        if self.player._health > 0:
            print('{} победил!'.format(self.player._name))
        else:
            print('{} победил!'.format(self.enemy._name))



game = Fight('Настя','Троль')
game.battle()


