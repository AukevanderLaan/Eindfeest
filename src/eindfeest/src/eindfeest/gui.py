import csv
import sys

import pyqtgraph as pg

# PyQtGraph global options
pg.setConfigOption("background", "w")
pg.setConfigOption("foreground", "k")

import numpy as np
from PySide6 import QtWidgets
from PySide6.QtCore import Slot


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        """init function to create a window"""
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
