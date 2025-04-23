# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BJ_Dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_BJ_Dialog(object):
    def setupUi(self, BJ_Dialog):
        if not BJ_Dialog.objectName():
            BJ_Dialog.setObjectName(u"BJ_Dialog")
        BJ_Dialog.resize(386, 327)
        self.verticalLayout = QVBoxLayout(BJ_Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(BJ_Dialog)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(200)
        self.spinBox.setSingleStep(0)
        self.spinBox.setValue(100)

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.spinBox_2 = QSpinBox(self.frame)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMaximum(200)
        self.spinBox_2.setValue(60)

        self.horizontalLayout_2.addWidget(self.spinBox_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame1 = QFrame(BJ_Dialog)
        self.frame1.setObjectName(u"frame1")
        self.horizontalLayout_3 = QHBoxLayout(self.frame1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_5 = QLabel(self.frame1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.spinBox_3 = QSpinBox(self.frame1)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setFont(font)
        self.spinBox_3.setSingleStep(1)
        self.spinBox_3.setValue(24)

        self.horizontalLayout_3.addWidget(self.spinBox_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_6 = QLabel(self.frame1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.spinBox_4 = QSpinBox(self.frame1)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setFont(font)
        self.spinBox_4.setValue(12)

        self.horizontalLayout_3.addWidget(self.spinBox_4)


        self.verticalLayout.addWidget(self.frame1)

        self.frame_2 = QFrame(BJ_Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.spinBox_5 = QSpinBox(self.frame_2)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setFont(font)
        self.spinBox_5.setValue(94)

        self.horizontalLayout_4.addWidget(self.spinBox_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame2 = QFrame(BJ_Dialog)
        self.frame2.setObjectName(u"frame2")
        self.horizontalLayout = QHBoxLayout(self.frame2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame2)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(12)
        self.pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame2)


        self.retranslateUi(BJ_Dialog)

        QMetaObject.connectSlotsByName(BJ_Dialog)
    # setupUi

    def retranslateUi(self, BJ_Dialog):
        BJ_Dialog.setWindowTitle(QCoreApplication.translate("BJ_Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("BJ_Dialog", u"\u5fc3\u7387:", None))
        self.label_2.setText(QCoreApplication.translate("BJ_Dialog", u"\u4e0a\u9608\u503c\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("BJ_Dialog", u"\u4e0b\u9608\u503c\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("BJ_Dialog", u"\u547c\u5438\u7387:", None))
        self.label_5.setText(QCoreApplication.translate("BJ_Dialog", u"\u4e0a\u9608\u503c\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("BJ_Dialog", u"\u4e0b\u9608\u503c\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("BJ_Dialog", u"\u8840\u6c27\u9971\u548c\u5ea6:", None))
        self.label_9.setText(QCoreApplication.translate("BJ_Dialog", u"\u4e0b\u9608\u503c\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("BJ_Dialog", u"\u8bbe\u7f6e", None))
        self.pushButton_2.setText(QCoreApplication.translate("BJ_Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

