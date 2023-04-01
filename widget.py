# This Python file uses the following encoding: utf-8
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


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form_2 import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    app.exec()
    sys.exit(app.exec())
    
