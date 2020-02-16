import numpy as np
from DataStructure.DSU import dsu
# 上下左右四个方向区域扩展
ways = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# 使用并查集进行图像分割（类似区域拓展区域分割）
class ImageCut(object):
    # 初始化 scale为欧式距离平方的限界
    def __init__(self, img, scale):
        self.img = img
        self.rows = img.shape[0]
        self.cols = img.shape[1]
        self.Dsu = dsu(self.rows, self.cols)
        self.scale = scale

    # 欧式距离的平方
    def Distance(self, veca, vecb):
        return sum(np.power(veca - vecb, 2))

    # 如果相邻两个点欧式距离平方不超过scale则将这两个点所在集合合并
    def Cut(self):
        for x in range(self.rows):
            for y in range(self.cols):
                for way in ways:
                    tx = x + way[0]
                    ty = y + way[1]
                    if 0 <= tx < self.rows and 0 <= ty < self.cols and self.Distance(self.img[tx, ty],
                                                                                     self.img[x, y]) <= self.scale:
                        self.Dsu.PointUnion(x, y, tx, ty)
            if x % 100 == 0:
                print(x / self.rows * 100, "%")
        print("100%")

    # 二维坐标点展成一维后的编号id
    def GetId(self, x: int, y: int):
        return x * self.cols + y

    # 对图片进行重新染色，使用集合中rgb的平均值作为最终颜色，返回重新染色后的图像
    def RePaint(self):
        self.Cut()
        fa = self.Dsu.GetAll()
        Map2Num = {}
        Map2Val = {}
        for i in range(self.rows):
            for j in range(self.cols):
                id = self.GetId(i, j)
                if fa[id] in Map2Num:
                    Map2Num[fa[id]] = Map2Num[fa[id]] + 1
                    Map2Val[fa[id]] = Map2Val[fa[id]] + self.img[i, j]
                else:
                    Map2Num[fa[id]] = 1
                    Map2Val[fa[id]] = np.zeros(3, dtype=int) + self.img[i, j]

        for id in Map2Num.keys():
            Map2Val[id] = np.uint8(Map2Val[id] / Map2Num[id])

        retimg = np.zeros(self.img.shape, dtype=np.uint8)

        for i in range(self.rows):
            for j in range(self.cols):
                retimg[i, j] = Map2Val[fa[self.GetId(i, j)]]
        return retimg
