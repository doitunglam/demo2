# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'form.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
                               QTextEdit, QToolButton, QWidget, QLabel)

# import file system
import os

# import time to caclculate the timing interval
import time

# telex keyboard
import bogo

# text to speech library
from gtts import gTTS
from playsound import playsound

# speech to text library
import speech_recognition as sr
import pyaudio
r = sr.Recognizer()

WAIT_TIME = 1
KEYMAP = [
    [u'a', u'ă', u'â', u'b', u'c'],
    [u'd', u'đ', u'e', u'ê', u'f'],
    [u'g', u'h', u'i'],
    [u'j', u'k', u'l'],
    [u'm', u'n', u'o', u'ô', u'ơ'],
    [u'p', u'q', u'r', u's'],
    [u't', u'u', u'ư', u'v'],
    [u'w', u'x', u'y', u'z'],
    [u'!', u'@', u'#', u'$', u'%', u'^', u'&', u'*', u'(', u')'],
    [u'0', u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9']
]


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        self.prevWord = ''
        # false flag indicates that the string is proccessed by bogo or not
        self.currentWord = ['', False]
        self.prevTime = time.monotonic()
        self.prevKey = [-1, 0]
        Widget.resize(360, 500)
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
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(10)
        font.setBold(True)
        Widget.setFont(font)
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 190, 341, 301))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_del = QPushButton(self.gridLayoutWidget)
        self.button_del.setObjectName(u"button_del")
        self.button_del.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_del, 6, 1, 1, 1)

        self.button_xyz = QPushButton(self.gridLayoutWidget)
        self.button_xyz.setObjectName(u"button_xyz")
        self.button_xyz.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_xyz, 5, 1, 1, 1)

        self.button_tuv = QPushButton(self.gridLayoutWidget)
        self.button_tuv.setObjectName(u"button_tuv")
        self.button_tuv.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_tuv, 5, 0, 1, 1)

        self.button_abc = QPushButton(self.gridLayoutWidget)
        self.button_abc.setObjectName(u"button_abc")
        self.button_abc.setMinimumSize(QSize(0, 29))
        self.button_abc.setMaximumSize(QSize(16777214, 16777215))
        self.button_abc.setAutoDefault(False)

        self.gridLayout.addWidget(self.button_abc, 2, 0, 1, 1)

        self.button_def = QPushButton(self.gridLayoutWidget)
        self.button_def.setObjectName(u"button_def")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.button_def.sizePolicy().hasHeightForWidth())
        self.button_def.setSizePolicy(sizePolicy)
        self.button_def.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_def, 2, 1, 1, 1)

        self.button_symbol = QPushButton(self.gridLayoutWidget)
        self.button_symbol.setObjectName(u"button_symbol")
        self.button_symbol.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_symbol, 5, 2, 1, 1)

        self.button_mno = QPushButton(self.gridLayoutWidget)
        self.button_mno.setObjectName(u"button_mno")
        self.button_mno.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_mno, 4, 1, 1, 1)

        self.button_jkl = QPushButton(self.gridLayoutWidget)
        self.button_jkl.setObjectName(u"button_jkl")
        sizePolicy.setHeightForWidth(
            self.button_jkl.sizePolicy().hasHeightForWidth())
        self.button_jkl.setSizePolicy(sizePolicy)
        self.button_jkl.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_jkl, 4, 0, 1, 1)

        self.button_pqrs = QPushButton(self.gridLayoutWidget)
        self.button_pqrs.setObjectName(u"button_pqrs")
        self.button_pqrs.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_pqrs, 4, 2, 1, 1)

        self.button_ghi = QPushButton(self.gridLayoutWidget)
        self.button_ghi.setObjectName(u"button_ghi")
        sizePolicy.setHeightForWidth(
            self.button_ghi.sizePolicy().hasHeightForWidth())
        self.button_ghi.setSizePolicy(sizePolicy)
        self.button_ghi.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_ghi, 2, 2, 1, 1)

        self.button_number = QPushButton(self.gridLayoutWidget)
        self.button_number.setObjectName(u"button_number")
        sizePolicy.setHeightForWidth(
            self.button_number.sizePolicy().hasHeightForWidth())
        self.button_number.setSizePolicy(sizePolicy)
        self.button_number.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_number, 6, 0, 1, 1)

        self.button_space = QPushButton(self.gridLayoutWidget)
        self.button_space.setObjectName(u"button_space")
        self.button_space.setMinimumSize(QSize(0, 29))

        self.gridLayout.addWidget(self.button_space, 6, 2, 1, 1)

        self.button_mic = QToolButton(Widget)
        self.button_mic.setObjectName(u"button_mic")
        self.button_mic.setGeometry(QRect(10, 30, 30, 30))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.button_mic.sizePolicy().hasHeightForWidth())
        self.button_mic.setSizePolicy(sizePolicy1)
        self.button_mic.setMinimumSize(QSize(24, 24))
        self.button_mic.setStyleSheet(u"qicon = rgb(41, 112, 200)")
        icon = QIcon()
        icon.addFile(u"icons/icons8-microphone-24.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.button_mic.setIcon(icon)
        self.button_mic.setIconSize(QSize(24, 24))
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 10, 261, 76))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.button_speaker = QToolButton(Widget)
        self.button_speaker.setObjectName(u"button_speaker")
        self.button_speaker.setGeometry(QRect(320, 30, 30, 30))
        icon1 = QIcon()
        icon1.addFile(u"icons/icons8-audio-24.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.button_speaker.setIcon(icon1)
        self.button_speaker.setIconSize(QSize(24, 24))

        # button logics
        self.button_abc.clicked.connect(self.abc_clicked)
        self.button_def.clicked.connect(self.def_clicked)
        self.button_ghi.clicked.connect(self.ghi_clicked)
        self.button_jkl.clicked.connect(self.jkl_clicked)
        self.button_mno.clicked.connect(self.mno_clicked)
        self.button_pqrs.clicked.connect(self.pqrs_clicked)
        self.button_tuv.clicked.connect(self.tuv_clicked)
        self.button_xyz.clicked.connect(self.xyz_clicked)
        self.button_number.clicked.connect(self.num_clicked)
        self.button_symbol.clicked.connect(self.sym_clicked)
        self.button_space.clicked.connect(self.space_clicked)
        self.button_del.clicked.connect(self.del_clicked)
        self.button_speaker.clicked.connect(self.speaker_clicked)
        self.button_mic.clicked.connect(self.mic_clicked)
        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(
            QCoreApplication.translate("Widget", u"Widget", None))
        self.button_del.setText(
            QCoreApplication.translate("Widget", u"DEL", None))
        self.button_xyz.setText(
            QCoreApplication.translate("Widget", u"WXYZ", None))
        self.button_tuv.setText(
            QCoreApplication.translate("Widget", u"TUV", None))
        self.button_abc.setText(
            QCoreApplication.translate("Widget", u"ABC", None))
        self.button_def.setText(
            QCoreApplication.translate("Widget", u"DEF", None))
        self.button_symbol.setText(
            QCoreApplication.translate("Widget", u"@#?", None))
        self.button_mno.setText(
            QCoreApplication.translate("Widget", u"MNO", None))
        self.button_jkl.setText(
            QCoreApplication.translate("Widget", u"JKL", None))
        self.button_pqrs.setText(
            QCoreApplication.translate("Widget", u"PQRS", None))
        self.button_ghi.setText(
            QCoreApplication.translate("Widget", u"GHI", None))
        self.button_number.setText(
            QCoreApplication.translate("Widget", u"123", None))
        self.button_space.setText(
            QCoreApplication.translate("Widget", u"__________", None))
        self.button_mic.setText("")
        self.button_speaker.setText("")
    # retranslateUi

    def input_clicked(self, key):
        currTime = time.monotonic()
        inputInterval = currTime - self.prevTime
        prevKeyValue = self.prevKey[0]
        prevKeyCount = self.prevKey[1]
        # self.textEdit.append(str(currTime - self.prevTime))

        SUB_KEYMAP = KEYMAP[key]
        print(key)
        print(prevKeyValue)
        if (prevKeyValue != key):
            self.currentWord[0] += SUB_KEYMAP[0]
            self.prevKey = [key, 0]
        else:
            if (inputInterval < WAIT_TIME):
                prevKeyCount = (prevKeyCount + 1) % SUB_KEYMAP.__len__()
                self.currentWord[0] = self.currentWord[0][:-1]
                self.currentWord[0] += SUB_KEYMAP[prevKeyCount]
                self.prevKey = [key, prevKeyCount]
            else:
                self.currentWord[0] += SUB_KEYMAP[0]
                self.prevKey = [key, 0]
        self.prevTime = currTime
        presentCurrentWord = bogo.process_sequence(self.currentWord[0])
        self.textEdit.setText(self.prevWord + presentCurrentWord+'|')

    def abc_clicked(self):
        self.input_clicked(0)

    def def_clicked(self):
        self.input_clicked(1)

    def ghi_clicked(self):
        self.input_clicked(2)

    def jkl_clicked(self):
        self.input_clicked(3)

    def mno_clicked(self):
        self.input_clicked(4)

    def pqrs_clicked(self):
        self.input_clicked(5)

    def tuv_clicked(self):
        self.input_clicked(6)

    def xyz_clicked(self):
        self.input_clicked(7)

    def sym_clicked(self):
        self.input_clicked(8)

    def num_clicked(self):
        self.input_clicked(9)

    def space_clicked(self):
        if(not self.currentWord[1]):
            self.currentWord[0] = bogo.process_sequence(self.currentWord[0])
            self.currentWord[1] = True
        self.prevWord = self.prevWord + self.currentWord[0] + ' '
        self.currentWord[0] = ''
        self.currentWord[1] = False
        self.prevTime = time.monotonic()
        self.prevKey = [-1, 0]

    def del_clicked(self):
        self.prevTime = time.monotonic()
        self.prevKey = [-1, 0]
        if(not self.currentWord[1]):
            self.currentWord[0] = bogo.process_sequence(self.currentWord[0])
            self.currentWord[1] = True
        if (self.currentWord[0]):
            self.currentWord[0] = self.currentWord[0][:-1]
        else:
            if (self.prevWord):
                self.prevWord = self.prevWord[:-1]
        self.textEdit.setText(self.prevWord + self.currentWord[0] + '|')

    def speaker_clicked(self):
        if(not self.currentWord[1]):
            self.currentWord[0] = bogo.process_sequence(self.currentWord[0])
            self.currentWord[1] = True
        text = self.prevWord + self.currentWord[0]
        output = gTTS(text, lang="vi", slow=False)

        output.save("output.mp3")
        playsound("output.mp3")
        os.remove("output.mp3")

    def mic_clicked(self):
        if(not self.currentWord[1]):
            self.currentWord[0] = bogo.process_sequence(self.currentWord[0])
            self.currentWord[1] = True
        with sr.Microphone() as source:
            audio = r.listen(source, 2, 10)
            try:
                text = r.recognize_google(audio, language="vi-VI")
                self.prevWord = self.prevWord + self.currentWord[0]
                self.currentWord[0] = text
                self.currentWord[1] = True
                self.textEdit.setText(
                    self.prevWord + self.currentWord[0] + '|')
            except:
                print("Xin lỗi! tôi không nhận được voice!")
