############ Start PyQt5.QtGui############
from PyQt5.QtGui import QIcon,QPixmap,QRegExpValidator
############ End PyQt5.QtGui############

############ Start PyQt5.QtWidgets ############

from PyQt5.QtWidgets import\
    QMenu,QAction,QMainWindow,\
    QDialog,\
    QLabel,QLineEdit,QMessageBox,\
    QTableWidgetItem,QButtonGroup,QFileDialog,\
    QPushButton,QApplication

############ End PyQt5.QtWidgets############

############ Start PyQt5.QtCore ############

from PyQt5.QtCore import QDateTime,QDate,pyqtSignal,pyqtSlot,QThread,Qt,QRegExp,QUrl

############ End PyQt5.QtCore############

############ Start PyQt5.QtWebEngineWidgets ############

from PyQt5.QtWebEngineWidgets import QWebEngineView

############ End PyQt5.QtCore############

import sys
import os
from ToolsGui import *

### For File Ui
# from PyQt5.uic import loadUiType
# FORE_CLASS1,_ = loadUiType(os.path.join(os.path.dirname(__file__),"gui/ui/customre.ui"))
# FORE_CLASS2, _ = loadUiType( os.path.join( os.path.dirname( __file__ ), "gui/ui/dialogDomain.ui" ) )
# FORE_CLASS3, _ = loadUiType( os.path.join( os.path.dirname( __file__ ), "gui/ui/Clients.ui" ) )
# FORE_CLASS4, _ = loadUiType( os.path.join( os.path.dirname( __file__ ), "gui/ui/Login_Setup.ui" ) )
# FORE_CLASS5, _ = loadUiType( os.path.join( os.path.dirname( __file__ ), "gui/ui/info.ui" ) )

### For File py
from gui.customre import Ui_MainWindow_customre             #number 1
from gui.dialogDomain import Ui_Dialog_AddServices          #number 2
from gui.Clients import Ui_Dialog_AddClients                #number 3
from gui.Login_Setup import Ui_MainWindow_Setup             #number 4
from gui.info import Ui_Dialog_info                         #number 5

class Main(QMainWindow,QMessageBox,Ui_MainWindow_customre):   #FORE_CLASS1          number 1
    def __init__(self,parent= None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        ##Start hide lineEdite
        self.customer_lineEdit_14.hide()        #lineEdite Id Client
        ##End hide lineEdite
        ##Setting TabelWidget Text Name Colums
        ListItem  = ['id','نوع الخدمة','الموقع' , 'تاريخ البداية','تاريخ النهاية' , 'البيانات' , 'سعر التكلفة' , 'سعر البيع','العميل']
        for Cloums in range(len(ListItem)):
            item = self.customer_tableWidget.horizontalHeaderItem(Cloums)
            if Cloums == 0:
                self.customer_tableWidget.setColumnWidth(Cloums,4)    #cloumn id width
            item.setText(str(ListItem[Cloums]))

        ##End  Text Name Colums

class dialogDomain(QDialog,Ui_Dialog_AddServices):       #FORE_CLASS2       number 2
    def __init__(self, parent=None):
        QDialog.__init__( self, parent )
        self.setupUi( self )
        ##Start hide lineEdite
        self.Domain_lineEdit.hide()  # id service
        self.Domain_lineEdit_7.hide() # id user
        self.Domain_lineEdit_9.hide()  # name service
        ##End hide lineEdite

        ## defult LineEdite Cost price and selling
        self.Domain_lineEdit_23.setText( '0.000' )
        self.Domain_lineEdit_24.setText( '0.000' )

        ##Start Set DateTime Now
        self.Domain_dateEdit_4.setDate( QDate.currentDate() )
        self.Domain_dateEdit_5.setDate( QDate.currentDate() )
        ##End Set DateTime Now

        ##Start Regx
        self.Tools = ToolsLogin()
        listLinecurreancy = [self.Domain_lineEdit_23, self.Domain_lineEdit_24]
        self.Tools.F_Line_curreancy( listLinecurreancy )
        listLineDomain = [self.Domain_lineEdit_2]
        self.Tools.F_Line_Domain( listLineDomain )
        ##End Regx

class dialogClients(QDialog,Ui_Dialog_AddClients):          #FORE_CLASS3        number 3
    def __init__(self, parent=None):
        QDialog.__init__( self, parent )
        self.setupUi( self )

        ##Start Set DateTime Now
        self.customer_dateEdit.setDate( QDate.currentDate() )

        ##End Set DateTime Now

        ##Start regex
        self.Tools = ToolsLogin()
        UserName = [self.customer_lineEdit_3]
        self.Tools.F_Line_RegisterNick( UserName )
        listPhone = [self.customer_lineEdit_4]
        self.Tools.F_Line_Phone( listPhone )
        listEmail = [self.customer_lineEdit_5]
        self.Tools.F_Line_Email( listEmail )
        listCountry = [self.customer_lineEdit_6]
        self.Tools.F_Line_Country( listCountry )
        ##End regex

        ##Start After Add New client clear all lineEdite
        self.customer_lineEdit_3.clear()
        self.customer_lineEdit_4.clear()
        self.customer_lineEdit_5.clear()
        self.customer_lineEdit_6.clear()
        self.customer_textEdit.clear()
        ##End After Add New client clear all lineEdite

class Login_Setup(QMainWindow,QMessageBox,Ui_MainWindow_Setup):         #FORE_CLASS4        number 4
    def __init__(self,parent= None):
        super(Login_Setup,self).__init__(parent)
        QMainWindow.__init__(self, parent)
        self.setupUi(self)


class MSGINFO(QDialog,Ui_Dialog_info,QWebEngineView):                   #FORE_CLASS5        number 5
    def __init__(self, parent=None):
        QDialog.__init__( self, parent )
        self.setupUi( self )
        self.setWindowTitle( 'معلومات عني' )
        self.setWindowIcon( QIcon( 'Icon/info_client.png' ) )
        self.buttonClose.clicked.connect(self.close)
        self.LineUp()
        self.frame1.setFixedHeight(100)
        self.LineDwon()
        self.frame2.setFixedHeight( 250 )

    def LineUp(self):
        self.pixmap = QPixmap('Icon/M3foOoS.png')
        self.AboutInofImagelabel.setPixmap(self.pixmap)

    def LineDwon(self):
        self.browser2 = QWebEngineView(self.frame2)
        self.browser2.setFixedWidth(750)
        self.browser2.setFixedHeight(300)
        # self.browser2.setHtml(sessions.Aboutinfo2)
        pathMSGFile = os.getcwd()
        url = QUrl.fromLocalFile(r"/Icon/MSG.html")
        self.browser2.load(url)




# # For Test And Check My proograms All GUI Deisgner
# if __name__ == '__main__':
#
#     app = QApplication( sys.argv )          # only object not run or show
#     Select = MSGINFO()
#     Select.show()
#     app.exec_()



