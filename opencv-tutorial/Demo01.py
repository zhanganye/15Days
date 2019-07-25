# -*- coding:utf-8 -*-
import cv2
import imutils

def showImage(path):
    img = cv2.imread(path)
    cv2.imshow('原图', img)

    (h, w, d) = img.shape
    print(h, w, d)

    (B, G, R) = img[3, 8]
    print("R={}, G={}, B={}".format(R, G, B))

    roi = img[60:500, 10:200, 2]
    cv2.imshow('部分', roi)

    resize = cv2.resize(img, (int(w * 0.8), int(h*0.8)))
    cv2.imshow('resize', resize)

    resize2 = imutils.resize(img, height =300)
    cv2.imshow('resize2', resize2)

    cv2.waitKey(0)

def fun1(path):
    img = cv2.imread(path)
    cv2.imshow('img', img)

    (h, w, d) = img.shape
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, -45, 1.0)
    rotated = cv2.warpAffine(img, M, (w*2, h*2))
    cv2.imshow('rotaing', rotated)
    cv2.waitKey(0)


if __name__ == '__main__':
    picPath = 'jp.png'
    # showImage(picPath)
    fun1(picPath)