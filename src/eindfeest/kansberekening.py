import csv
import sys
import numpy as np
import pyqtgraph as pg
import pyvisa

from eindfeest.kaartteller import Ui_MainWindow
from PySide6 import QtWidgets


class kansberekening:
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.list_start = []
        for i in range(0,2:)
            self.list_start.append(4)

        self.total_stock = 416
        self.list_stock = []
        self.list_chance = []
        for i in range(0, 12):
            self.list_stock.append(32)
            self.list_chance.append(1/13)

        self.ui.low_card_button.clicked.connect(self.low_card)
        self.ui.neutral_card_button.clicked.connect(self.neutral_card)
        self.ui.high_card_button.clicked.connect(self.high_card)

        self.show()

    @Slot
    def total_cards(self):
        for i in range(0, 12):
            self.total_stock += self.list_stock[i]
        return self.total_stock

    @Slot
    def chance(self, value):
        p = self.list_stock[value] / self.total_cards()
        self.list_chance[value] = p
        return p

    @slot
    def reset(self):
        for i in range(0, 12):
            self.list_stock[i] = 32

    @Slot
    def card_drawn(self, value):
        self.list_stock[value] -= 1
        

    @Slot
    def low_card(self):
        total = 0
        self.list_start[0] -= 1
        
        # counting total amount of cards
        for i in range(0,2):
            total += self.list_start[i]

        # calculating chance to get low card
        chance_low = self.list_start[0] / total

        # updates stock and chance
        self.ui.text_low.clear()
        self.ui.text_low.append(f"Aantal lage:{self.list_start[0]}")
        self.ui.text_low.append(f"Kans op hoog{chance_low}")


    @Slot
    def neutral_card(self):
        total = 0
        self.list_start[1] -= 1
        
        # counting total amount of cards
        for i in range(0,2):
            total += self.list_start[i]

        # calculating chance to get a neutral card
        chance_neutral = self.list_start[1] / total

        # updates stock and chance
        self.ui.text_neutral.clear()
        self.ui.text_neutral.append(f"Aantal middelste{self.list_start[1]}")
        self.ui.text_neutral.append(f"Kans op hoog{chance_neutral}")

    @slot 
    def high_card(self):
        total = 0
        self.list_start[2] -= 1

        # counting total amount of cards
        for i in range(0,2):
            total += self.list_start[i]

        # calculating chance to get a high hard
        chance_high = self.list_start[2] / total

        # updates stock and chance
        self.ui.text_high.clear()
        self.ui.text_high.append(f"Aantal hoge{self.list_start[2]}")
        self.ui.text_high.append(f"Kans op hoog{chance_high}")
