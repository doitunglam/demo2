# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'form.ui'
##
# Created by: Qt User Interface Compiler version 6.4.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from TextGenerator import TextGenerator
import subprocess
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy, QHBoxLayout,
                               QTextEdit, QToolButton, QWidget, QLabel, QMessageBox)

import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton

from PySide6.QtMultimedia import (
    QMediaCaptureSession,
    QAudioInput,
    QMediaRecorder,
    QMediaFormat,
)

from PySide6.QtCore import QDir, QUrl

from pathlib import Path

import os

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

from Controller import bind
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

        self.suggestButton: list[QPushButton] = []

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
        sizePolicy3.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setMinimumSize(QSize(100, 0))

        self.suggestButton.append(self.pushButton)
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)
        self.pushButton_2.setMinimumSize(QSize(100, 0))

        self.suggestButton.append(self.pushButton_2)
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalLayoutWidget_2 = QWidget(Widget)
        self.horizontalLayoutWidget_2.setObjectName(
            u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 341, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy3.setHeightForWidth(
            self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy3)
        self.pushButton_5.setMinimumSize(QSize(100, 0))

        self.suggestButton.append(self.pushButton_5)
        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy3.setHeightForWidth(
            self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy3)
        self.pushButton_4.setMinimumSize(QSize(100, 0))

        self.suggestButton.append(self.pushButton_4)
        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(100)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        self.pushButton_3.setMinimumSize(QSize(100, 0))

        self.suggestButton.append(self.pushButton_3)
        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.suggestButton[0].clicked.connect(lambda: self.suggest_clicked(0))
        self.suggestButton[1].clicked.connect(lambda: self.suggest_clicked(1))
        self.suggestButton[2].clicked.connect(lambda: self.suggest_clicked(2))
        self.suggestButton[3].clicked.connect(lambda: self.suggest_clicked(3))
        self.suggestButton[4].clicked.connect(lambda: self.suggest_clicked(4))

        # button logics
        bind(self)
        # for i in range(5):
        #     print("done binding for {}".format(i))
        #     self.suggestButton[i].clicked.connect(lambda: self.suggest_clicked(i))
        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

        self.generator: TextGenerator = TextGenerator()

        # self.textEdit.setText(res)
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

    def suggest_clicked(self, key):
        self.prevWord = self.prevWord + self.currentWord[0] + self.res[key]
        self.reset_word()
        self.post_input_clicked()


    def post_input_clicked(self):
        self.currentWord[0] = bogo.process_sequence(self.currentWord[0])
        self.textEdit.setText(self.prevWord + self.currentWord[0]+'|')
        prompt = self.prevWord + self.currentWord[0]
        self.res = self.generator.genText(prompt)
        pos = len(prompt.split(' '))
        print(pos)

        for i in range(5):
            self.res[i] = self.res[i][pos]
            self.suggestButton[i].setText(self.res[i])

    def input_clicked(self, key):
        currTime = time.monotonic()
        inputInterval = currTime - self.prevTime
        prevKeyValue = self.prevKey[0]
        prevKeyCount = self.prevKey[1]

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
            self.finalize_word()
        self.prevTime = currTime
        self.post_input_clicked()

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

    def finalize_word(self):
        if(not self.currentWord[1]):
            self.currentWord[0] = bogo.process_sequence(self.currentWord[0])
            self.currentWord[1] = True
        pass

    def reset_word(self):
        self.currentWord[0] = ''
        self.currentWord[1] = False
        self.prevTime = time.monotonic()
        self.prevKey = [-1, 0]

    def space_clicked(self):
        self.prevWord = self.prevWord + self.currentWord[0] + ' '
        self.textEdit.setText(self.prevWord + '|')
        self.reset_word()

    def del_clicked(self):
        self.prevTime = time.monotonic()
        self.prevKey = [-1, 0]
        if (self.currentWord[0]):
            self.currentWord[0] = self.currentWord[0][:-1]
            if(self.currentWord[0] == ''):
                self.reset_word()
        else:
            if (self.prevWord):
                self.prevWord = self.prevWord[:-1]
        self.textEdit.setText(self.prevWord + self.currentWord[0] + '|')
        self.post_input_clicked()

    def speaker_clicked(self):
        self.finalize_word()
        text = self.prevWord + self.currentWord[0]
        output = gTTS(text, lang="vi", slow=False)
        msg = QMessageBox()
        msg.setWindowTitle('Dang phat tieng')
        x = msg.show()
        output.save("output.mp3")
        playsound("output.mp3")
        os.remove("output.mp3")

    def mic_clicked(self):

        session = QMediaCaptureSession()
        audioInput = QAudioInput()
        session.setAudioInput(audioInput)
        recorder = QMediaRecorder()
        session.setRecorder(recorder)
        recorder.setMediaFormat(QMediaFormat.FileFormat.Wave)
        filename = Path(QDir.currentPath()) / "test"
        url = QUrl.fromLocalFile(os.fspath(filename))
        recorder.setOutputLocation(url)
        recorder.record()
        msg = QMessageBox()
        button = QMessageBox.StandardButton(0)
        msg.addButton(button)
        # button.show()
        msg.exec_()
        recorder.stop()
        subprocess.call(['ffmpeg', '-y', '-i', 'test.m4a',
                         './audio.wav'])
        self.handle_stt()

    def handle_stt(self):
        if(not self.currentWord[1]):
            self.currentWord[0] = bogo.process_sequence(self.currentWord[0])
            self.currentWord[1] = True
        with sr.WavFile('audio.wav') as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="vi-VI")
                self.prevWord = self.prevWord + self.currentWord[0]
                self.currentWord[0] = text
                self.currentWord[1] = True
                self.textEdit.setText(
                    self.prevWord + self.currentWord[0] + '|')
            except:
                print("Xin lỗi! tôi không nhận được voice!")
