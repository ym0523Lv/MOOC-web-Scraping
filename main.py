from mainwindow import Ui_MainWindow
from crawldata import Crawldata
from querydata import Querydata
from visualdata import Visualdata
from PySide6.QtWidgets import *
import sys
class Main(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Main, self).__init__(parent=parent)
        self.setupUi(self)
    def crawlData(self):
        crawl.show()
    def queryData(self):
        query.show()
    def visualData(self):
        visual.show()

if __name__=='__main__':
    app = QApplication(sys.argv)  #实例化QApplication类，作为GUI主程序入口
    mainWindow=Main()   #实例化Main类
    crawl = Crawldata()  #实例化数据爬取类
    query = Querydata()  #实例化数据查询类
    visual = Visualdata()  #实例化数据可视化类
    mainWindow.show()   #显示窗体
    app.exec_()
    sys.exit()
