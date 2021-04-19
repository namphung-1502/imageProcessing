import sys
import cv2 as cv
import matplotlib.pyplot as mlt
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from tabbar import tabar_option


class main_layout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Processing")
        self.resize(860, 680)
        self.setWindowIcon(QtGui.QIcon("image/python_icon.png"))
        self.layout = QVBoxLayout()
        self.top_frame = QFrame(self)
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setObjectName("frame1")

        # button open file
        self.btn_openfile = QPushButton("Open file")
        self.btn_openfile.setIcon(QIcon("image/openfile.png"))
        self.btn_openfile.setObjectName("btn_openfile")
        self.btn_openfile.clicked.connect(self.openfile)

        # save image
        self.btn_saveimage = QPushButton("Save image")
        self.btn_saveimage.setIcon(QIcon("image/savefile.png"))
        self.btn_saveimage.setObjectName("btn_saveimage")

        # add widget to top frame
        self.top_frame.layout =QHBoxLayout()
        self.top_frame.layout.addWidget(self.btn_openfile)
        self.top_frame.layout.addWidget(self.btn_saveimage)
        self.top_frame.setLayout(self.top_frame.layout)

        # create main frame to show image
        self.main_frame = QFrame(self)
        self.main_frame.setContentsMargins(0,0,0,0)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setObjectName("frame2")

        # Label to show original image
        self.ori_image = QLabel()
        self.ori_image.setText("Original Image")
        self.ori_image.setAlignment(Qt.AlignCenter)
        self.ori_image.setObjectName("ori_image")

        # Label to show handle image
        self.process_image = QLabel()
        self.process_image.setText("Process Image")
        self.process_image.setAlignment(Qt.AlignCenter)
        self.process_image.setObjectName("process_image")


        self.main_frame.layout = QHBoxLayout()
        self.main_frame.layout.addWidget(self.ori_image)
        self.main_frame.layout.addWidget(self.process_image)
        self.main_frame.setLayout(self.main_frame.layout)

        self.option_frame = QFrame(self)
        self.option_frame.setFrameShape(QFrame.StyledPanel)
        self.option_frame.setObjectName("frame3")
        self.tab_option = tabar_option(self)
        self.tab_option.btn_birnary.clicked.connect(self.test_action)
        self.option_frame.layout = QHBoxLayout()
        self.option_frame.layout.addWidget(self.tab_option)
        self.option_frame.setLayout(self.option_frame.layout)

        self.layout.addWidget(self.top_frame)
        self.layout.addWidget(self.main_frame)
        self.layout.addWidget(self.option_frame)
        self.setLayout(self.layout)
        # add file qss
        sshFile = "qss/design.qss"
        with open(sshFile, "r") as fh:
            self.setStyleSheet(fh.read())

    def openfile(self):
        path_image = QFileDialog.getOpenFileName(self, "Image file")
        global path
        path = path_image[0]
        self.ori_image.setPixmap(QPixmap(path))
        # self.ori_image.setScaledContents(True)
        # self.label_2.setPixmap(QPixmap(path))
        self.pix = QPixmap.fromImage(path)
        self.ori_image.setPixmap(self.pix.scaled(self.process_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.process_image.setPixmap(self.pix.scaled(self.process_image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
    # return path file
    def path_file(self):
        if "path" in globals():
            return path
        else:
            return " ";
    # convert cv_image to QImage
    def imageOpenCv2ToQImage (cv_img):
        height, width, bytesPerComponent = cv_img.shape
        bytesPerLine = bytesPerComponent * width;
        cv.cvtColor(cv_img, cv.COLOR_RGB2GRAY, cv_img)
        return QtGui.QImage(cv_img.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
    # reverse image
    def resverse_image(img):
        return 255-img

    def test_action(self):
        # get path image
        img = cv.imread(self.path_file())
        print(self.path_file())
        reverse_image = self.resverse_image(img)
        show_image = self.imageOpenCv2ToQImage(reverse_image)
        self.image_process(self, show_image)

    def image_process(self, img):
        self.process_image.setPixmap(QtGui.QPixmap.fromImage(img))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main_layout()
    window.show()
    sys.exit(app.exec_())