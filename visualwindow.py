# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'visualwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGroupBox,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
import top_rc

class Ui_VisualWindow(object):
    def setupUi(self, VisualWindow):
        if not VisualWindow.objectName():
            VisualWindow.setObjectName(u"VisualWindow")
        VisualWindow.resize(650, 500)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        font.setBold(True)
        VisualWindow.setFont(font)
        self.centralwidget = QWidget(VisualWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.top_label = QLabel(self.centralwidget)
        self.top_label.setObjectName(u"top_label")
        self.top_label.setGeometry(QRect(0, 0, 650, 64))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.top_label.setFont(font1)
        self.top_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-image: url(:/a/top.jpg);")
        self.top_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(80, 170, 500, 280))
        self.cloud_groupbox = QGroupBox(self.centralwidget)
        self.cloud_groupbox.setObjectName(u"cloud_groupbox")
        self.cloud_groupbox.setGeometry(QRect(20, 60, 240, 111))
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.cloud_groupbox.setFont(font2)
        self.wordnum_label = QLabel(self.cloud_groupbox)
        self.wordnum_label.setObjectName(u"wordnum_label")
        self.wordnum_label.setGeometry(QRect(10, 20, 141, 20))
        self.wordnum_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wordnum_combobox = QComboBox(self.cloud_groupbox)
        self.wordnum_combobox.setObjectName(u"wordnum_combobox")
        self.wordnum_combobox.setGeometry(QRect(140, 10, 81, 31))
        self.wordnum_combobox.setEditable(True)
        self.schoolcloud_btn = QPushButton(self.cloud_groupbox)
        self.schoolcloud_btn.setObjectName(u"schoolcloud_btn")
        self.schoolcloud_btn.setGeometry(QRect(40, 44, 161, 31))
        self.coursecloud_btn = QPushButton(self.cloud_groupbox)
        self.coursecloud_btn.setObjectName(u"coursecloud_btn")
        self.coursecloud_btn.setGeometry(QRect(40, 74, 161, 31))
        self.pie_groupbox = QGroupBox(self.centralwidget)
        self.pie_groupbox.setObjectName(u"pie_groupbox")
        self.pie_groupbox.setGeometry(QRect(280, 60, 351, 111))
        self.pie_groupbox.setFont(font2)
        self.school_label = QLabel(self.pie_groupbox)
        self.school_label.setObjectName(u"school_label")
        self.school_label.setGeometry(QRect(10, 20, 71, 20))
        self.school_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.school_text = QTextEdit(self.pie_groupbox)
        self.school_text.setObjectName(u"school_text")
        self.school_text.setGeometry(QRect(80, 10, 120, 30))
        self.coursenum_label = QLabel(self.pie_groupbox)
        self.coursenum_label.setObjectName(u"coursenum_label")
        self.coursenum_label.setGeometry(QRect(210, 20, 61, 20))
        self.coursenum_label.setFont(font2)
        self.coursenum_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coursenum_combobox = QComboBox(self.pie_groupbox)
        self.coursenum_combobox.setObjectName(u"coursenum_combobox")
        self.coursenum_combobox.setGeometry(QRect(260, 20, 51, 21))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(8)
        font3.setBold(False)
        self.coursenum_combobox.setFont(font3)
        self.coursenum_combobox.setEditable(True)
        self.enrollbar_btn = QPushButton(self.pie_groupbox)
        self.enrollbar_btn.setObjectName(u"enrollbar_btn")
        self.enrollbar_btn.setGeometry(QRect(40, 40, 261, 31))
        self.evaluatebar_btn = QPushButton(self.pie_groupbox)
        self.evaluatebar_btn.setObjectName(u"evaluatebar_btn")
        self.evaluatebar_btn.setGeometry(QRect(40, 70, 261, 31))
        VisualWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VisualWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 33))
        VisualWindow.setMenuBar(self.menubar)

        self.retranslateUi(VisualWindow)

        QMetaObject.connectSlotsByName(VisualWindow)
    # setupUi
        self.schoolcloud_btn.clicked.connect(VisualWindow.schoolCloud)  # 连接到visualdata.py中schoolCloud()方法
        self.coursecloud_btn.clicked.connect(VisualWindow.courseCloud)  # 连接到visualdata.py中courseCloud()方法
        self.enrollbar_btn.clicked.connect(VisualWindow.enrollBar)  # 连接到visualdata.py中enrollBar()方法
        self.evaluatebar_btn.clicked.connect(VisualWindow.evaluateBar)  # 连接到visualdata.py中evaluateBar()方法

    def retranslateUi(self, VisualWindow):
        VisualWindow.setWindowTitle(QCoreApplication.translate("VisualWindow", u"\u6570\u636e\u53ef\u89c6\u5316", None))
        self.top_label.setText(QCoreApplication.translate("VisualWindow", u"\u6570\u636e\u53ef\u89c6\u5316      ", None))
        self.cloud_groupbox.setTitle(QCoreApplication.translate("VisualWindow", u"\u4e91\u56fe", None))
        self.wordnum_label.setText(QCoreApplication.translate("VisualWindow", u"\u9009\u62e9\u8bfe\u7a0b\u6570\uff08\u5b66\u6821\u6570\uff09", None))
        self.wordnum_combobox.setCurrentText(QCoreApplication.translate("VisualWindow", u"10", None))
        self.schoolcloud_btn.setText(QCoreApplication.translate("VisualWindow", u"\u5f00\u8bfe\u95e8\u6570\u7684\u5b66\u6821\u8bcd\u4e91", None))
        self.coursecloud_btn.setText(QCoreApplication.translate("VisualWindow", u"\u53c2\u52a0\u4eba\u6570\u7684\u8bfe\u7a0b\u8bcd\u4e91", None))
        self.pie_groupbox.setTitle(QCoreApplication.translate("VisualWindow", u"\u997c\u56fe", None))
        self.school_label.setText(QCoreApplication.translate("VisualWindow", u"\u5b66\u6821\u540d\u79f0", None))
        self.coursenum_label.setText(QCoreApplication.translate("VisualWindow", u"\u8bfe\u7a0b\u6570", None))
        self.coursenum_combobox.setCurrentText(QCoreApplication.translate("VisualWindow", u"5", None))
        self.enrollbar_btn.setText(QCoreApplication.translate("VisualWindow", u"\u53c2\u52a0\u4eba\u6570\u6700\u591a\u7684\u8bfe\u7a0b\u997c\u56fe", None))
        self.evaluatebar_btn.setText(QCoreApplication.translate("VisualWindow", u"\u8bc4\u4ef7\u4eba\u6570\u6700\u591a\u7684\u8bfe\u7a0b\u997c\u56fe", None))
    # retranslateUi

