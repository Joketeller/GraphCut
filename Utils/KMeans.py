import cv2 as cv
import numpy as np
# KMeans聚类进行图像分割
def KMeans(img, size=100):
    # 展平
    img_flat = img.reshape((-1, 3))
    img_flat = np.float32(img_flat)
    # 迭代参数
    # 定义中心 (type,max_iter,epsilon)
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    # 设置标签
    flags = cv.KMEANS_RANDOM_CENTERS
    # KMeans
    compactness, labels, centers = cv.kmeans(img_flat, size, None, criteria, 10, flags)
    centers = np.uint8(centers)
    # 染色
    res = centers[labels.flatten()]
    return res.reshape((img.shape))
