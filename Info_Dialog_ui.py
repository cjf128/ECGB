# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Info_Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Info_Dialog(object):
    def setupUi(self, Info_Dialog):
        if not Info_Dialog.objectName():
            Info_Dialog.setObjectName(u"Info_Dialog")
        Info_Dialog.resize(400, 212)
        self.verticalLayout = QVBoxLayout(Info_Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stopBitsLabel = QLabel(Info_Dialog)
        self.stopBitsLabel.setObjectName(u"stopBitsLabel")
        self.stopBitsLabel.setMinimumSize(QSize(100, 0))
        self.stopBitsLabel.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.stopBitsLabel.setFont(font)
        self.stopBitsLabel.setLayoutDirection(Qt.LeftToRight)
        self.stopBitsLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.stopBitsLabel)

        self.lineEdit = QLineEdit(Info_Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stopBitsLabel_3 = QLabel(Info_Dialog)
        self.stopBitsLabel_3.setObjectName(u"stopBitsLabel_3")
        self.stopBitsLabel_3.setMinimumSize(QSize(100, 0))
        self.stopBitsLabel_3.setMaximumSize(QSize(200, 16777215))
        self.stopBitsLabel_3.setFont(font)
        self.stopBitsLabel_3.setLayoutDirection(Qt.LeftToRight)
        self.stopBitsLabel_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.stopBitsLabel_3)

        self.id_lineEdit = QLineEdit(Info_Dialog)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        self.id_lineEdit.setFont(font1)
        self.id_lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.id_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.uartNumLabel = QLabel(Info_Dialog)
        self.uartNumLabel.setObjectName(u"uartNumLabel")
        self.uartNumLabel.setMaximumSize(QSize(100, 16777215))
        self.uartNumLabel.setFont(font)
        self.uartNumLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.uartNumLabel)

        self.comboBox = QComboBox(Info_Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font1)

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dataBitsLabel = QLabel(Info_Dialog)
        self.dataBitsLabel.setObjectName(u"dataBitsLabel")
        self.dataBitsLabel.setMaximumSize(QSize(100, 16777215))
        self.dataBitsLabel.setFont(font)
        self.dataBitsLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.dataBitsLabel)

        self.comboBox_2 = QComboBox(Info_Dialog)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.comboBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.QD_btn = QPushButton(Info_Dialog)
        self.QD_btn.setObjectName(u"QD_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QD_btn.sizePolicy().hasHeightForWidth())
        self.QD_btn.setSizePolicy(sizePolicy)
        self.QD_btn.setFont(font1)

        self.horizontalLayout_2.addWidget(self.QD_btn)

        self.Cancel_btn = QPushButton(Info_Dialog)
        self.Cancel_btn.setObjectName(u"Cancel_btn")
        sizePolicy.setHeightForWidth(self.Cancel_btn.sizePolicy().hasHeightForWidth())
        self.Cancel_btn.setSizePolicy(sizePolicy)
        self.Cancel_btn.setFont(font1)

        self.horizontalLayout_2.addWidget(self.Cancel_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Info_Dialog)

        QMetaObject.connectSlotsByName(Info_Dialog)
    # setupUi

    def retranslateUi(self, Info_Dialog):
        Info_Dialog.setWindowTitle(QCoreApplication.translate("Info_Dialog", u"Dialog", None))
        self.stopBitsLabel.setText(QCoreApplication.translate("Info_Dialog", u"\u59d3\u540d:", None))
        self.stopBitsLabel_3.setText(QCoreApplication.translate("Info_Dialog", u"\u5e8a\u53f7:", None))
        self.id_lineEdit.setText(QCoreApplication.translate("Info_Dialog", u"0001", None))
        self.uartNumLabel.setText(QCoreApplication.translate("Info_Dialog", u"\u6027\u522b:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Info_Dialog", u"\u7537", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Info_Dialog", u"\u5973", None))

        self.dataBitsLabel.setText(QCoreApplication.translate("Info_Dialog", u"\u6a21\u5f0f:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Info_Dialog", u"\u6210\u4eba", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Info_Dialog", u"\u65b0\u751f\u513f\uff080-1\u6708\uff09", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Info_Dialog", u"\u5a74\u513f\uff081\u6708-1\u5c81\uff09", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Info_Dialog", u"\u5e7c\u513f\uff081-3\u5c81\uff09", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("Info_Dialog", u"\u5b66\u9f84\u524d\u513f\u7ae5\uff083-6\u5c81\uff09", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("Info_Dialog", u"\u5b66\u9f84\u513f\u7ae5\uff086-12\u5c81\uff09", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("Info_Dialog", u"\u9752\u5c11\u5e74\uff0812-18\u5c81\uff09", None))

        self.QD_btn.setText(QCoreApplication.translate("Info_Dialog", u"\u786e\u8ba4", None))
        self.Cancel_btn.setText(QCoreApplication.translate("Info_Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

