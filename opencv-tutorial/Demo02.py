# -*- coding:utf-8 -*-

import cv2
import imutils

def fun(path):
    img = cv2.imread(path)
    cv2.imshow('original', img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)

    edged = cv2.Canny(gray, 100, 130)
    cv2.imshow('canny', edged)

    thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow('thresh', thresh)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    output = img.copy()

    for c in cnts:
        cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
        cv2.imshow("Contours", output)
        cv2.waitKey(0)
    cv2.waitKey(0)

if __name__ == '__main__':
    picPath = 'tetris_blocks.png'
    fun(picPath)
