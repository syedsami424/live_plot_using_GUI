# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\iqras\AppData\Local\Programs\Python\Python311\Lib\site-packages\QtDesigner\singlegraph.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib.animation as animation
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import pandas as pd

c=0
x_list=[]
y1_list=[]
y2_list=[]
y3_list=[]
y4_list=[]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("QFrame{\n"
"    background-color: rgb(0,200,96);\n"
"    border: none;\n"
"    padding: 5px;\n"
"    color: rgb(205,230,255);\n"
"    border-radius: 5px;\n"
"    font: 75 14pt \"Candara\";\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        #############################################
        #ADDING CANVAS:-
        self.horizontalLayout_4=QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        #CANVAS CODE:-
        self.figure=plt.figure()
        self.canvas=FigureCanvas(self.figure)
        self.horizontalLayout_4.addWidget(self.canvas)
        #############################################
        #self.ax=self.figure.add_subplot(1,1,1)
        #self.ani_func()
        self.paused=False
        self.ani=None
        #############################################

        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.plotOnCanvas())
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0,200,96);\n"
"    border: none;\n"
"    padding: 5px;\n"
"    color: rgb(205,230,255);\n"
"    border-radius: 5px;\n"
"    font: 75 14pt \"Candara\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0,240,115);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0,200,96);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2_pause = QtWidgets.QPushButton(self.frame_4, clicked=lambda: self.pause_animation())
        self.pushButton_2_pause.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0,200,96);\n"
"    border: none;\n"
"    padding: 5px;\n"
"    color: rgb(205,230,255);\n"
"    border-radius: 5px;\n"
"    font: 75 14pt \"Candara\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0,240,115);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0,200,96);\n"
"}")
        self.pushButton_2_pause.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2_pause)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Plot Display"))
        self.pushButton.setText(_translate("MainWindow", "click here to start plot"))
        self.pushButton_2_pause.setText(_translate("MainWindow", "click here to stop plot"))

    def ani_func(self, i):  #animate function
        global c
        data=pd.read_csv("flightSimulatorResults.csv")
        if self.paused:
            return
        x=list(data['Time'])
        y1=list(data['Velocity'])
        y2=list(data['Acceleration'])
        y3=list(data['Altitude'])
        y4=list(data['Thrust'])
        x_list.append(x[c])
        y1_list.append(y1[c])
        y2_list.append(y2[c])
        y3_list.append(y3[c])
        y4_list.append(y4[c])
        c=c+1

        self.plt=self.figure.add_subplot(2,2,1)
        self.plt.clear()
        self.plt.plot(x_list,y1_list)
        plt.xlim(0,47)
        plt.ylim(0,57)

        self.plt=self.figure.add_subplot(2,2,2)
        self.plt.clear()
        self.plt.plot(x_list,y2_list)
        plt.xlim(0,47)
        plt.ylim(0,32)

        self.plt=self.figure.add_subplot(2,2,3)
        self.plt.clear()
        self.plt.plot(x_list,y3_list)
        plt.xlim(0,47)
        plt.ylim(0,145)

        self.plt=self.figure.add_subplot(2,2,4)
        self.plt.clear()
        self.plt.plot(x_list,y4_list)
        plt.xlim(0,47)
        plt.ylim(0,15)

    def plotOnCanvas(self):  #plot function
        self.ani=animation.FuncAnimation(self.figure, self.ani_func, 100**100)
        #self.paused= False
        self.canvas.draw()
        #self.ani_func.start()
        print("Started")

        self.paused=False
        if self.ani is not None:
            self.ani.event_source.start()
        self.canvas.draw()



    def clearplotOnCanvas(self):
        if self.ani is not None:
            self.ani_func.event_source.stop()

        self.ax.clear()
        self.canvas.draw()

    def pause_animation(self): #pushButton_2_pause
        self.paused=True
        print("Paused")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
