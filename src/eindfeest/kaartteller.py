# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kaartteller.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 493)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 10, 551, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.low_card_button = QPushButton(self.verticalLayoutWidget)
        self.low_card_button.setObjectName("low_card_button")

        self.horizontalLayout_2.addWidget(self.low_card_button)

        self.neutral_card_button = QPushButton(self.verticalLayoutWidget)
        self.neutral_card_button.setObjectName("neutral_card_button")

        self.horizontalLayout_2.addWidget(self.neutral_card_button)

        self.high_card_button = QPushButton(self.verticalLayoutWidget)
        self.high_card_button.setObjectName("high_card_button")

        self.horizontalLayout_2.addWidget(self.high_card_button)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")

        self.horizontalLayout.addWidget(self.textEdit)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 708, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.low_card_button.setText(
            QCoreApplication.translate("MainWindow", "Low card (2-6)", None)
        )
        self.neutral_card_button.setText(
            QCoreApplication.translate("MainWindow", "Neutral card (7-9)", None)
        )
        self.high_card_button.setText(
            QCoreApplication.translate("MainWindow", "High card (10-ace)", None)
        )

    # retranslateUi
