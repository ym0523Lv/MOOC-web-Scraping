from visualwindow import  Ui_VisualWindow
from PySide6.QtWidgets import *
from db_conn import DbConn

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#创建一个matplotlib图形绘制类，这是连接PySide6与matplotlib的关键
class MyFigureCanvas(FigureCanvas):
    def __init__(self, width, height, dpi=100):
         # 创建一个Figure,该Figure为matplotlib下的Figure，不是matplotlib.pyplot下面的Figure
         # 注意：plt.figure不能写成plt.Figure，否则在控件中不显示图像，只显示图形
        self.fig = plt.figure(figsize=(width, height), dpi=dpi)
        # 在父类中激活Figure窗口，此句必不可少，否则不能显示图形
        super(MyFigureCanvas,self).__init__(self.fig)
        # 调用Figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot(1,1,1)方法
        self.axes = self.fig.add_subplot(111)  # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

class Visualdata(QMainWindow,Ui_VisualWindow):
    def __init__(self,parent=None):
        super(Visualdata, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = DbConn()
        # 添加rc参数 实现在图形中显示中文
        plt.rcParams["font.sans-serif"] = "SimHei"
        plt.rcParams["axes.unicode_minus"]= False

    def word_cloud(self,data,number):
        # 配置词云参数
        wc = WordCloud(
            # 设置字体
            font_path='C:\\windows\\Fonts\\STSONG.TTF',
            # 设置背景色
            background_color='white',
            # 允许最大词汇
            max_words=number,
            # 最大号字体
            max_font_size=50,
            random_state=100,  #为每个单词返回一个PIL颜色
        )
        # 生成词云
        wc.generate_from_frequencies(data)
        return wc

    def schoolCloud(self):
        # 实例化一个FigureCanvas
        self.figure_visual = MyFigureCanvas(width=self.graphicsView.width() / 101,
                                            height=self.graphicsView.height() / 101, dpi=100)
        conn, cursor = self.db.open_conn()
        sc_name = []
        sc_count = []
        # 获取下拉列表框选中选项的文本
        num = self.wordnum_combobox.currentText().strip()
        cursor.execute("select schoolName,courseTotleCount from school")
        results = cursor.fetchall()
        # 把从数据库中读取元组数据转化为列表
        for i in results:
            sc_name.append(i[0])
            sc_count.append(i[1])
        # 把两个列表数据转化为字典
        dic = dict(zip(sc_name, sc_count))
        # 调用word_cloud()方法绘制词云
        wc = self.word_cloud(dic,int(num))
        # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
        self.figure_visual.axes.clear()
        # 云图的标题
        self.figure_visual.axes.set_title('开课门数最多的学校名称词云')
        plt.imshow(wc)
        plt.axis('off')  #关闭坐标轴
        #加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(self.figure_visual)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 调用show方法呈现图形

    def courseCloud(self):
        # 实例化一个FigureCanvas
        self.figure_visual = MyFigureCanvas(width=self.graphicsView.width() / 101,
                                            height=self.graphicsView.height() / 101, dpi=100)
        conn, cursor = self.db.open_conn()
        cs_name = []
        cs_count = []
        # 获取下拉列表框选中选项的文本
        num = self.wordnum_combobox.currentText().strip()
        cursor.execute("select courseName,enrollCount from course")
        results = cursor.fetchall()
        # 把从数据库中读取元组数据转化为列表
        for i in results:
            cs_name.append(i[0])
            cs_count.append(i[1])
        # 把两个列表数据转化为字典
        dic = dict(zip(cs_name, cs_count))
        # 调用word_cloud()方法绘制词云
        wc = self.word_cloud(dic,int(num))
        # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
        self.figure_visual.axes.clear()
        # 云图的标题
        self.figure_visual.axes.set_title('参加人数最多的课程名称词云')
        plt.imshow(wc)
        plt.axis('off')
        #加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(self.figure_visual)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 调用show方法呈现图形

    def enrollBar(self):
        # 实例化一个FigureCanvas，用于在控件中显示饼图
        self.figure_visual = MyFigureCanvas(width=self.graphicsView.width() / 101,
                                            height=self.graphicsView.height() / 101, dpi=100)
        conn, cursor = self.db.open_conn()
        cs_name = []
        cs_count = []
        # 获取文本框输入的文本
        schoolname = self.school_text.toPlainText().strip()
        # 获取下拉列表框选中选项的文本
        num = self.coursenum_combobox.currentText().strip()
        sql = 'select courseName,enrollCount from course '
        if schoolname:
            sql += 'where ' + 'schoolName like "%{}%"'.format(schoolname)
        sql += ' order by enrollCount desc '
        if num and num.isdigit():
            sql += 'limit {}'.format(num)
        sql += ';'
        cursor.execute(sql)
        results = cursor.fetchall()
        for i in results:
            cs_name.append(i[0])
            cs_count.append(i[1])
        # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
        self.figure_visual.axes.clear()
        # 柱状图的标题
        self.figure_visual.axes.set_title('参加人数最多的课程柱状图')
        #倾斜显示x轴标签
        plt.xticks(rotation=20)
        #绘制柱状图
        plt.bar(x=cs_name, height=cs_count)
        #获取x轴标签信息
        xticks = self.figure_visual.axes.get_xticks()
        #每根柱子上方添加数值标签
        for i in range(len(xticks)):
            xy = (xticks[i], cs_count[i])
            s = str(cs_count[i])
            self.figure_visual.axes.annotate(
                s,  # 要添加的文本
                xy=xy,  # 将文本添加到哪个位置
                fontsize=12,  # 标签大小
                color="blue",  # 标签颜色
                ha="center",  # 水平对齐
                va="baseline"  # 垂直对齐
            )
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(self.figure_visual)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 调用show方法呈现图形



    def evaluateBar(self):
        # 实例化一个FigureCanvas，用于在控件中显示饼图
        self.figure_visual = MyFigureCanvas(width=self.graphicsView.width() / 101,
                                            height=self.graphicsView.height() / 101, dpi=100)
        conn, cursor = self.db.open_conn()
        cs_name = []
        cs_count = []
        # 获取文本框输入的文本
        schoolname = self.school_text.toPlainText().strip()
        # 获取下拉列表框选中选项的文本
        num = self.coursenum_combobox.currentText().strip()
        sql = 'select courseName,enrollCount from course '
        if schoolname:
            sql += 'where ' + 'schoolName like "%{}%"'.format(schoolname)
        sql += ' order by enrollCount '
        if num and num.isdigit():
            sql += 'limit {}'.format(num)
        sql += ';'
        cursor.execute(sql)
        results = cursor.fetchall()
        for i in results:
            cs_name.append(i[0])
            cs_count.append(i[1])
        # 由于图片需要反复绘制，所以每次绘制前清空，然后绘图
        self.figure_visual.axes.clear()
        # 柱状图的标题
        self.figure_visual.axes.set_title('评价人数最少的课程柱状图')
        # 倾斜显示x轴标签
        plt.xticks(rotation=20)
        # 绘制柱状图
        plt.bar(x=cs_name, height=cs_count)
        # 获取x轴标签信息
        xticks = self.figure_visual.axes.get_xticks()
        # 每根柱子上方添加数值标签
        for i in range(len(xticks)):
            xy = (xticks[i], cs_count[i])
            s = str(cs_count[i])
            self.figure_visual.axes.annotate(
                s,  # 要添加的文本
                xy=xy,  # 将文本添加到哪个位置
                fontsize=12,  # 标签大小
                color="blue",  # 标签颜色
                ha="center",  # 水平对齐
                va="baseline"  # 垂直对齐
            )
        # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        self.graphic_scene = QGraphicsScene()  # 创建一个QGraphicsScene
        self.graphic_scene.addWidget(self.figure_visual)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        self.graphicsView.setScene(self.graphic_scene)  # 把QGraphicsScene放入QGraphicsView
        self.graphicsView.show()  # 调用show方法呈现图形











