import numpy as np


class kansberekening:
    def __init__(self):
        self.total_stock = 416
        self.list_stock = []
        self.list_chance = []
        for i in range(0, 12):
            self.list_stock[i] = 32
            self.list_chance[i] = 1 / 13

    def total_cards(self):
        for i in range(0, 12):
            self.total_stock += self.list_stock[i]
        return self.total_stock

    def chance(self, value):
        p = self.list_stock[value] / self.total_cards()
        self.list_chance[value] = p
        return p

    def reset(self):
        for i in range(0, 12):
            self.list_stock[i] = 32

    def card_drawn(self, value):
        self.list_stock[value] -= 1
