# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'querywindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QTableView, QTextEdit, QWidget)
import top_rc

class Ui_QueryWindow(object):
    def setupUi(self, QueryWindow):
        if not QueryWindow.objectName():
            QueryWindow.setObjectName(u"QueryWindow")
        QueryWindow.resize(650, 500)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(10)
        font.setKerning(True)
        QueryWindow.setFont(font)
        QueryWindow.setStyleSheet(u"")
        QueryWindow.setAnimated(True)
        self.centralwidget = QWidget(QueryWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.top_label = QLabel(self.centralwidget)
        self.top_label.setObjectName(u"top_label")
        self.top_label.setGeometry(QRect(0, 0, 650, 64))
        font1 = QFont()
        font1.setFamilies([u"\u6977\u4f53"])
        font1.setPointSize(23)
        font1.setBold(True)
        font1.setKerning(True)
        self.top_label.setFont(font1)
        self.top_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.top_label.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"background-image:url(:/a/top.jpg)")
        self.top_label.setTextFormat(Qt.TextFormat.AutoText)
        self.top_label.setScaledContents(False)
        self.top_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.top_label.setWordWrap(False)
        self.top_label.setOpenExternalLinks(True)
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 160, 621, 290))
        self.num_label = QLabel(self.centralwidget)
        self.num_label.setObjectName(u"num_label")
        self.num_label.setGeometry(QRect(440, 140, 111, 20))
        self.num_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.num_comboBox = QComboBox(self.centralwidget)
        self.num_comboBox.setObjectName(u"num_comboBox")
        self.num_comboBox.setGeometry(QRect(560, 140, 68, 22))
        self.num_comboBox.setEditable(True)
        self.query_widget = QWidget(self.centralwidget)
        self.query_widget.setObjectName(u"query_widget")
        self.query_widget.setGeometry(QRect(10, 60, 620, 60))
        self.school_label = QLabel(self.query_widget)
        self.school_label.setObjectName(u"school_label")
        self.school_label.setGeometry(QRect(10, 10, 54, 31))
        self.school_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.school_text = QTextEdit(self.query_widget)
        self.school_text.setObjectName(u"school_text")
        self.school_text.setGeometry(QRect(60, 10, 104, 30))
        self.course_label = QLabel(self.query_widget)
        self.course_label.setObjectName(u"course_label")
        self.course_label.setGeometry(QRect(190, 10, 54, 30))
        self.course_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.course_text = QTextEdit(self.query_widget)
        self.course_text.setObjectName(u"course_text")
        self.course_text.setGeometry(QRect(240, 10, 104, 30))
        self.teacher_label = QLabel(self.query_widget)
        self.teacher_label.setObjectName(u"teacher_label")
        self.teacher_label.setGeometry(QRect(370, 10, 71, 30))
        self.teacher_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.teacher_text = QTextEdit(self.query_widget)
        self.teacher_text.setObjectName(u"teacher_text")
        self.teacher_text.setGeometry(QRect(440, 10, 104, 30))
        self.query_btn = QPushButton(self.query_widget)
        self.query_btn.setObjectName(u"query_btn")
        self.query_btn.setGeometry(QRect(570, 20, 51, 24))
        self.queryBtn_widget = QWidget(self.centralwidget)
        self.queryBtn_widget.setObjectName(u"queryBtn_widget")
        self.queryBtn_widget.setGeometry(QRect(10, 110, 621, 30))
        self.enrollLess_btn = QPushButton(self.queryBtn_widget)
        self.enrollLess_btn.setObjectName(u"enrollLess_btn")
        self.enrollLess_btn.setGeometry(QRect(170, 0, 141, 31))
        self.enrollMore_btn = QPushButton(self.queryBtn_widget)
        self.enrollMore_btn.setObjectName(u"enrollMore_btn")
        self.enrollMore_btn.setGeometry(QRect(10, 0, 141, 31))
        self.markMore_btn = QPushButton(self.queryBtn_widget)
        self.markMore_btn.setObjectName(u"markMore_btn")
        self.markMore_btn.setGeometry(QRect(330, 0, 141, 31))
        self.markLess_btn = QPushButton(self.queryBtn_widget)
        self.markLess_btn.setObjectName(u"markLess_btn")
        self.markLess_btn.setGeometry(QRect(480, 0, 141, 31))
        QueryWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(QueryWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 33))
        QueryWindow.setMenuBar(self.menubar)

        self.retranslateUi(QueryWindow)

        QMetaObject.connectSlotsByName(QueryWindow)
    # setupUi
        self.query_btn.clicked.connect(QueryWindow.queryData)  # 连接到querydata.py中queryData方法
        #self.enrollMore_btn.clicked.connect(QueryWindow.enrollMore)  # 连接到querydata.py中enrollMore方法
        #self.enrollLess_btn.clicked.connect(QueryWindow.enrollLess)  # 连接到querydata.py中enrollLess方法
        #self.markMore_btn.clicked.connect(QueryWindow.markMore)  # 连接到querydata.py中markMore方法
        #self.markLess_btn.clicked.connect(QueryWindow.markLess)  # 连接到querydata.py中markLess方法

    def retranslateUi(self, QueryWindow):
        QueryWindow.setWindowTitle(QCoreApplication.translate("QueryWindow", u"\u6570\u636e\u67e5\u8be2", None))
        self.top_label.setText(QCoreApplication.translate("QueryWindow", u"\u6570\u636e\u67e5\u8be2     ", None))
        self.num_label.setText(QCoreApplication.translate("QueryWindow", u"\u9009\u62e9\u663e\u793a\u6570\u636e\u6761\u6570", None))
        self.num_comboBox.setCurrentText(QCoreApplication.translate("QueryWindow", u"\u5168\u90e8", None))
        self.school_label.setText(QCoreApplication.translate("QueryWindow", u"\u5b66\u6821\u540d", None))
        self.course_label.setText(QCoreApplication.translate("QueryWindow", u"\u8bfe\u7a0b\u540d", None))
        self.teacher_label.setText(QCoreApplication.translate("QueryWindow", u"\u6388\u8bfe\u6559\u5e08", None))
        self.query_btn.setText(QCoreApplication.translate("QueryWindow", u"\u67e5\u8be2", None))
        self.enrollLess_btn.setText(QCoreApplication.translate("QueryWindow", u"\u8bfe\u7a0b\u53c2\u52a0\u4eba\u6570\u6700\u5c11", None))
        self.enrollMore_btn.setText(QCoreApplication.translate("QueryWindow", u"\u8bfe\u7a0b\u53c2\u52a0\u4eba\u6570\u6700\u591a", None))
        self.markMore_btn.setText(QCoreApplication.translate("QueryWindow", u"\u8bfe\u7a0b\u8bc4\u4ef7\u5206\u6570\u6700\u9ad8", None))
        self.markLess_btn.setText(QCoreApplication.translate("QueryWindow", u"\u8bfe\u7a0b\u8bc4\u4ef7\u5206\u6570\u6700\u4f4e", None))
    # retranslateUi

