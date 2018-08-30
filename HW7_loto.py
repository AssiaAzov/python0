# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается
# Побеждает тот, кто первый закроет все числа на своей карточке.


import random

len_str = 9
count_str = 3
num_in_line = 5
count_numbers = 15
card_name1 = 'Ваша карточка'
card_name2 = 'Карточка компьютера'

class Card:

    def __init__(self, card_name):
        self._card = []                            #создаем пустую карточку

    # генерируем карточку
    def _generation_card(self,card_name):
        self.set_numbers = set()                      #создаем множество номеров
        while len(self.set_numbers) < count_numbers:
            self.set_numbers.add(random.randint(1,90))
        self.set_numbers = list(self.set_numbers)     #переделываем множество в список чтобы удалять использованный номер
        for _ in range(count_str):
            self.line = []
            while len(self.line) < num_in_line:
                elem = random.choice(list(self.set_numbers))
                self.line.append(elem)
                self.set_numbers.remove(elem)
            self.line = list(self.line + [' ' for _ in range(len_str - num_in_line)]) #дозаполняем пробелами строку
            random.shuffle(self.line)                                #перемешиваем строку
            self._card.append(self.line)                             #добавляем в карточку получившуюся строку
        return self._card

    #выводим карточку на экран
    def _print_card(self,card_name):
        print('{:-^26} '.format(card_name))
        for line in self._card:
            line_str = [str(elem).rjust(2) for elem in line]
            print(' '.join(line_str))
        print('{:-^26}\n'.format('-'))



class Game:

    def __init__(self, card_name1 = 'Ваша карточка', card_name2 = 'Карточка компьютера'):
        self.result = True
        self.list_numbers = [i for i in range(1, 91)]                  #создаем мешок с невторимыми бочонками
        self._score1 = 0
        self._score2 = 0
        self.player1 = Card(card_name1)
        self.player2 = Card(card_name2)
        self._card1 = self.player1._generation_card(card_name1)
        self.player1._print_card(card_name1)                           #печатаем карту одного
        self._card2 = self.player2._generation_card(card_name2)
        self.player2._print_card(card_name2)                           #печатаем карту второго
        while True:
            self.get_num()
            self._comp_go(self._card2)
            self.choice(self._card1)
            if self.result == False:                                  #выходим из игры, если player накосячил
                break
            self.player1._print_card(card_name1)                      #вывели снова карточки и проверили счет
            self.player2._print_card(card_name2)
            if self._score1 == 15 and self._score2 == 15:
                print('Ничья!')
                break
            elif self._score1 == 15:
                print('Победила {}!'.format(card_name1))
                break
            elif self._score2 == 15:
                print('Победила {}!'.format(card_name2))
                break



    # достаем бочонок, объявляем и удаляем из мешка
    def get_num(self):
        self.new_num = random.choice(self.list_numbers)
        print('Номер {}!'.format(self.new_num))
        self.list_numbers.remove(self.new_num)

     # выбор пользователя и проверка выбора + вывод на экран карточки после зачеркивания
    def choice(self, card):
        self._choice = input('Зачеркнуть цифру? (y/n) ')
        if self._choice != 'y' and self._choice != 'n':                    #если ввели что-то не то, предлагаем ввести еще раз
            self._choice = input('Ответ должен быть y или n! Введите еще раз:')
        if self._choice == 'y':
            k = 0
            for i, line in enumerate(card):
                if self.new_num in line:
                    ind = line.index(self.new_num)                #находим индекс эл в строке и заменяем его на -
                    line[ind] = '-'
                    k += 1
                    self._score1 += 1
            if k == 0:
                print('Вы проиграли!')
                self.result = False
        elif self._choice == 'n':
            for i, line in enumerate(card):
                if self.new_num in line:
                    print('Вы проиграли!')
                    self.result = False
        return self.result


    # ход компа автоматический
    def _comp_go(self, card):
        k = 0
        for i, line in enumerate(card):
            if self.new_num in line:
                ind = line.index(self.new_num)
                line[ind] = '-'
                k += 1
                self._score2 += 1




game = Game()
