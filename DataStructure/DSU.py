import numpy as np

#并查集（数据结构）
class dsu(object):
    # 初始化
    def __init__(self, _rows: int, _cols: int):
        self.rows = _rows
        self.cols = _cols
        self.fa = np.arange(0, self.rows * self.cols)

    # 二维坐标点展成一维后的编号id
    def GetId(self, x: int, y: int):
        return x * self.cols + y

    # 寻找元素所处的集合（代表元素）
    def GetFather(self, x: int):
        list = []
        while (x != self.fa[x]):
            list.append(x)
            x = self.fa[x]
        for id in list:
            self.fa[id] = x
        return x

    # 合并两个集合
    def Union(self, x: int, y: int):
        tmpx = self.GetFather(x)
        tmpy = self.GetFather(y)
        if tmpx == tmpy:
            return False
        else:
            self.fa[tmpx] = tmpy

    # 找到所有点所处的集合
    def FindAll(self):
        for i in range(self.rows * self.cols):
            self.GetFather(i)

    # 使用二维坐标点坐标合并集合
    def PointUnion(self, x1: int, y1: int, x2: int, y2: int):
        return self.Union(self.GetId(x1, y1), self.GetId(x2, y2))

    # 返回存储所有点集合的array
    def GetAll(self):
        self.FindAll()
        return self.fa
