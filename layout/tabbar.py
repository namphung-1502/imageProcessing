import sys

import cv2 as cv
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class tabar_option(QWidget):
    def __init__(self, parent):
        super(tabar_option, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        #init tab screen
        self.tabs = QTabWidget()
        self.tabs.tabBar().setDocumentMode(True)
        self.tabs.setObjectName("tabbar")
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tabs.resize(300,300)

        # add tab
        self.tabs.addTab(self.tab1, "General")
        self.tabs.addTab(self.tab2, "Smooth")
        self.tabs.addTab(self.tab3, "General")
        self.tabs.addTab(self.tab4, "Smooth")
        self.tabs.addTab(self.tab5, "General")
        self.tabs.addTab(self.tab6, "Smooth")

        #set icon for tab
        self.tabs.setTabIcon(0, QtGui.QIcon("image/openfile.png"))

        # first tab
        self.tab1.layout = QVBoxLayout(self)
        self.l1 = QLabel()
        self.l1.setText("This is first tab")
        self.btn_birnary = QPushButton("Binary Image")
        # self.btn_birnary.clicked.connect(self.binary_image)
        self.tab1.layout.addWidget(self.btn_birnary)
        self.tab1.layout.addWidget(self.l1)
        self.tab1.setLayout(self.tab1.layout)

        # add tab to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        sshFile = "qss/tabar.qss"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())
    # def binary_image(self):
    #     # get path image
    #     img = cv.imread(main_layout.path_file(self))
    #     reverse_image = handle_image.resverse_image(img)
    #     show_image = handle_image.imageOpenCv2ToQImage(reverse_image)
    #     main_layout.image_process(main_layout(), show_image)

# class handle_image():
#     def imageOpenCv2ToQImage (cv_img):
#         height, width, bytesPerComponent = cv_img.shape
#         bytesPerLine = bytesPerComponent * width;
#         cv.cvtColor(cv_img, cv.COLOR_RGB2GRAY, cv_img)
#         return QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
#     def resverse_image(img):
#         return 255-img



