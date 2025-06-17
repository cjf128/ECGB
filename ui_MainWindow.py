# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ECGB_Window(object):
    def setupUi(self, ECGB_Window):
        if not ECGB_Window.objectName():
            ECGB_Window.setObjectName(u"ECGB_Window")
        ECGB_Window.resize(1281, 849)
        self.centralwidget = QWidget(ECGB_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setStyleSheet(u"background-color: rgb(102, 101, 101);")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.id_label = QLabel(self.widget)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setFont(font1)
        self.id_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.id_label)

        self.horizontalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_13)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.name_label = QLabel(self.widget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setFont(font1)
        self.name_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.name_label)

        self.horizontalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.mode_label = QLabel(self.widget)
        self.mode_label.setObjectName(u"mode_label")
        self.mode_label.setFont(font1)
        self.mode_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.mode_label)

        self.horizontalSpacer_15 = QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.sex_label = QLabel(self.widget)
        self.sex_label.setObjectName(u"sex_label")
        self.sex_label.setFont(font1)
        self.sex_label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.sex_label)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.line_6 = QFrame(self.widget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_6)

        self.state_hr_label = QLabel(self.widget)
        self.state_hr_label.setObjectName(u"state_hr_label")
        self.state_hr_label.setMinimumSize(QSize(100, 0))
        self.state_hr_label.setFont(font)
        self.state_hr_label.setStyleSheet(u"color: rgb(0, 255, 0);")
        self.state_hr_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.state_hr_label)

        self.line_8 = QFrame(self.widget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_8)

        self.status_label = QLabel(self.widget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font1)
        self.status_label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_4.addWidget(self.status_label)

        self.horizontalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.date_label = QLabel(self.widget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setFont(font1)
        self.date_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.date_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.date_label)

        self.time_label = QLabel(self.widget)
        self.time_label.setObjectName(u"time_label")
        font2 = QFont()
        font2.setPointSize(11)
        self.time_label.setFont(font2)
        self.time_label.setLayoutDirection(Qt.LeftToRight)
        self.time_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.time_label)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget1 = QWidget(self.frame_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.widget1)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(40, 0))
        self.frame.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        self.label_11.setMinimumSize(QSize(0, 0))
        self.label_11.setMaximumSize(QSize(40, 28))
        font3 = QFont()
        font3.setFamily(u"Agency FB")
        font3.setPointSize(18)
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: rgb(37, 232, 30);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy2)
        self.label_12.setMaximumSize(QSize(32, 150))
        self.label_12.setFont(font1)
        self.label_12.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_12.setFrameShape(QFrame.NoFrame)
        self.label_12.setFrameShadow(QFrame.Plain)
        self.label_12.setLineWidth(0)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_12)


        self.horizontalLayout_6.addWidget(self.frame)

        self.frame1 = QFrame(self.widget1)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMinimumSize(QSize(720, 0))
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame1)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.ECG_wave = QLabel(self.frame1)
        self.ECG_wave.setObjectName(u"ECG_wave")
        self.ECG_wave.setMinimumSize(QSize(800, 200))

        self.verticalLayout_12.addWidget(self.ECG_wave)


        self.horizontalLayout_6.addWidget(self.frame1)


        self.horizontalLayout.addWidget(self.widget1)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(280, 16777215))
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, -1, 2)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_17 = QLabel(self.widget_2)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(48, 0))
        self.label_17.setMaximumSize(QSize(48, 28))
        font4 = QFont()
        font4.setFamily(u"Agency FB")
        font4.setPointSize(14)
        self.label_17.setFont(font4)
        self.label_17.setStyleSheet(u"background-color: rgb(37, 232, 30);\n"
"border-radius: 5px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_17)

        self.label_18 = QLabel(self.widget_2)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setMaximumSize(QSize(38, 28))
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"color: rgb(37, 232, 30);")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_18)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.DL1_label = QLabel(self.widget_2)
        self.DL1_label.setObjectName(u"DL1_label")
        sizePolicy1.setHeightForWidth(self.DL1_label.sizePolicy().hasHeightForWidth())
        self.DL1_label.setSizePolicy(sizePolicy1)
        self.DL1_label.setMinimumSize(QSize(0, 0))
        self.DL1_label.setMaximumSize(QSize(38, 28))
        self.DL1_label.setFont(font4)
        self.DL1_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.DL1_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.DL1_label)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.HR_label = QLabel(self.widget_2)
        self.HR_label.setObjectName(u"HR_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.HR_label.sizePolicy().hasHeightForWidth())
        self.HR_label.setSizePolicy(sizePolicy3)
        self.HR_label.setMinimumSize(QSize(0, 0))
        self.HR_label.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamily(u"Agency FB")
        font5.setPointSize(120)
        self.HR_label.setFont(font5)
        self.HR_label.setStyleSheet(u"color: rgb(37, 232, 30);")
        self.HR_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.HR_label)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.line_4 = QFrame(self.frame_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setLineWidth(1)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.frame2 = QFrame(self.widget_4)
        self.frame2.setObjectName(u"frame2")
        sizePolicy.setHeightForWidth(self.frame2.sizePolicy().hasHeightForWidth())
        self.frame2.setSizePolicy(sizePolicy)
        self.frame2.setMinimumSize(QSize(40, 0))
        self.verticalLayout_5 = QVBoxLayout(self.frame2)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.label_13 = QLabel(self.frame2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(0, 0))
        self.label_13.setMaximumSize(QSize(38, 28))
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(255, 195, 0);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMaximumSize(QSize(32, 150))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_14)


        self.horizontalLayout_7.addWidget(self.frame2)

        self.frame_3 = QFrame(self.widget_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(720, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.RESP_wave = QLabel(self.frame_3)
        self.RESP_wave.setObjectName(u"RESP_wave")
        self.RESP_wave.setMinimumSize(QSize(800, 200))

        self.verticalLayout_11.addWidget(self.RESP_wave)


        self.horizontalLayout_7.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(280, 16777215))
        self.widget_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_22 = QLabel(self.widget_3)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QSize(48, 0))
        self.label_22.setMaximumSize(QSize(48, 28))
        self.label_22.setFont(font4)
        self.label_22.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(255, 195, 0);")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_22)

        self.label_23 = QLabel(self.widget_3)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)
        self.label_23.setMinimumSize(QSize(0, 0))
        self.label_23.setMaximumSize(QSize(38, 28))
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"color: rgb(255, 195, 0);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_23)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.DL2_label = QLabel(self.widget_3)
        self.DL2_label.setObjectName(u"DL2_label")
        sizePolicy1.setHeightForWidth(self.DL2_label.sizePolicy().hasHeightForWidth())
        self.DL2_label.setSizePolicy(sizePolicy1)
        self.DL2_label.setMinimumSize(QSize(0, 0))
        self.DL2_label.setMaximumSize(QSize(38, 28))
        self.DL2_label.setFont(font4)
        self.DL2_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.DL2_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.DL2_label)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.RESP_label = QLabel(self.widget_3)
        self.RESP_label.setObjectName(u"RESP_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.RESP_label.sizePolicy().hasHeightForWidth())
        self.RESP_label.setSizePolicy(sizePolicy4)
        self.RESP_label.setMinimumSize(QSize(0, 0))
        self.RESP_label.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamily(u"Agency FB")
        font6.setPointSize(100)
        self.RESP_label.setFont(font6)
        self.RESP_label.setStyleSheet(u"color: rgb(255, 195, 0);")
        self.RESP_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.RESP_label)


        self.horizontalLayout_2.addWidget(self.widget_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_5 = QFrame(self.frame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_6 = QWidget(self.frame_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.widget_6)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(40, 0))
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setMinimumSize(QSize(0, 0))
        self.label_15.setMaximumSize(QSize(40, 28))
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(51, 232, 220);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        sizePolicy2.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy2)
        self.label_16.setMaximumSize(QSize(32, 150))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.label_16)


        self.horizontalLayout_8.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.widget_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(720, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.SPO2_wave = QLabel(self.frame_4)
        self.SPO2_wave.setObjectName(u"SPO2_wave")
        self.SPO2_wave.setMinimumSize(QSize(800, 200))

        self.verticalLayout_10.addWidget(self.SPO2_wave)


        self.horizontalLayout_8.addWidget(self.frame_4)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.widget_5 = QWidget(self.frame_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(280, 16777215))
        self.widget_5.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_9 = QVBoxLayout(self.widget_5)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_26 = QLabel(self.widget_5)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QSize(48, 0))
        self.label_26.setMaximumSize(QSize(48, 28))
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(51, 232, 220);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_26)

        self.label2 = QLabel(self.widget_5)
        self.label2.setObjectName(u"label2")
        sizePolicy1.setHeightForWidth(self.label2.sizePolicy().hasHeightForWidth())
        self.label2.setSizePolicy(sizePolicy1)
        self.label2.setMinimumSize(QSize(0, 0))
        self.label2.setMaximumSize(QSize(38, 28))
        self.label2.setFont(font3)
        self.label2.setStyleSheet(u"color: rgb(51, 232, 220);")
        self.label2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.SpO2_label = QLabel(self.widget_5)
        self.SpO2_label.setObjectName(u"SpO2_label")
        sizePolicy4.setHeightForWidth(self.SpO2_label.sizePolicy().hasHeightForWidth())
        self.SpO2_label.setSizePolicy(sizePolicy4)
        self.SpO2_label.setMinimumSize(QSize(0, 0))
        self.SpO2_label.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamily(u"Agency FB")
        font7.setPointSize(72)
        self.SpO2_label.setFont(font7)
        self.SpO2_label.setStyleSheet(u"color: rgb(51, 232, 220);")
        self.SpO2_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.SpO2_label)

        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font7)
        self.label.setStyleSheet(u"color: rgb(49, 223, 211);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label)

        self.PR_label = QLabel(self.widget_5)
        self.PR_label.setObjectName(u"PR_label")
        sizePolicy4.setHeightForWidth(self.PR_label.sizePolicy().hasHeightForWidth())
        self.PR_label.setSizePolicy(sizePolicy4)
        self.PR_label.setMinimumSize(QSize(0, 0))
        self.PR_label.setMaximumSize(QSize(16777215, 16777215))
        self.PR_label.setFont(font7)
        self.PR_label.setStyleSheet(u"color: rgb(51, 232, 220);")
        self.PR_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.PR_label)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_10 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.DL3_label = QLabel(self.widget_5)
        self.DL3_label.setObjectName(u"DL3_label")
        sizePolicy1.setHeightForWidth(self.DL3_label.sizePolicy().hasHeightForWidth())
        self.DL3_label.setSizePolicy(sizePolicy1)
        self.DL3_label.setMinimumSize(QSize(0, 0))
        self.DL3_label.setMaximumSize(QSize(16777215, 28))
        self.DL3_label.setFont(font4)
        self.DL3_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.DL3_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.DL3_label)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)

        self.DL4_label = QLabel(self.widget_5)
        self.DL4_label.setObjectName(u"DL4_label")
        sizePolicy1.setHeightForWidth(self.DL4_label.sizePolicy().hasHeightForWidth())
        self.DL4_label.setSizePolicy(sizePolicy1)
        self.DL4_label.setMinimumSize(QSize(0, 0))
        self.DL4_label.setMaximumSize(QSize(16777215, 28))
        self.DL4_label.setFont(font4)
        self.DL4_label.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.DL4_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.DL4_label)

        self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_3.addWidget(self.widget_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.widget_31 = QWidget(self.centralwidget)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setMaximumSize(QSize(16777215, 60))
        self.widget_31.setStyleSheet(u"background-color: rgb(102, 101, 101);")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.XX_btn = QPushButton(self.widget_31)
        self.XX_btn.setObjectName(u"XX_btn")
        sizePolicy4.setHeightForWidth(self.XX_btn.sizePolicy().hasHeightForWidth())
        self.XX_btn.setSizePolicy(sizePolicy4)
        font8 = QFont()
        font8.setFamily(u"Agency FB")
        font8.setPointSize(20)
        self.XX_btn.setFont(font8)
        self.XX_btn.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius: 8px;")

        self.horizontalLayout_5.addWidget(self.XX_btn)

        self.CK_btn = QPushButton(self.widget_31)
        self.CK_btn.setObjectName(u"CK_btn")
        sizePolicy4.setHeightForWidth(self.CK_btn.sizePolicy().hasHeightForWidth())
        self.CK_btn.setSizePolicy(sizePolicy4)
        self.CK_btn.setMinimumSize(QSize(0, 0))
        self.CK_btn.setFont(font8)
        self.CK_btn.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius: 8px;\n"
"")

        self.horizontalLayout_5.addWidget(self.CK_btn)

        self.load_btn = QPushButton(self.widget_31)
        self.load_btn.setObjectName(u"load_btn")
        sizePolicy4.setHeightForWidth(self.load_btn.sizePolicy().hasHeightForWidth())
        self.load_btn.setSizePolicy(sizePolicy4)
        self.load_btn.setMinimumSize(QSize(0, 0))
        self.load_btn.setFont(font8)
        self.load_btn.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius: 8px;\n"
