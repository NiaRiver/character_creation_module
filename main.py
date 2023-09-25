"""This module adds Character classes and derived classes.

Such as Warrior, Mage, And Healer with different realisation of skills
like attack, deffence and special skill.

Also this module have function for
stating training(see start_training.__doc__)
and for choosing characters name and class
(see choice_char_class.__doc__).
"""
from random import randint
from graphic_arts.start_game_banner import run_screensaver
ON_OFF = {
        'X': True,
        'Q': False,
        'x': True,
        'q': False
    }
DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    """Base class for all characters with some constants and methods."""

    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name) -> None:
        """Initialise base character object."""
        self.name = name

    def attack(self):
        """Call function that use 'Attack' skill for base object."""
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанес противнику урон, равный {value_attack}')

    def defence(self):
        """Call function that use 'Defence' skill for base object."""
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} ед. урона.'

    def special(self):
        """Call function that cast special skill for base object."""
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')

    def __str__(self):
        """Describe character object.

        Displays name of class and description
        from the constant variable in class
        """
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    """Class Warrior derived from class Character."""

    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    """Class Mage derived from class Character."""

    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    """Class Healer derived from class Character."""

    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def choice_char_class(char_name: str) -> Character:
    """Implement choosing game character operation."""
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    approve_choice: str = None

    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character: Character) -> bool:
    """Implement a training function for the game."""
    commands = {
        'attack': character.attack,
        'defence': character.defence,
        'special': character.special
    }
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            print(commands[cmd]())
        else:
            print('Такой команды нет. Попробуй снова!!!')


def play():
    """Start game."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'{char_name}')
    print(f'Сейчас твоя выносливость — {DEFAULT_STAMINA}, '
          f'атака — {DEFAULT_ATTACK} и защита — {DEFAULT_ATTACK}')
    print('Ты можешь выбрать один из трёх путей силы:')
    char_class = choice_char_class(char_name)
    start_training(char_class)


def main():
    """Start main UI function."""
    while True:
        run_screensaver()
        key = input('Если Хотите начать нажмите X/x,'
                    'если хотите уйти нажмите Q/q:')
        if key not in ON_OFF:
            continue
        elif ON_OFF[key]:
            play()
        else:
            print('До скорого!!!')


if __name__ == '__main__':
    main()
