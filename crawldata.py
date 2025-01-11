from crawlwindow import  Ui_CrawlWindow
from PySide6.QtWidgets import *
from PySide6 import QtWidgets
import requests
from lxml import etree
import re
import time
from db_conn import DbConn

class Crawldata(QMainWindow,Ui_CrawlWindow):
    def __init__(self,parent=None):
        super(Crawldata, self).__init__(parent=parent)
        self.setupUi(self)
        self.db = DbConn()
        self.datas = []
        self.school_urls = []

    def crawlSchool(self):
        conn, cursor = self.db.open_conn()
        #检查数据库表school中是否已经有数据
        sql = 'select * from school'
        sql += ';'
        cursor.execute(sql)
        datas = cursor.fetchall()
        if datas:
            reply = QtWidgets.QMessageBox.question(self, '提示信息', '学校数据已经存在，是否清空原有数据，重新爬取？',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                #清空数据库表school的内容
                sql = 'delete from school'
                sql += ';'
                cursor.execute(sql)
                cursor.connection.commit()
            else:
                return
        self.show_label.setText("正在爬取学校数据，请耐心等待")
        self.crawlSchool_btn.setText("waiting......")
        self.crawlSchool_btn.setEnabled(False)
        self.crawlCourse_btn.setEnabled(False)
        self.exit_btn.setEnabled(False)
        QApplication.processEvents()  #实时刷新界面
        # 创建头部信息
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        # 需要爬取网页的网址
        url = "https://www.icourse163.org/university/view/all.htm"
        # 发送网络请求
        res = requests.get(url, headers=headers)
        # 获取相应文本，也就是对应html页面的文本信息
        school_res = res.text
        # 把HTML源码转变成_Element对象
        page = etree.HTML(school_res)
        school_ID = []
        school_name = []
        school_SN = []
        school_urls = []
        # 获取学校中文名称
        for i in page.xpath('//*[@id="g-body"]//a/img/@alt'):
            school_name.append(i)
        # 获取学校链接地址和英文简称
        url = "https://www.icourse163.org"
        for i in page.xpath('//*[@id="g-body"]//a/@href'):
            school_urls.append(url + i)
            school_SN.append(i[12:].strip())
        # 获取schoolId
        for url in school_urls[0:]:
            res = requests.get(url, headers=headers).text
            # 用re正则表达式获取网页源代码中schoolId的值
            schoolId = re.findall(r'window.schoolId = "(\d+)"', res)[0]
            school_ID.append(schoolId.strip())
        print( school_ID[1])
        self.crawlSchool_btn.setEnabled(True)
        self.crawlCourse_btn.setEnabled(True)
        self.exit_btn.setEnabled(True)
        self.show_label.setText("学校数据爬取成功！")
        self.crawlSchool_btn.setText("爬 取 学 校 数 据")
        # 把爬取到的学校数据存储到school表中
        for i in range(len(school_name)):
            cursor.execute(
                "insert into school(schoolID,schoolName,schoolSN,schoolURL)"
                " values('{}', '{}','{}','{}')".format(school_ID[i], school_name[i], school_SN[i], school_urls[i])
            )
        cursor.connection.commit()
        self.db.close_conn(conn, cursor)


    def crawlcourse(self):
        conn, cursor = self.db.open_conn()
        # 从school表中获取学校地址
        sql = 'select schoolURL from school'
        sql += ';'
        cursor.execute(sql)
        data = cursor.fetchall()
        if not(data):
            QtWidgets.QMessageBox.warning(self, "警告", "请先爬取学校数据")
            return
        # fetchall获得的是tuple元组数据，要转换为列表
        for i in data:
            self.school_urls.append(i[0])
        # 检查数据库表course中是否已经有数据
        sql = 'select * from course'
        sql += ';'
        cursor.execute(sql)
        datas = cursor.fetchall()
        if datas:
            reply = QtWidgets.QMessageBox.question(self, '提示信息', '课程数据已经存在，是否清除原有数据，重新爬取？',
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # 清空数据库表school的内容
                sql = 'delete from course'
                sql += ';'
                cursor.execute(sql)
                cursor.connection.commit()
            else:
                return
        self.show_label.setText("正在爬取课程数据，请耐心等待")
        self.crawlCourse_btn.setText("waiting......")
        self.crawlSchool_btn.setEnabled(False)
        self.crawlCourse_btn.setEnabled(False)
        self.exit_btn.setEnabled(False)
        QApplication.processEvents()  # 实时刷新界面
        headers = {
            'cookie': 'EDUWEBDEVICE=2238272f616d4e99ad13968d8d17f809; __yadk_uid=t0iXnOH0k9JwcF8PTqxAhWmcwBDP4dtF; __utma=63145271.1945292559.1616508903.1616508903.1616508903.1; __utmz=63145271.1616508903.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=ILwtvT7dT6RBFRQFUFd/xCfvKSYqEX5l; hasVolume=true; videoVolume=0.8; WM_NI=nso85YQorLW9lJupGWENQbnshXnJ+FomYmTd+hl515dLTNI30PdZPaSXMoI9ltpuNaNwAuIKMC++whajvoaB/po/2T6zpN/j2AhRy0h7na9u3mLtQf/EQpPkwplDAnnqZkE=; WM_NIKE=9ca17ae2e6ffcda170e2e6ee92cf6ffb9889daca3e8f8a8fb6c54f978f9aaff87dacac83b5e65bade79792cd2af0fea7c3b92aaeada1d9b85393b1beadd633b096bb91c65d87929f83ed79ac88a2abaa4eadb3978ed770e9b8a4d6b43fa8949cafcc39f490acbbd36b91888390cc33b0acc096cd6b8ea98f96cc418f9de5ccf664a3b6ba90e44aedb0a1d0b160f6a6c0afae62f29fa8b3fc3cace9a282bc7ff1b38495d46eed9b9f91d361b5b0a4a5c466aeaf968cc837e2a3; utm="eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cDovL2xvY2FsaG9zdDo4ODg4Lw=="; WX_WEBVIEW_AUTH=1; STUDY_WTR="RXy7L4XZfPmvMFsYXR57mM7jkIOFbiwLH2bLu59j3DuYHDDzGG1gelp8X3KDVDlHJUTMGZpuf6tE3Nb+1dY3FectFtLo2+dk1T5E80p7J2Q="; MOOC_PRIVACY_INFO_APPROVED=true; hb_MA-A976-948FFA05E931_source=localhost:8888; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1620109879,1620112395,1620112675,1620112815; NTESSTUDYSI=400283bb14674760a4f89c0f4d8c609a; NTES_YD_SESS=98M8rGIZKwqYJs2a5JzebaJTa69.dq9l8KAH79mEGMDErPh.QAcwBDiK.KCHDlYyTTX4wN6a7_06tbPU_lYMvLEqbMV2fjkJr_g_lM05uCRYrBS87.yUWJwobb.sMrO8_jgK2X.x3L8jKCtpWrPz3YFA8SjVRmZkl11VWV7jH_Tr16Eiv_OdafqvvViu69kOzOrgIoZAbtYY_nJFJWNnJYmTcu3lj.Sk9J1SH_9J_o4XT; NTES_YD_PASSPORT=V5LjnYNjYBSdb2XA.2Sk.3or7YjpVF.j4KSPd3z2rpK9ZnqeiEjDRK5mem7YKcvUSSTkDMy.6xWYmb3Kuq1okDF6ivmL43Nu7CKEn0uY1uGX4Hy8HTvd4mmp0Rc7szncHilNvus6jLoll2TbEmkUN2bACxkX51XYsCA6f1vOshGgfR1QS1bIGps9IRTjlfenVbW9kYSeG32m0OyvXO8UDhtAW; S_INFO=1620112897|0|3&80##|13717378202; P_INFO=13717378202|1620112897|1|imooc|00&99|gud&1618063872&imooc#gud&440500#10#0#0|&0|null|13717378202; STUDY_INFO="yd.9c87ec9048f04d6bb@163.com|8|1141190892|1620112898259"; STUDY_SESS="HSWw+UKn4Fn/O1hClGLQDIgcvj9DLtzp2edCyM/BR4m1IcnA9H2BXSSGOe/wVXK3SjPKhIFzp/bViei9eLNWzyY5yp2idAuW7A95VNd/Z0F36355dwB2S8UMO/h13WcqPz9haBgXAVtCpm+SISPfehGcDeFtXYLyHw61wQJpb4gLhur2Nm2wEb9HcEikV+3FTI8+lZKyHhiycNQo+g+/oA=="; STUDY_PERSIST="BrgWbQ8sf5eHRWkAZTjIHfiw+0/gMJH4njBby+08N4vY7AZsnFf2cUVqsF945RigeyMhSStj4PT/4nU0qHRwHRjdf8CF46rXRI2Hin7O4Cofr4xiZkckvpeI/Z3STnlkQntXkICIL2QYXYBpgGMk4/qnrLRbZBndhCSVmBODf8kl+vmTkwfJWSGAu35vGxk5Fyau91zGZu2Lh4AUwDNf+sgrm9vwgjSkT/GyNzhyd+nZgpjCC7Iso4RP9U87vJE8LtaQzUT1ovP2MqtW5+L3Hw+PvH8+tZRDonbf7gEH7JU="; NETEASE_WDA_UID=1141190892#|#1527731391171; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1620112955',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }
        totlePageCount = []  # 课程显示分页数
        totleCount = []  # 课程门数
        ids = []  # 课程ID
        name = []  # 课程名称
        enrollCount = []  # 参加课程学习人数
        teacherName = []  # 授课教师姓名
        schoolName = []  # 开课学校
        schoolSN = []  # 学校名英文缩写
        startTime = []  # 开课时间
        endTime = []  # 课程结束时间
        avgMark = []  # 课程评价分数
        evaluateCount = []  # 课程参与评价人数
        school_ID = []
        for url in self.school_urls[0:3]:
            # 获取schoolId
            r = requests.get(url, headers=headers).text
            schoolId = re.findall(r'schoolId = "(\d+)"', r)[0]
            school_ID.append(schoolId)
            # 获取每个学校的课程显示页数和总课程数
            url1 = "https://www.icourse163.org/web/j/courseBean.getCourseListBySchoolId.rpc?" \
                   "csrfKey=400283bb14674760a4f89c0f4d8c609a"
            data1 = {
                "schoolId": schoolId,
                "p": "1",
                "psize": "20",
                "type": "1",
                "courseStatus": "30"
            }
            res = requests.post(url=url1, data=data1, headers=headers)
            result = res.json()["result"]["query"]
            totlePageCount.append(result['totlePageCount'])
            totleCount.append(int(result['totleCount']))
            for page in range(1, result['totlePageCount'] + 1):
                data = {
                    "schoolId": schoolId,
                    "p": page,
                    "psize": "20",
                    "type": "1",
                    "courseStatus": "30"
                }
                res = requests.post(url=url1, data=data, headers=headers)
                try:
                    result = res.json()["result"]["list"]
                    for i in range(20):
                        ids.append(result[i]["id"])
                        name.append(result[i]["name"])
                        enrollCount.append(int(result[i]["enrollCount"]))
                        teacherName.append(result[i]["teacherName"])
                        schoolName.append(result[i]["schoolName"])
                        schoolSN.append(result[i]["schoolSN"])
                        startTime.append(time.strftime("%Y-%m-%d", time.localtime(result[i]["startTime"] / 1000)))
                        endTime.append(time.strftime("%Y-%m-%d", time.localtime(result[i]["endTime"] / 1000)))
                        url2 = 'https://www.icourse163.org/web/j/mocCourseV2RpcBean.getEvaluateAvgAndCount.rpc?csrfKey=400283bb14674760a4f89c0f4d8c609a'
                        data2 = {
                            "courseId": result[i]["id"]
                        }
                        res = requests.post(url=url2, data=data2, headers=headers)
                        try:
                            avgMark.append(res.json()["result"]["avgMark"])
                            evaluateCount.append(res.json()["result"]["evaluateCount"])
                        except:
                            avgMark.append("0")
                            evaluateCount.append("0")
                except:
                    break
        self.crawlSchool_btn.setEnabled(True)
        self.crawlCourse_btn.setEnabled(True)
        self.exit_btn.setEnabled(True)
        self.show_label.setText("课程数据爬取成功！")
        self.crawlCourse_btn.setText("爬 取 课 程 数 据")
        #把爬取到的学校开课门数写到school表中
        for i in range(len(totleCount)):
            cursor.execute(
                "update school set courseTotleCount='{}'"
                " where schoolID={}".format(totleCount[i], school_ID[i])
            )
        cursor.connection.commit()
        # 把爬取到的课程数据存储到course表中
        for i in range(0, len(ids)):
            cursor.execute(
                "insert into course(courseID,courseName,schoolName,teacherName,startTime,endTime,enrollCount,evaluateMark,evaluateCount)"
                " values('{}', '{}','{}','{}', '{}','{}','{}', '{}','{}')"
                    .format(ids[i], name[i], schoolName[i],teacherName[i], startTime[i],endTime[i], enrollCount[i],avgMark[i], evaluateCount[i])
            )
        cursor.connection.commit()







