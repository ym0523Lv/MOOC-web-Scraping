from PySide6.QtCore import QAbstractTableModel,QModelIndex,Qt

#设置数据显示头名称
HEADERS = ('课程', '学校', '教师', '开课时间', '结束时间', '参加人数', '评分', '评价数')
CONVERTS_FUNS = [None, ] * len(HEADERS)

class DataModel(QAbstractTableModel):
    def __init__(self, headers=HEADERS):
        super().__init__()
        self.datas = []
        self.headers = headers

    # 载入数据函数
    def load(self, datas):
        self.beginResetModel()
        self.datas = datas
        self.endResetModel()

    # 供视图调用，以获取用以显示的数据
    def data(self,index,role=Qt.DisplayRole):
        if (not index.isValid() or not (0 <= index.row() < len(self.datas))):
            return None

        row,col = index.row(),index.column()
        data = self.datas[row]
        if role == Qt.DisplayRole:
            item = data[col]
            return item
        return None

    def rowCount(self,index=QModelIndex()):
        return len(self.datas)

    def columnCount(self,index=QModelIndex()):
        return len(self.headers)

    # 实现标题行的定义
    def headerData(self,section,orientation,role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            return self.headers[section]
        return int(section + 1)







