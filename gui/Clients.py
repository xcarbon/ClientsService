﻿# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clients.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_AddClients(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(447, 651)
        Dialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.customer_lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_lineEdit_3.sizePolicy().hasHeightForWidth())
        self.customer_lineEdit_3.setSizePolicy(sizePolicy)
        self.customer_lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.customer_lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.customer_lineEdit_3.setMaxLength(50)
        self.customer_lineEdit_3.setObjectName("customer_lineEdit_3")
        self.horizontalLayout.addWidget(self.customer_lineEdit_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.customer_lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_lineEdit_4.sizePolicy().hasHeightForWidth())
        self.customer_lineEdit_4.setSizePolicy(sizePolicy)
        self.customer_lineEdit_4.setMinimumSize(QtCore.QSize(0, 30))
        self.customer_lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.customer_lineEdit_4.setText("")
        self.customer_lineEdit_4.setMaxLength(50)
        self.customer_lineEdit_4.setObjectName("customer_lineEdit_4")
        self.horizontalLayout_2.addWidget(self.customer_lineEdit_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.customer_lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_lineEdit_5.sizePolicy().hasHeightForWidth())
        self.customer_lineEdit_5.setSizePolicy(sizePolicy)
        self.customer_lineEdit_5.setMinimumSize(QtCore.QSize(0, 30))
        self.customer_lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.customer_lineEdit_5.setMaxLength(50)
        self.customer_lineEdit_5.setObjectName("customer_lineEdit_5")
        self.horizontalLayout_3.addWidget(self.customer_lineEdit_5)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.customer_lineEdit_6 = QtWidgets.QLineEdit(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_lineEdit_6.sizePolicy().hasHeightForWidth())
        self.customer_lineEdit_6.setSizePolicy(sizePolicy)
        self.customer_lineEdit_6.setMinimumSize(QtCore.QSize(0, 30))
        self.customer_lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.customer_lineEdit_6.setMaxLength(50)
        self.customer_lineEdit_6.setObjectName("customer_lineEdit_6")
        self.horizontalLayout_4.addWidget(self.customer_lineEdit_6)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.customer_dateEdit = QtWidgets.QDateEdit(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_dateEdit.sizePolicy().hasHeightForWidth())
        self.customer_dateEdit.setSizePolicy(sizePolicy)
        self.customer_dateEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.customer_dateEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.customer_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.customer_dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 10, 1), QtCore.QTime(0, 0, 0)))
        self.customer_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.customer_dateEdit.setCalendarPopup(True)
        self.customer_dateEdit.setCurrentSectionIndex(0)
        self.customer_dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.customer_dateEdit.setObjectName("customer_dateEdit")
        self.horizontalLayout_5.addWidget(self.customer_dateEdit)
        self.verticalLayout.addWidget(self.frame_5)
        self.customer_textEdit = QtWidgets.QTextEdit(Dialog)
        self.customer_textEdit.setObjectName("customer_textEdit")
        self.verticalLayout.addWidget(self.customer_textEdit)
        self.customer_pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.customer_pushButton_5.setObjectName("customer_pushButton_5")
        self.verticalLayout.addWidget(self.customer_pushButton_5)
        self.customer_pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.customer_pushButton_4.setObjectName("customer_pushButton_4")
        self.verticalLayout.addWidget(self.customer_pushButton_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "الاسم"))
        self.customer_lineEdit_3.setPlaceholderText(_translate("Dialog", "اسم العميل"))
        self.label_2.setText(_translate("Dialog", "الهاتف"))
        self.customer_lineEdit_4.setPlaceholderText(_translate("Dialog", "الهاتف             هذا الحقل يستم تشفيرة لحفظ السرية"))
        self.label_3.setText(_translate("Dialog", "الايميل"))
        self.customer_lineEdit_5.setPlaceholderText(_translate("Dialog", "الاميل             هذا الحقل يستم تشفيرة لحفظ السرية"))
        self.label_4.setText(_translate("Dialog", "البلد"))
        self.customer_lineEdit_6.setPlaceholderText(_translate("Dialog", "البلد"))
        self.label_7.setText(_translate("Dialog", "بداية الخدمة"))
        self.customer_dateEdit.setDisplayFormat(_translate("Dialog", "dd-MM-yyyy"))
        self.customer_textEdit.setPlaceholderText(_translate("Dialog", "البيانات |  هذا الحقل يستم تشفيرة لحفظ السرية"))
        self.customer_pushButton_5.setText(_translate("Dialog", "إضافة"))
        self.customer_pushButton_4.setText(_translate("Dialog", "حفظ"))

