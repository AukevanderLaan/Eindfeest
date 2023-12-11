# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kaartteller.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(708, 493)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 10, 551, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.low_card_button = QPushButton(self.verticalLayoutWidget)
        self.low_card_button.setObjectName(u"low_card_button")

        self.horizontalLayout_2.addWidget(self.low_card_button)

        self.neutral_card_button = QPushButton(self.verticalLayoutWidget)
        self.neutral_card_button.setObjectName(u"neutral_card_button")

        self.horizontalLayout_2.addWidget(self.neutral_card_button)

        self.high_card_button = QPushButton(self.verticalLayoutWidget)
        self.high_card_button.setObjectName(u"high_card_button")

        self.horizontalLayout_2.addWidget(self.high_card_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_low = QTextEdit(self.verticalLayoutWidget)
        self.text_low.setObjectName(u"text_low")

        self.horizontalLayout.addWidget(self.text_low)

        self.text_neutral = QTextEdit(self.verticalLayoutWidget)
        self.text_neutral.setObjectName(u"text_neutral")

        self.horizontalLayout.addWidget(self.text_neutral)

        self.text_high = QTextEdit(self.verticalLayoutWidget)
        self.text_high.setObjectName(u"text_high")

        self.horizontalLayout.addWidget(self.text_high)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 708, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.low_card_button.setText(QCoreApplication.translate("MainWindow", u"Low card (2-6)", None))
        self.neutral_card_button.setText(QCoreApplication.translate("MainWindow", u"Neutral card (7-9)", None))
        self.high_card_button.setText(QCoreApplication.translate("MainWindow", u"High card (10-ace)", None))
    # retranslateUi

