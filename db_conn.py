import pymysql
class DbConn():
    def open_conn(self):
        #建立连接
        conn = pymysql.connect(
            host = 'localhost',
            port = 3306,
            db = 'mooc',
            user = 'root',
            passwd='',
            charset = 'utf8mb4'
        )
        #创建游标
        cursor = conn.cursor()
        return conn,cursor
    def close_conn(self,conn,cursor):
        if cursor:
            cursor.close()
        if conn:
            conn.close()