'''
使用了Utils 和 DataStructure
'''
import numpy as np
import cv2 as cv
from Utils.SmoothFilter import SmoothFilter
from Utils.AreaCut import ImageCut
from Utils.KMeans import KMeans
from Utils.MeanShift import MeanShift

def LoadImage(url):
    if (len(url)==0):
        url='Butterfly.jpg'
    print("image url: ", url)
    return cv.imread(url)


if __name__=='__main__':
    url=input("Please Enter the path of Image，No input means the defalut image: Butterfly.jpg:\n")
    img=LoadImage(url)
    cv.imshow('org',img)
    print('Load OK')
    img=SmoothFilter(img).filter()
    print('Filter OK')
    cv.imshow('filtered',img)
    img = ImageCut(img, 90).RePaint()
    print('AreaCut OK')
    cv.imshow('AreaCut', img)
    kimg=KMeans(img,3)  #分为三类
    print('KMeans OK')
    cv.imshow('kmeansed',kimg)
    cv.imwrite('KMeans.jpg',kimg)
    mimg=np.uint8(MeanShift(img,_h_value=60))
    cv.imshow('Meanshifted', mimg)
    cv.imwrite('Meanshift.jpg', mimg)
    print('MeanShift OK')
    cv.waitKey(0) #任意按键退出预览


