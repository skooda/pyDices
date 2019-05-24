import random

""" Representing one dice """
class Dice(object):
    def __init__(self, sides: int = 6):
        self.sides = 6

        self.set_random_function(random.randint)
        self.roll()

    def set_random_function(self, f):
        self._randint = f
        return self

    def roll(self):
        self.value = self._randint(1, self.sides)
        return self

    def __repr__(self):
        return "⚀⚁⚂⚃⚄⚅"[self.value - 1]

    def __str__(self):
        return "123456"[self.value - 1]

    def __int__(self):
        return int(self.__str__())