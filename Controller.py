from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
                               QTextEdit, QToolButton, QWidget, QLabel, QMessageBox)

def bind(self):
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
        # self.suggestButton.clicked.connect()
    