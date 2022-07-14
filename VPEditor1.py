import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1819, 112)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 50, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 0, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(55, 255, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 50, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(160, 0, 341, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 50, 341, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_20 = QtWidgets.QPushButton(Dialog)
        self.pushButton_20.setGeometry(QtCore.QRect(660, 0, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("background-color: rgb(131, 75, 166);")
        self.pushButton_20.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(820, 0, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(820, 50, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(920, 0, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(920, 50, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(1020, 0, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Dialog)
        self.pushButton_11.setGeometry(QtCore.QRect(1020, 50, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(660, 50, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(1120, 0, 221, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(1120, 50, 221, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(1340, 0, 221, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(1340, 50, 221, 51))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(1560, 0, 221, 51))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(1560, 50, 221, 51))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

# Funktionsdeklaration
        self.function1()
        self.function2()
        self.function3()
        self.function4()
        self.function5()
        self.function6()
        self.function7()
        self.function8()
        self.function9()
        self.function10()
        self.function11()
        self.function12()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Picture"))
        self.pushButton_2.setText(_translate("Dialog", "Video"))
        self.pushButton_3.setText(_translate("Dialog", "Camera"))
        self.pushButton_4.setText(_translate("Dialog", "StopCamera"))
        self.pushButton_20.setText(_translate("Dialog", "CustomColor"))
        self.pushButton_6.setText(_translate("Dialog", "0"))
        self.pushButton_7.setText(_translate("Dialog", "1"))
        self.pushButton_8.setText(_translate("Dialog", "2"))
        self.pushButton_9.setText(_translate("Dialog", "3"))
        self.pushButton_10.setText(_translate("Dialog", "4"))
        self.pushButton_11.setText(_translate("Dialog", "5"))
        self.pushButton_12.setText(_translate("Dialog", "ClearColor"))

# Variable
    hsvColor = [[0] * 2 for i in range(6)]
    counterColor = 0
    colorBar = [0] * 6
    colorButton = [[0] * 6 for i in range(6)]
    stopRun = 0
    middleColours = [[0] * 3 for i in range(6)]
    cap = cv2.VideoCapture(0)

# Aktion von Funktionen
    def chooseColor(self):
        self.counterColor = 1
        def nothing(self):
            pass
        cv2.namedWindow("settings", cv2.WINDOW_NORMAL)
        cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
        cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
        cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
        cv2.createTrackbar('h2', 'settings', 0, 255, nothing)
        cv2.createTrackbar('s2', 'settings', 0, 255, nothing)
        cv2.createTrackbar('v2', 'settings', 0, 255, nothing)
        crange = [0, 0, 0, 0, 0, 0]
        kernel = np.ones((5, 5), np.uint8)
        img1 = cv2.resize(cv2.imread('colors.jpg'), (1200, 500))
        while True:
            h1 = cv2.getTrackbarPos('h1', 'settings')
            s1 = cv2.getTrackbarPos('s1', 'settings')
            v1 = cv2.getTrackbarPos('v1', 'settings')
            h2 = cv2.getTrackbarPos('h2', 'settings')
            s2 = cv2.getTrackbarPos('s2', 'settings')
            v2 = cv2.getTrackbarPos('v2', 'settings')
            thresh = cv2.dilate(cv2.inRange(img1, (h1, s1, v1), (h2, s2, v2)), kernel, iterations=2)
            thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
            dst = cv2.addWeighted(img1, 1, thresh, 1, 0.0)
            cv2.imshow('img', dst)
            ch = cv2.waitKey(30)
            if ch == 49:
                break
        cv2.destroyAllWindows()

    def stopCamera(self):
        self.stopRun = 1
        self.cap.release()
        cv2.destroyAllWindows()

    def drawCountors(self, thresh, kernel, img, hsv):
            for i in range(6):
                thresh[i] = cv2.inRange(hsv, self.hsvColor[i][0], self.hsvColor[i][1])
                thresh[i] = cv2.dilate(thresh[i], kernel, iterations=2)
                contours, hierarhy = cv2.findContours(thresh[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                for contour in contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    if w > 20 and h > 20:
                        centrex = x + w / 2
                        centrey = y + h / 2
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        r = w / 2
                        cv2.putText(img,   str(x) + " " + str(y) + " " + str(r) , (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (self.middleColours[i][0], self.middleColours[i][1], self.middleColours[i][2]), 2)
                img = cv2.drawContours(img, contours, -1, (self.middleColours[i][0], self.middleColours[i][1], self.middleColours[i][2]), 4, cv2.LINE_AA, hierarhy, 1)
            cv2.imshow('img', img)
            dst = thresh[5]
            for i in range(5):
                dst = cv2.addWeighted(dst, 1, thresh[i], 1, 0.0)
            cv2.imshow('result', dst)

    def cameraColor(self):
        # if self.counterColor == 0:
        #     self.maxColorOnScreen(self, img)
        thresh = [0] * 6
        kernel = np.ones((5, 5), np.uint8)
        while True:
            flag, img = self.cap.read()
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            self.drawCountors(thresh, kernel, img, hsv)
            ch = cv2.waitKey(30)
            if self.stopRun == 1:
                break

    def videoColor(self, path4Video):
        thresh = [0] * 6
        kernel = np.ones((5, 5), np.uint8)
        vid_capture = cv2.VideoCapture(path4Video)
        while True:
            ret, img = vid_capture.read()
            img = cv2.resize(img, (1000, 450))
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            self.drawCountors(thresh, kernel, img, hsv)
            ch = cv2.waitKey(30)
            if self.stopRun == 1:
                break

    def pictureColor(self, path4Picture):
        thresh = [0] * 6
        kernel = np.ones((5, 5), np.uint8)
        img = cv2.resize(cv2.imread(path4Picture), (1000, 450))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        for i in range(6):
            thresh[i] = cv2.inRange(hsv, self.hsvColor[i][0], self.hsvColor[i][1])
            thresh[i] = cv2.dilate(thresh[i], kernel, iterations=2)
            contours, hierarhy = cv2.findContours(thresh[i], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            img = cv2.drawContours(img, contours, -1, (self.middleColours[i][0], self.middleColours[i][1], self.middleColours[i][2]), 2)
        cv2.imshow('img', img)
        dst = thresh[5]
        for i in range(5):
            dst = cv2.addWeighted(dst, 1, thresh[i], 1, 0.0)
        cv2.imshow('result', dst)
        ch = cv2.waitKey(30)

    def clearColor(self):
        self.counterColor = 0
        for i in range(6):
            self.colorBar[i] = 0
            for j in range(6):
                self.colorButton[i][j] = 0
        for i in range(6):
            for j in range(2):
                self.hsvColor[i][j] = 0
        self.textBrowser.setText(str(self.colorButton[0]))
        self.textBrowser_2.setText(str(self.colorButton[1]))
        self.textBrowser_3.setText(str(self.colorButton[2]))
        self.textBrowser_4.setText(str(self.colorButton[3]))
        self.textBrowser_5.setText(str(self.colorButton[4]))
        self.textBrowser_6.setText(str(self.colorButton[5]))

    def setColor(self, number):
        a = int(number)
        if self.counterColor == 1:
            self.colorBar[0] = cv2.getTrackbarPos('h1', 'settings')
            self.colorBar[1] = cv2.getTrackbarPos('s1', 'settings')
            self.colorBar[2] = cv2.getTrackbarPos('v1', 'settings')
            self.colorBar[3] = cv2.getTrackbarPos('h2', 'settings')
            self.colorBar[4] = cv2.getTrackbarPos('s2', 'settings')
            self.colorBar[5] = cv2.getTrackbarPos('v2', 'settings')
        for i in range(6):
            self.colorButton[a][i] = self.colorBar[i]
        for j in range(3):
            self.middleColours[a][j] = ((self.colorBar[j] + self.colorBar[j+3])/2)
        self.hsvColor[a][0] = np.array((self.colorButton[a][0], self.colorButton[a][1], self.colorButton[a][2]), np.uint8)
        self.hsvColor[a][1] = np.array((self.colorButton[a][3], self.colorButton[a][4], self.colorButton[a][5]), np.uint8)
        if a == 0:
            self.textBrowser.setText(str(self.colorButton[a]))
        elif a == 1:
            self.textBrowser_2.setText(str(self.colorButton[a]))
        elif a == 2:
            self.textBrowser_3.setText(str(self.colorButton[a]))
        elif a == 3:
            self.textBrowser_4.setText(str(self.colorButton[a]))
        elif a == 4:
            self.textBrowser_5.setText(str(self.colorButton[a]))
        elif a == 5:
            self.textBrowser_6.setText(str(self.colorButton[a]))

    def maxColorOnScreen(self, img):
        pass

# Aktionen der Schnittstelleca
    def function1(self):
        self.pushButton.clicked.connect(lambda: self.pictureColor(self.textEdit.toPlainText()))

    def function2(self):
        self.pushButton_2.clicked.connect(lambda: self.videoColor(self.textEdit_2.toPlainText()))

    def function3(self):
        self.pushButton_3.clicked.connect(self.cameraColor)

    def function4(self):
        self.pushButton_4.clicked.connect(self.stopCamera)

    def function5(self):
        self.pushButton_20.clicked.connect(self.chooseColor)

    def function6(self):
        self.pushButton_6.clicked.connect(lambda: self.setColor(self.pushButton_6.text()))

    def function7(self):
        self.pushButton_7.clicked.connect(lambda: self.setColor(self.pushButton_7.text()))

    def function8(self):
        self.pushButton_8.clicked.connect(lambda: self.setColor(self.pushButton_8.text()))

    def function9(self):
        self.pushButton_9.clicked.connect(lambda: self.setColor(self.pushButton_9.text()))

    def function10(self):
        self.pushButton_10.clicked.connect(lambda: self.setColor(self.pushButton_10.text()))

    def function11(self):
        self.pushButton_11.clicked.connect(lambda: self.setColor(self.pushButton_11.text()))

    def function12(self):
        self.pushButton_12.clicked.connect(self.clearColor)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
