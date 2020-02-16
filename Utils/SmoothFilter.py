import cv2
#使用高斯滤波平滑图像边界，能够让基于图分割的图像效果更好
class SmoothFilter(object):
    def __init__(self,img,sigma=0,core=(3,3)):
        self.sigma=sigma
        self.core=core
        self.img=img

    def filter(self):
        return cv2.GaussianBlur(self.img,self.core,self.sigma)
