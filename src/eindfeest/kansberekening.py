import csv
import sys

import numpy as np
import pyqtgraph as pg
import pyvisa

from eindfeest.kaartteller import Ui_MainWindow


class kansberekening(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # filling starting list for stock
        self.list_start = []
        for i in range(0,2:)
            self.list_start.append(4)

        self.total_stock = 416
        self.list_stock = []
        self.list_chance = []
        for i in range(0, 12):
            self.list_stock.append(32)
            self.list_chance.append(1/13)

        self.ui.card_button_2.clicked.connect(self.card_2)
        self.ui.card_button_3.clicked.connect(self.card_3)
        self.ui.card_button_4.clicked.connect(self.card_4)
        self.ui.card_button_5.clicked.connect(self.card_5)
        self.ui.card_button_6.clicked.connect(self.card_6)
        self.ui.card_button_7.clicked.connect(self.card_7)
        self.ui.card_button_8.clicked.connect(self.card_8)
        self.ui.card_button_9.clicked.connect(self.card_9)
        self.ui.card_button_10.clicked.connect(self.card_10)
        self.ui.card_button_jack.clicked.connect(self.card_jack)
        self.ui.card_button_queen.clicked.connect(self.card_queen)
        self.ui.card_button_king.clicked.connect(self.card_king)
        self.ui.card_button_ace.clicked.connect(self.card_ace)
        self.ui.reset_button.clicked.connect(self.reset)
        self.show()

    @Slot()
    def total_cards(self):
        for i in range(0, 12):
            self.total_stock += self.list_stock[i]
        return self.total_stock

    @Slot()
    def reset(self):
        for i in range(0, 12):
            self.list_start[i] = 32

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
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total
            chance_5 = self.list_start[3] / total
            chance_6 = self.list_start[4] / total
            chance_7 = self.list_start[5] / total
            chance_8 = self.list_start[6] / total
            chance_9 = self.list_start[7] / total
            chance_10 = self.list_start[8] / total
            chance_jack = self.list_start[9] / total
            chance_queen = self.list_start[10] / total
            chance_king = self.list_start[11] / total
            chance_ace = self.list_start[12] / total
            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")


    @Slot
    def neutral_card(self):
        total = 0
        self.list_start[1] -= 1
        
        # counting total amount of cards
        for i in range(0,2):
            total += self.list_start[i]

            # calculating chance to get a neutral card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @slot 
    def high_card(self):
        total = 0
        self.list_start[2] -= 1

        # counting total amount of cards
        for i in range(0,2):
            total += self.list_start[i]

            # calculating chance to get a high hard
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @Slot()
    def card_5(self):
        if self.list_start[0] > 0:
            self.list_start[0] -= 1

            # counting total amount of cards
            total = self.total_cards()

            # calculating chance to get low card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @Slot()
    def card_6(self):
        if self.list_start[0] > 0:
            self.list_start[0] -= 1

            # counting total amount of cards
            total = self.total_cards()

            # calculating chance to get low card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @Slot()
    def card_7(self):
        if self.list_start[0] > 0:
            self.list_start[0] -= 1

            # counting total amount of cards
            total = self.total_cards()

            # calculating chance to get low card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @Slot()
    def card_8(self):
        if self.list_start[0] > 0:
            self.list_start[0] -= 1

            # counting total amount of cards
            total = self.total_cards()

            # calculating chance to get low card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @Slot()
    def card_9(self):
        if self.list_start[0] > 0:
            self.list_start[0] -= 1

            # counting total amount of cards
            total = self.total_cards()

            # calculating chance to get low card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @Slot()
    def card_10(self):
        if self.list_start[0] > 0:
            self.list_start[0] -= 1

            # counting total amount of cards
            total = self.total_cards()

            # calculating chance to get low card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @Slot()
    def card_jack(self):
        if self.list_start[0] > 0:
            self.list_start[0] -= 1

            # counting total amount of cards
            total = self.total_cards()

            # calculating chance to get low card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @Slot()
    def card_queen(self):
        if self.list_start[0] > 0:
            self.list_start[0] -= 1

            # counting total amount of cards
            total = self.total_cards()

            # calculating chance to get low card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @Slot()
    def card_king(self):
        if self.list_start[0] > 0:
            self.list_start[0] -= 1

            # counting total amount of cards
            total = self.total_cards()

            # calculating chance to get low card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")

    @Slot()
    def card_ace(self):
        if self.list_start[0] > 0:
            self.list_start[0] -= 1

            # counting total amount of cards
            total = self.total_cards()

            # calculating chance to get low card
            chance_2 = self.list_start[0] / total
            chance_3 = self.list_start[1] / total
            chance_4 = self.list_start[2] / total

            # updates stock and chance
            self.ui.text_2.clear()
            self.ui.text_2.append(f"Aantal lage:{self.list_start[0]}")
            self.ui.text_2.append(f"Kans op laag{chance_2}")

            self.ui.text_3.clear()
            self.ui.text_3.append(f"Aantal middelste{self.list_start[1]}")
            self.ui.text_3.append(f"Kans op middelste{chance_3}")

            self.ui.text_4.clear()
            self.ui.text_4.append(f"Aantal hoge{self.list_start[2]}")
            self.ui.text_4.append(f"Kans op hoog{chance_4}")


def main():
    """Main function to start the inteface and show it."""
    app = QtWidgets.QApplication(sys.argv)
    ui = kansberekening()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