"")

        self.horizontalLayout_5.addWidget(self.load_btn)

        self.SJ_btn = QPushButton(self.widget_31)
        self.SJ_btn.setObjectName(u"SJ_btn")
        sizePolicy4.setHeightForWidth(self.SJ_btn.sizePolicy().hasHeightForWidth())
        self.SJ_btn.setSizePolicy(sizePolicy4)
        self.SJ_btn.setFont(font8)
        self.SJ_btn.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius: 8px;")

        self.horizontalLayout_5.addWidget(self.SJ_btn)

        self.BJ_btn = QPushButton(self.widget_31)
        self.BJ_btn.setObjectName(u"BJ_btn")
        sizePolicy4.setHeightForWidth(self.BJ_btn.sizePolicy().hasHeightForWidth())
        self.BJ_btn.setSizePolicy(sizePolicy4)
        self.BJ_btn.setFont(font8)
        self.BJ_btn.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius: 8px;")

        self.horizontalLayout_5.addWidget(self.BJ_btn)

        self.JC_btn = QPushButton(self.widget_31)
        self.JC_btn.setObjectName(u"JC_btn")
        sizePolicy4.setHeightForWidth(self.JC_btn.sizePolicy().hasHeightForWidth())
        self.JC_btn.setSizePolicy(sizePolicy4)
        self.JC_btn.setFont(font8)
        self.JC_btn.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"border-radius: 8px;")

        self.horizontalLayout_5.addWidget(self.JC_btn)


        self.verticalLayout.addWidget(self.widget_31)

        ECGB_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(ECGB_Window)

        QMetaObject.connectSlotsByName(ECGB_Window)
    # setupUi

    def retranslateUi(self, ECGB_Window):
        ECGB_Window.setWindowTitle(QCoreApplication.translate("ECGB_Window", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("ECGB_Window", u"\u5e8a\u53f7:", None))
        self.id_label.setText(QCoreApplication.translate("ECGB_Window", u"0001", None))
        self.label_7.setText(QCoreApplication.translate("ECGB_Window", u"\u59d3\u540d:", None))
        self.name_label.setText(QCoreApplication.translate("ECGB_Window", u"None", None))
        self.label_2.setText(QCoreApplication.translate("ECGB_Window", u"\u6a21\u5f0f:", None))
        self.mode_label.setText(QCoreApplication.translate("ECGB_Window", u"None", None))
        self.label_3.setText(QCoreApplication.translate("ECGB_Window", u"\u6027\u522b:", None))
        self.sex_label.setText(QCoreApplication.translate("ECGB_Window", u"None", None))
        self.state_hr_label.setText(QCoreApplication.translate("ECGB_Window", u"\u6b63\u5e38", None))
        self.status_label.setText(QCoreApplication.translate("ECGB_Window", u"\u4e32\u53e3\u672a\u6253\u5f00", None))
        self.date_label.setText(QCoreApplication.translate("ECGB_Window", u"\u2014\u2014", None))
        self.time_label.setText(QCoreApplication.translate("ECGB_Window", u"\u2014\u2014", None))
        self.label_11.setText(QCoreApplication.translate("ECGB_Window", u"ECG", None))
        self.label_12.setText("")
        self.ECG_wave.setText("")
        self.label_17.setText(QCoreApplication.translate("ECGB_Window", u"\u5fc3\u7387", None))
        self.label_18.setText(QCoreApplication.translate("ECGB_Window", u"HR", None))
        self.DL1_label.setText(QCoreApplication.translate("ECGB_Window", u"\u5bfc\u8054", None))
        self.HR_label.setText("")
        self.label_13.setText(QCoreApplication.translate("ECGB_Window", u"RESP", None))
        self.label_14.setText("")
        self.RESP_wave.setText("")
        self.label_22.setText(QCoreApplication.translate("ECGB_Window", u"\u547c\u5438", None))
        self.label_23.setText(QCoreApplication.translate("ECGB_Window", u"RESP", None))
        self.DL2_label.setText(QCoreApplication.translate("ECGB_Window", u"\u5bfc\u8054", None))
        self.RESP_label.setText("")
        self.label_15.setText(QCoreApplication.translate("ECGB_Window", u"SpO2", None))
        self.label_16.setText("")
        self.SPO2_wave.setText("")
        self.label_26.setText(QCoreApplication.translate("ECGB_Window", u"\u8840\u6c27", None))
        self.label2.setText(QCoreApplication.translate("ECGB_Window", u"SpO2", None))
        self.SpO2_label.setText("")
        self.label.setText(QCoreApplication.translate("ECGB_Window", u"/", None))
        self.PR_label.setText("")
        self.DL3_label.setText(QCoreApplication.translate("ECGB_Window", u"\u63a2\u5934\u8131\u843d", None))
        self.DL4_label.setText(QCoreApplication.translate("ECGB_Window", u"\u624b\u6307\u8131\u843d", None))
        self.XX_btn.setText(QCoreApplication.translate("ECGB_Window", u"\u4fe1\u606f\u5f55\u5165", None))
        self.CK_btn.setText(QCoreApplication.translate("ECGB_Window", u"\u4e32\u53e3\u8bbe\u7f6e", None))
        self.load_btn.setText(QCoreApplication.translate("ECGB_Window", u"\u6570\u636e\u5bfc\u5165", None))
        self.SJ_btn.setText(QCoreApplication.translate("ECGB_Window", u"\u6570\u636e\u5b58\u50a8", None))
        self.BJ_btn.setText(QCoreApplication.translate("ECGB_Window", u"\u62a5\u8b66\u8bbe\u7f6e", None))
        self.JC_btn.setText(QCoreApplication.translate("ECGB_Window", u"\u89e3\u9664\u60a3\u8005", None))
    # retranslateUi

