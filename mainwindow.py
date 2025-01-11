# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
import image_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(650, 500)
        MainWindow.setStyleSheet(u"background-image:url(D:/AAA_document_Lv/\u8bfe/Python/\u5b9e\u8bad\u722c\u866b/background.jpg);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:transparent;\n"
"")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(70, 110, 531, 101))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(28)
        self.title_label.setFont(font)
        self.title_label.setLayoutDirection(Qt.LeftToRight)
        self.title_label.setStyleSheet(u"background:transparent;\n"
"color:rgb(255,255,255)")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(150, 170, 361, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.crawl_btn = QPushButton(self.verticalLayoutWidget)
        self.crawl_btn.setObjectName(u"crawl_btn")
        self.crawl_btn.setMaximumSize(QSize(359, 32))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(20)
        self.crawl_btn.setFont(font1)
        self.crawl_btn.setStyleSheet(u"background:transparent;\n"
"color:rgb(255,255,0)")

        self.verticalLayout.addWidget(self.crawl_btn)

        self.query_btn = QPushButton(self.verticalLayoutWidget)
        self.query_btn.setObjectName(u"query_btn")
        self.query_btn.setFont(font1)
        self.query_btn.setStyleSheet(u"background:transparent;\n"
"color:rgb(255,255,0)")

        self.verticalLayout.addWidget(self.query_btn)

        self.visual_btn = QPushButton(self.verticalLayoutWidget)
        self.visual_btn.setObjectName(u"visual_btn")
        self.visual_btn.setFont(font1)
        self.visual_btn.setStyleSheet(u"background:transparent;\n"
"color:rgb(255,255,0)")

        self.verticalLayout.addWidget(self.visual_btn)

        self.exit_btn = QPushButton(self.verticalLayoutWidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setFont(font1)
        self.exit_btn.setStyleSheet(u"background:transparent;\n"
"color:rgb(255,255,0)")

        self.verticalLayout.addWidget(self.exit_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        self.crawl_btn.clicked.connect(MainWindow.crawlData)  # 连接到main.py中crawlData方法
        self.query_btn.clicked.connect(MainWindow.queryData)  # 连接到main.py中queryData方法
        self.visual_btn.clicked.connect(MainWindow.visualData)  # 连接到main.py中visualData方法
        self.exit_btn.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e2d\u56fd\u5927\u5b66MOOC\u8bfe\u7a0b\u6570\u636e\u722c\u53d6\u53ca\u5206\u6790\u7cfb\u7edf", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u6570\u636e\u722c\u53d6\u53ca\u5206\u6790\u7cfb\u7edf", None))
        self.crawl_btn.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u722c\u53d6", None))
        self.query_btn.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u67e5\u8be2", None))
        self.visual_btn.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u53ef\u89c6\u5316\u5206\u6790", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
    # retranslateUi

