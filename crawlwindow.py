# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crawlwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import image_rc

class Ui_CrawlWindow(object):
    def setupUi(self, CrawlWindow):
        if not CrawlWindow.objectName():
            CrawlWindow.setObjectName(u"CrawlWindow")
        CrawlWindow.resize(650, 500)
        CrawlWindow.setStyleSheet(u"background-image: url(:/a/background.jpg);")
        self.centralwidget = QWidget(CrawlWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(100, 110, 461, 331))
        self.listView.setStyleSheet(u"background: transparent")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(100, 110, 461, 81))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(36)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"background:transparent;\n"
"color: rgb(255, 255, 255);")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.show_label = QLabel(self.centralwidget)
        self.show_label.setObjectName(u"show_label")
        self.show_label.setGeometry(QRect(120, 180, 411, 41))
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(11)
        self.show_label.setFont(font1)
        self.show_label.setStyleSheet(u"background:transparent")
        self.show_label.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(170, 220, 321, 221))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.crawlSchool_btn = QPushButton(self.verticalLayoutWidget)
        self.crawlSchool_btn.setObjectName(u"crawlSchool_btn")
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        font2.setPointSize(26)
        self.crawlSchool_btn.setFont(font2)
        self.crawlSchool_btn.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.534, stop:0 rgba(161, 161, 161, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.verticalLayout.addWidget(self.crawlSchool_btn)

        self.crawlCourse_btn = QPushButton(self.verticalLayoutWidget)
        self.crawlCourse_btn.setObjectName(u"crawlCourse_btn")
        self.crawlCourse_btn.setFont(font2)
        self.crawlCourse_btn.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.534, stop:0 rgba(161, 161, 161, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.verticalLayout.addWidget(self.crawlCourse_btn)

        self.exit_btn = QPushButton(self.verticalLayoutWidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setFont(font2)
        self.exit_btn.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.534, stop:0 rgba(161, 161, 161, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.verticalLayout.addWidget(self.exit_btn)

        CrawlWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CrawlWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 26))
        CrawlWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CrawlWindow)
        self.statusbar.setObjectName(u"statusbar")
        CrawlWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CrawlWindow)

        QMetaObject.connectSlotsByName(CrawlWindow)
    # setupUi
        self.crawlSchool_btn.clicked.connect(CrawlWindow.crawlSchool)  # 连接到crawldata.py中crawlSchool方法
        self.crawlCourse_btn.clicked.connect(CrawlWindow.crawlcourse)  # 连接到crawldata.py中crawlCourse方法
        self.exit_btn.clicked.connect(CrawlWindow.close)

    def retranslateUi(self, CrawlWindow):
        CrawlWindow.setWindowTitle(QCoreApplication.translate("CrawlWindow", u"\u6570\u636e\u722c\u53d6", None))
        self.title_label.setText(QCoreApplication.translate("CrawlWindow", u"\u6570  \u636e  \u722c  \u53d6", None))
        self.show_label.setText("")
        self.crawlSchool_btn.setText(QCoreApplication.translate("CrawlWindow", u"\u722c\u53d6\u5927\u5b66\u6570\u636e", None))
        self.crawlCourse_btn.setText(QCoreApplication.translate("CrawlWindow", u"\u722c\u53d6\u8bfe\u7a0b\u6570\u636e", None))
        self.exit_btn.setText(QCoreApplication.translate("CrawlWindow", u"\u9000\u51fa", None))
    # retranslateUi

