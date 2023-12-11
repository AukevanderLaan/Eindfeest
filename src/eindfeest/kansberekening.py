import csv
import sys
import numpy as np
import pyqtgraph as pg
import pyvisa

from src.kaartteller import Ui_MainWindow
from PySide6 import QtWidgets


class kansberekening:
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.total_stock = 416
        self.list_stock = []
        self.list_chance = []
        for i in range(0, 12):
            self.list_stock[i] = 32
            self.list_chance[i] = 1 / 13

        self.ui.low_card_button.clicked.connect(self.low_card)
        self.ui.neutral_card_button.clicked.connect(self.neutral_card)
        self.ui.high_card_button.clicked.connect(self.high_card)

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
        
    @Slot
    def neutral_card(self):

    @slot 
    def high_card(self):

