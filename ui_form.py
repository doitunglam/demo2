# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QTextEdit, QToolButton, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(360, 372)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(10)
        font.setBold(True)
        Widget.setFont(font)
        Widget.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(0, 255, 255);\n"
"	font: 9pt \"Segoe Print\";\n"
"	border-radius: 10px;\n"
"}\n"
"QToolButton {\n"
"	background-color: rgb(170, 255, 255);\n"
"	f\n"
"	border-radius: 10px;\n"
"}")
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 150, 341, 211))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_pqrs = QPushButton(self.gridLayoutWidget)
        self.button_pqrs.setObjectName(u"button_pqrs")
        self.button_pqrs.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_pqrs, 4, 2, 1, 1)

        self.button_jkl = QPushButton(self.gridLayoutWidget)
        self.button_jkl.setObjectName(u"button_jkl")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_jkl.sizePolicy().hasHeightForWidth())
        self.button_jkl.setSizePolicy(sizePolicy)
        self.button_jkl.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_jkl, 4, 0, 1, 1)

        self.button_def = QPushButton(self.gridLayoutWidget)
        self.button_def.setObjectName(u"button_def")
        sizePolicy.setHeightForWidth(self.button_def.sizePolicy().hasHeightForWidth())
        self.button_def.setSizePolicy(sizePolicy)
        self.button_def.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_def, 2, 1, 1, 1)

        self.button_del = QPushButton(self.gridLayoutWidget)
        self.button_del.setObjectName(u"button_del")
        self.button_del.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_del, 6, 1, 1, 1)

        self.button_abc = QPushButton(self.gridLayoutWidget)
        self.button_abc.setObjectName(u"button_abc")
        self.button_abc.setMinimumSize(QSize(0, 29))
        self.button_abc.setMaximumSize(QSize(16777214, 16777215))
        self.button_abc.setAutoDefault(False)

        self.gridLayout.addWidget(self.button_abc, 2, 0, 1, 1)

        self.button_tuv = QPushButton(self.gridLayoutWidget)
        self.button_tuv.setObjectName(u"button_tuv")
        self.button_tuv.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_tuv, 5, 0, 1, 1)

        self.button_number = QPushButton(self.gridLayoutWidget)
        self.button_number.setObjectName(u"button_number")
        sizePolicy.setHeightForWidth(self.button_number.sizePolicy().hasHeightForWidth())
        self.button_number.setSizePolicy(sizePolicy)
        self.button_number.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_number, 6, 0, 1, 1)

        self.button_ghi = QPushButton(self.gridLayoutWidget)
        self.button_ghi.setObjectName(u"button_ghi")
        sizePolicy.setHeightForWidth(self.button_ghi.sizePolicy().hasHeightForWidth())
        self.button_ghi.setSizePolicy(sizePolicy)
        self.button_ghi.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_ghi, 2, 2, 1, 1)

        self.button_symbol = QPushButton(self.gridLayoutWidget)
        self.button_symbol.setObjectName(u"button_symbol")
        self.button_symbol.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_symbol, 5, 2, 1, 1)

        self.button_xyz = QPushButton(self.gridLayoutWidget)
        self.button_xyz.setObjectName(u"button_xyz")
        self.button_xyz.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_xyz, 5, 1, 1, 1)

        self.button_space = QPushButton(self.gridLayoutWidget)
        self.button_space.setObjectName(u"button_space")
        self.button_space.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_space, 6, 2, 1, 1)

        self.button_mno = QPushButton(self.gridLayoutWidget)
        self.button_mno.setObjectName(u"button_mno")
        self.button_mno.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_mno, 4, 1, 1, 1)

        self.button_mic = QToolButton(Widget)
        self.button_mic.setObjectName(u"button_mic")
        self.button_mic.setGeometry(QRect(10, 30, 30, 30))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_mic.sizePolicy().hasHeightForWidth())
        self.button_mic.setSizePolicy(sizePolicy1)
        self.button_mic.setMinimumSize(QSize(24, 24))
        self.button_mic.setStyleSheet(u"qicon = rgb(41, 112, 200)")
        icon = QIcon()
        icon.addFile(u"icons/icons8-microphone-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_mic.setIcon(icon)
        self.button_mic.setIconSize(QSize(24, 24))
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 10, 261, 76))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.button_speaker = QToolButton(Widget)
        self.button_speaker.setObjectName(u"button_speaker")
        self.button_speaker.setGeometry(QRect(320, 30, 30, 30))
        icon1 = QIcon()
        icon1.addFile(u"icons/icons8-audio-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_speaker.setIcon(icon1)
        self.button_speaker.setIconSize(QSize(24, 24))
        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 90, 341, 29))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)
        self.pushButton_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalLayoutWidget_2 = QWidget(Widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 341, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy3.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy3)
        self.pushButton_5.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy3.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy3)
        self.pushButton_4.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(100)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        self.pushButton_3.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.button_pqrs.setText(QCoreApplication.translate("Widget", u"PQRS", None))
        self.button_jkl.setText(QCoreApplication.translate("Widget", u"JKL", None))
        self.button_def.setText(QCoreApplication.translate("Widget", u"DEF", None))
        self.button_del.setText(QCoreApplication.translate("Widget", u"DEL", None))
        self.button_abc.setText(QCoreApplication.translate("Widget", u"ABC", None))
        self.button_tuv.setText(QCoreApplication.translate("Widget", u"TUV", None))
        self.button_number.setText(QCoreApplication.translate("Widget", u"123", None))
        self.button_ghi.setText(QCoreApplication.translate("Widget", u"GHI", None))
        self.button_symbol.setText(QCoreApplication.translate("Widget", u"@#?", None))
        self.button_xyz.setText(QCoreApplication.translate("Widget", u"XYZ", None))
        self.button_space.setText(QCoreApplication.translate("Widget", u"__________", None))
        self.button_mno.setText(QCoreApplication.translate("Widget", u"MNO", None))
        self.button_mic.setText("")
        self.button_speaker.setText("")
        self.pushButton.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"PushButton", None))
    # retranslateUi

