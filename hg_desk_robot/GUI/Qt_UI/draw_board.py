# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'draw_board.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Draw_Board(object):
    def setupUi(self, Draw_Board):
        Draw_Board.setObjectName("Draw_Board")
        Draw_Board.resize(869, 615)
        # Draw_Board.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # Draw_Board.setFrameShadow(QtWidgets.QFrame.Raised)
        self.layoutWidget = QtWidgets.QWidget(Draw_Board)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 832, 76))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(19)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(120, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(120, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(120, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(120, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(120, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.layoutWidget1 = QtWidgets.QWidget(Draw_Board)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 200, 194, 170))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setMinimumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_2.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_3.setMinimumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.layoutWidget2 = QtWidgets.QWidget(Draw_Board)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 100, 277, 72))
        self.layoutWidget2.setToolTipDuration(-1)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(35)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(120, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_8.setMinimumSize(QtCore.QSize(120, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_8.setToolTipDuration(-1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.label_4 = QtWidgets.QLabel(Draw_Board)
        self.label_4.setGeometry(QtCore.QRect(350, 100, 500, 500))
        self.label_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(1)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Draw_Board)
        self.comboBox.currentIndexChanged.connect(Draw_Board.ListenComboBox)
        self.comboBox_2.currentIndexChanged.connect(Draw_Board.ListenComboBox)
        self.comboBox_3.currentIndexChanged.connect(Draw_Board.ListenComboBox)
        self.pushButton.clicked.connect(Draw_Board.StartDraw)
        self.pushButton_2.clicked.connect(Draw_Board.ClearBoard)
        self.pushButton_3.clicked.connect(Draw_Board.CancelPreviousStep)
        self.pushButton_4.clicked.connect(Draw_Board.Finish)
        self.pushButton_5.clicked.connect(Draw_Board.Exit)
        self.pushButton_6.clicked.connect(Draw_Board.Save)
        self.pushButton_7.clicked.connect(Draw_Board.UsePen)
        self.pushButton_8.clicked.connect(Draw_Board.UseEraser)
        QtCore.QMetaObject.connectSlotsByName(Draw_Board)

    def retranslateUi(self, Draw_Board):
        _translate = QtCore.QCoreApplication.translate
        Draw_Board.setWindowTitle(_translate("Draw_Board", "画板"))

        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.NoFocus)

        self.pushButton.setText(_translate("Draw_Board", "开始绘画"))
        self.pushButton_3.setText(_translate("Draw_Board", "撤销上一步"))
        self.pushButton_2.setText(_translate("Draw_Board", "清空画布"))
        self.pushButton_4.setText(_translate("Draw_Board", "结束绘画"))
        self.pushButton_6.setText(_translate("Draw_Board", "保存画作"))
        self.pushButton_5.setText(_translate("Draw_Board", "退出画板"))
        self.label.setText(_translate("Draw_Board", "   线条风格"))
        self.comboBox.setCurrentText(_translate("Draw_Board", "实线"))
        self.comboBox.setItemText(0, _translate("Draw_Board", "实线"))
        self.comboBox.setItemText(1, _translate("Draw_Board", "虚线"))
        self.comboBox.setItemText(2, _translate("Draw_Board", "点"))
        self.label_2.setText(_translate("Draw_Board", "   线条粗细"))
        self.comboBox_2.setItemText(0, _translate("Draw_Board", "细"))
        self.comboBox_2.setItemText(1, _translate("Draw_Board", "中"))
        self.comboBox_2.setItemText(2, _translate("Draw_Board", "粗"))
        self.label_3.setText(_translate("Draw_Board", "   橡皮大小"))
        self.comboBox_3.setItemText(0, _translate("Draw_Board", "小"))
        self.comboBox_3.setItemText(1, _translate("Draw_Board", "中"))
        self.comboBox_3.setItemText(2, _translate("Draw_Board", "大"))
        self.pushButton_7.setText(_translate("Draw_Board", "使用画笔"))
        self.pushButton_8.setText(_translate("Draw_Board", "使用橡皮"))
        self.label_4.setText(_translate("Draw_Board", "Image_View"))

