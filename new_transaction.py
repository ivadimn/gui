# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res-new-window-rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(330, 395)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_new_transaction = QLabel(self.frame)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        self.lbl_new_transaction.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_new_transaction)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox { \n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item { \n"
"color: black;\n"
"} ")

        self.verticalLayout.addWidget(self.comboBox)

        self.data = QDateEdit(self.frame)
        self.data.setObjectName(u"data")
        self.data.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.data.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.data.setDate(QDate(2023, 1, 1))

        self.verticalLayout.addWidget(self.data)

        self.le_description = QLineEdit(self.frame)
        self.le_description.setObjectName(u"le_description")
        self.le_description.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_description)

        self.le_balance = QLineEdit(self.frame)
        self.le_balance.setObjectName(u"le_balance")
        self.le_balance.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.le_balance)

        self.comboBox_2 = QComboBox(self.frame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QComboBox { \n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item { \n"
"color: black;\n"
"} ")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.btn_new_transaction = QPushButton(self.frame)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setStyleSheet(u"QPushButton { \n"
"background-color:rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px; \n"
"color: white;\n"
"} \n"
"QPushButton:hover {\n"
"background-color:rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:rgba(255, 255, 255, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_new_transaction)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("Dialog", u"New transaction", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Groceries", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Entertainment", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Auto", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Work", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.le_description.setPlaceholderText(QCoreApplication.translate("Dialog", u"Description", None))
        self.le_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Dialog", u"Outcome", None))

        self.btn_new_transaction.setText(QCoreApplication.translate("Dialog", u"Save new transaction", None))
    # retranslateUi

