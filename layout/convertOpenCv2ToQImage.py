import sys
import cv2 as cv
import matplotlib.pyplot as plt
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

def convert_nparray_to_QPixmap(img):
    w,h,ch = img.shape
    # Convert resulting image to pixmap
    if img.ndim == 1:
        img =  cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

    qimg = QImage(img.data, h, w, 3*h, QImage.Format_RGB888)
    qpixmap = QPixmap(qimg)

    return qpixmap

def dao_anh(img):
    return 255-img

def imageOpenCv2ToQImage (cv_img):
    height, width, bytesPerComponent = cv_img.shape
    bytesPerLine = bytesPerComponent * width;
    cv.cvtColor(cv_img, cv.COLOR_RGB2GRAY, cv_img)
    return QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
if __name__ == '__main__':
    img = cv.imread('E:\icon\sanbay.tif')
    grayimage = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img3 = dao_anh(img)
    show_image = imageOpenCv2ToQImage(img3)


    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setPixmap(QtGui.QPixmap.fromImage(show_image))

    widget.setGeometry(50, 50, 320, 200)
    widget.setWindowTitle("PyQt5 Example")
    widget.show()
    sys.exit(app.exec_())
