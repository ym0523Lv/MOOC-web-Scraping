from querywindow import  Ui_QueryWindow
from PySide6.QtWidgets import *
from tab_model import DataModel
from db_conn import DbConn

class Querydata(QMainWindow,Ui_QueryWindow):
    def __init__(self,parent=None):
        super(Querydata, self).__init__(parent=parent)
        self.setupUi(self)
        self.user_model = DataModel()  #实例化DataModel类的对象，用于在Table View中显示数据
        self.tableView.setModel(self.user_model)
        self.db = DbConn()
        self.datas = []

    def queryData(self):
        conn, cursor = self.db.open_conn()
        #获取文本框输入的文本
        schoolname = self.school_text.toPlainText().strip()
        coursename = self.course_text.toPlainText().strip()
        teacher = self.teacher_text.toPlainText().strip()
        #获取下拉列表框选中选项的文本
        num = self.num_comboBox.currentText().strip()
        sql = 'select courseName,schoolName,teacherName,startTime,endTime,' \
              'enrollCount,evaluateMark,evaluateCount from course '
        wstr = []  #查询条件where后面的字符串
        if schoolname:
            wstr.append('schoolName like "%{}%"'.format(schoolname))
        if coursename:
            wstr.append('courseName like "%{}%"'.format(coursename))
        if teacher:
            wstr.append('teacherName like "%{}%"'.format(teacher))

        if wstr:
            wstr = ' and '.join(wstr)
            if wstr:
                sql += 'where ' + wstr
        if num and num.isdigit():
            sql += ' limit {}'.format(num)
        sql += ';'
        cursor.execute(sql)
        datas = cursor.fetchall()
        self.datas = [list(d) for d in datas]
        for data in self.datas:
            for i in range(len(data)):
                data[i] = str(data[i])
        self.user_model.load(self.datas)
        self.db.close_conn(conn, cursor)

    def enrollMore(self):
        conn, cursor = self.db.open_conn()
        num = self.num_comboBox.currentText().strip()
        sql = 'select courseName,schoolName,teacherName,startTime,endTime,enrollCount,' \
              'evaluateMark,evaluateCount from course order by enrollCount desc '
        if num and num.isdigit():
            sql += ' limit {}'.format(num)
        sql += ';'
        cursor.execute(sql)
        datas = cursor.fetchall()
        self.datas = [list(d) for d in datas]
        for data in self.datas:
            for i in range(len(data)):
                data[i] = str(data[i])
        self.user_model.load(self.datas)
        self.db.close_conn(conn, cursor)

    def enrollLess(self):
        conn, cursor = self.db.open_conn()
        num = self.num_comboBox.currentText().strip()
        sql = 'select courseName,schoolName,teacherName,startTime,endTime,enrollCount,' \
              'evaluateMark,evaluateCount from course order by enrollCount '
        if num and num.isdigit():
            sql += ' limit {}'.format(num)
        sql += ';'
        cursor.execute(sql)
        datas = cursor.fetchall()
        self.datas = [list(d) for d in datas]
        for data in self.datas:
            for i in range(len(data)):
                data[i] = str(data[i])
        self.user_model.load(self.datas)
        self.db.close_conn(conn, cursor)

    def markMore(self):
        conn, cursor = self.db.open_conn()
        num = self.num_comboBox.currentText().strip()
        sql = 'select courseName,schoolName,teacherName,startTime,endTime,enrollCount,' \
              'evaluateMark,evaluateCount from course order by evaluateMark desc '
        if num and num.isdigit():
            sql += ' limit {}'.format(num)
        sql += ';'
        cursor.execute(sql)
        datas = cursor.fetchall()
        self.datas = [list(d) for d in datas]
        for data in self.datas:
            for i in range(len(data)):
                data[i] = str(data[i])
        self.user_model.load(self.datas)
        self.db.close_conn(conn, cursor)

    def markLess(self):
        conn, cursor = self.db.open_conn()
        num = self.num_comboBox.currentText().strip()
        sql = 'select courseName,schoolName,teacherName,startTime,endTime,enrollCount,' \
              'evaluateMark,evaluateCount from course order by evaluateMark '
        if num and num.isdigit():
            sql += ' limit {}'.format(num)
        sql += ';'
        cursor.execute(sql)
        datas = cursor.fetchall()
        self.datas = [list(d) for d in datas]
        for data in self.datas:
            for i in range(len(data)):
                data[i] = str(data[i])
        self.user_model.load(self.datas)
        self.db.close_conn(conn, cursor)






