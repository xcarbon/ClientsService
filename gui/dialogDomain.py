﻿# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogDomain.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_AddServices(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(771, 1048)
        Dialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 747, 1024))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Domain_lineEdit = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Domain_lineEdit.sizePolicy().hasHeightForWidth())
        self.Domain_lineEdit.setSizePolicy(sizePolicy)
        self.Domain_lineEdit.setReadOnly(True)
        self.Domain_lineEdit.setObjectName("Domain_lineEdit")
        self.verticalLayout_5.addWidget(self.Domain_lineEdit)
        self.Domain_lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Domain_lineEdit_7.sizePolicy().hasHeightForWidth())
        self.Domain_lineEdit_7.setSizePolicy(sizePolicy)
        self.Domain_lineEdit_7.setReadOnly(True)
        self.Domain_lineEdit_7.setObjectName("Domain_lineEdit_7")
        self.verticalLayout_5.addWidget(self.Domain_lineEdit_7)
        self.Domain_lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Domain_lineEdit_8.sizePolicy().hasHeightForWidth())
        self.Domain_lineEdit_8.setSizePolicy(sizePolicy)
        self.Domain_lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.Domain_lineEdit_8.setReadOnly(True)
        self.Domain_lineEdit_8.setObjectName("Domain_lineEdit_8")
        self.verticalLayout_5.addWidget(self.Domain_lineEdit_8)
        self.Domain_lineEdit_9 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Domain_lineEdit_9.sizePolicy().hasHeightForWidth())
        self.Domain_lineEdit_9.setSizePolicy(sizePolicy)
        self.Domain_lineEdit_9.setReadOnly(True)
        self.Domain_lineEdit_9.setObjectName("Domain_lineEdit_9")
        self.verticalLayout_5.addWidget(self.Domain_lineEdit_9)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.customer_comboBox = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customer_comboBox.sizePolicy().hasHeightForWidth())
        self.customer_comboBox.setSizePolicy(sizePolicy)
        self.customer_comboBox.setObjectName("customer_comboBox")
        self.customer_comboBox.addItem("")
        self.customer_comboBox.addItem("")
        self.customer_comboBox.addItem("")
        self.customer_comboBox.addItem("")
        self.customer_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.customer_comboBox)
        self.verticalLayout_5.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Domain_lineEdit_2 = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Domain_lineEdit_2.sizePolicy().hasHeightForWidth())
        self.Domain_lineEdit_2.setSizePolicy(sizePolicy)
        self.Domain_lineEdit_2.setMaxLength(50)
        self.Domain_lineEdit_2.setObjectName("Domain_lineEdit_2")
        self.horizontalLayout.addWidget(self.Domain_lineEdit_2)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.Domain_dateEdit_4 = QtWidgets.QDateEdit(self.frame_8)
        self.Domain_dateEdit_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Domain_dateEdit_4.setWrapping(False)
        self.Domain_dateEdit_4.setFrame(True)
        self.Domain_dateEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Domain_dateEdit_4.setKeyboardTracking(True)
        self.Domain_dateEdit_4.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 10, 1), QtCore.QTime(0, 0, 0)))
        self.Domain_dateEdit_4.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.Domain_dateEdit_4.setCalendarPopup(True)
        self.Domain_dateEdit_4.setObjectName("Domain_dateEdit_4")
        self.verticalLayout_8.addWidget(self.Domain_dateEdit_4)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.frame_9)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.Domain_dateEdit_5 = QtWidgets.QDateEdit(self.frame_9)
        self.Domain_dateEdit_5.setFrame(True)
        self.Domain_dateEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.Domain_dateEdit_5.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.Domain_dateEdit_5.setAccelerated(False)
        self.Domain_dateEdit_5.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.Domain_dateEdit_5.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 10, 1), QtCore.QTime(0, 0, 0)))
        self.Domain_dateEdit_5.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.Domain_dateEdit_5.setCalendarPopup(True)
        self.Domain_dateEdit_5.setObjectName("Domain_dateEdit_5")
        self.verticalLayout_9.addWidget(self.Domain_dateEdit_5)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.verticalLayout_6.addWidget(self.frame_7)
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.line_2 = QtWidgets.QFrame(self.frame_10)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_32.addWidget(self.line_2)
        self.verticalLayout_6.addWidget(self.frame_10)
        self.Domain_textEdit = QtWidgets.QTextEdit(self.frame_5)
        self.Domain_textEdit.setDocumentTitle("")
        self.Domain_textEdit.setOverwriteMode(False)
        self.Domain_textEdit.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.Domain_textEdit.setObjectName("Domain_textEdit")
        self.verticalLayout_6.addWidget(self.Domain_textEdit)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.frame_49 = QtWidgets.QFrame(self.frame)
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_49)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.line_3 = QtWidgets.QFrame(self.frame_49)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_34.addWidget(self.line_3)
        self.verticalLayout_5.addWidget(self.frame_49)
        self.frame_50 = QtWidgets.QFrame(self.frame)
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_50)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_3 = QtWidgets.QLabel(self.frame_50)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_24.addWidget(self.label_3)
        self.Domain_lineEdit_23 = QtWidgets.QLineEdit(self.frame_50)
        self.Domain_lineEdit_23.setObjectName("Domain_lineEdit_23")
        self.horizontalLayout_24.addWidget(self.Domain_lineEdit_23)
        self.label_4 = QtWidgets.QLabel(self.frame_50)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_24.addWidget(self.label_4)
        self.Domain_lineEdit_24 = QtWidgets.QLineEdit(self.frame_50)
        self.Domain_lineEdit_24.setObjectName("Domain_lineEdit_24")
        self.horizontalLayout_24.addWidget(self.Domain_lineEdit_24)
        self.verticalLayout_5.addWidget(self.frame_50)
        self.Domain_pushButton = QtWidgets.QPushButton(self.frame)
        self.Domain_pushButton.setObjectName("Domain_pushButton")
        self.verticalLayout_5.addWidget(self.Domain_pushButton)
        self.Domain_pushButton_Edite = QtWidgets.QPushButton(self.frame)
        self.Domain_pushButton_Edite.setObjectName("Domain_pushButton_Edite")
        self.verticalLayout_5.addWidget(self.Domain_pushButton_Edite)
        self.verticalLayout_3.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Domain_lineEdit.setPlaceholderText(_translate("Dialog", "id service"))
        self.Domain_lineEdit_7.setPlaceholderText(_translate("Dialog", "id user"))
        self.Domain_lineEdit_8.setPlaceholderText(_translate("Dialog", "name user"))
        self.Domain_lineEdit_9.setPlaceholderText(_translate("Dialog", "name service"))
        self.label_5.setText(_translate("Dialog", "نوع الخدمة"))
        self.customer_comboBox.setItemText(0, _translate("Dialog", "Domain"))
        self.customer_comboBox.setItemText(1, _translate("Dialog", "WebHosting"))
        self.customer_comboBox.setItemText(2, _translate("Dialog", "mobaileApps"))
        self.customer_comboBox.setItemText(3, _translate("Dialog", "WebApps"))
        self.customer_comboBox.setItemText(4, _translate("Dialog", "DesktopApps"))
        self.Domain_lineEdit_2.setPlaceholderText(_translate("Dialog", "اسم الموقع"))
        self.label.setText(_translate("Dialog", "بداية التاريخ"))
        self.Domain_dateEdit_4.setToolTip(_translate("Dialog", "start date"))
        self.Domain_dateEdit_4.setDisplayFormat(_translate("Dialog", "dd-MM-yyyy"))
        self.label_2.setText(_translate("Dialog", "نهاية التاريخ"))
        self.Domain_dateEdit_5.setToolTip(_translate("Dialog", "end date"))
        self.Domain_dateEdit_5.setDisplayFormat(_translate("Dialog", "dd-MM-yyyy"))
        self.Domain_textEdit.setPlaceholderText(_translate("Dialog", "البيانات | هذا الحقل يستم تشفيرة لحفظ السرية"))
        self.label_3.setText(_translate("Dialog", " التكلفة"))
        self.Domain_lineEdit_23.setPlaceholderText(_translate("Dialog", "سعر التكلفة"))
        self.label_4.setText(_translate("Dialog", "البيع"))
        self.Domain_lineEdit_24.setPlaceholderText(_translate("Dialog", "سعر البيع"))
        self.Domain_pushButton.setText(_translate("Dialog", "إضافة"))
        self.Domain_pushButton_Edite.setText(_translate("Dialog", "حفظ"))

