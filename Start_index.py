from customre import *
from encrypted import *
from ConnactionDb import *
from ToolsGui import *
from MyThread import *


class StartClass(Main,Lang):
    def __init__(self,parent= None):
        super(StartClass,self).__init__(parent)
        self.setWindowTitle('Customer program V 1.0')
        self.setWindowIcon( QIcon('Icon\Program_icon.png'))
        self.setStyleSheet(sessions.CustomreCSS)
        self.label_nameAdmin.setText( sessions.UserNameAdmin )
        self.Tools = ToolsLogin()       # object class Tools Program
        self.Start_Onstartup()          # Opstions on Start Class Programs Clients
        self.ConnectedRightClick()      # methood RgihtClick
        self.MenuBarPrograms()          # Methood MenuBar Programs

        # set button context menu policy

    def MenuBarPrograms(self):
        ###### MeunBar SMD ########
        Index1 = self.menubar
        File = Index1.addMenu(self.SPadd)
        Help = Index1.addMenu(self.SPhelp)
        ####File
        NewClient_Action = QAction(self.DCaddClientsTitle,self)
        NewClient_Action.setShortcut('F1')
        File.addAction(NewClient_Action)
        NewClient_Action.triggered.connect(lambda :self.MenuBarSelecter('F1'))
        ####Help
        info_Action = QAction(self.SPAboutme,self)
        info_Action.setShortcut('F12')
        Help.addAction(info_Action)
        info_Action.triggered.connect(lambda :self.MenuBarSelecter('F12'))
        self.openWindoCount = 0
        ########
        exit_Action = QAction(self.SPExite,self)
        exit_Action.setShortcut('Esc')
        Help.addAction(exit_Action)
        exit_Action.triggered.connect(lambda :self.MenuBarSelecter('Esc'))

    def MenuBarSelecter(self,Cmd):
        if Cmd == 'F1':
            Proograms.Add_ClientsContral( self, 0 )
        elif Cmd == 'F12':
            if self.openWindoCount == 0:
                self.showMsg = MSGINFO(self)  # Object dialog about menuBar
                self.showMsg.show()
                self.openWindoCount +=1
                self.showMsg.exec_()
                self.openWindoCount = 0

        elif Cmd == 'Esc':
            self.close()

    def ConnectedRightClick(self):
        # Start RightClick in listwidgets
        self.customer_listWidget.setContextMenuPolicy( Qt.CustomContextMenu )
        self.customer_listWidget.customContextMenuRequested.connect( self.ListWidget_context_menu )
        # End RightClick in listwidgets

        # Start RightClick in TabelWidgets
        self.customer_tableWidget.setContextMenuPolicy( Qt.CustomContextMenu )
        self.customer_tableWidget.customContextMenuRequested.connect( self.TabelWidget_Widget_context_menu )
        # End RightClick in TabelWidgets


    def ListWidget_context_menu(self, point):
        # create context menu
        popMenu = QMenu()
        NewCleint = popMenu.addAction(QIcon( 'Icon/add_client.png' ),self.DCaddClientsTitle)
        popMenu.addSeparator()
        popMenu.addSeparator()
        InfoCleint = popMenu.addAction(QIcon( 'Icon/info_client.png' ),self.DCinfoClientTitle)
        popMenu.addSeparator()
        EditeCleint = popMenu.addAction(QIcon( 'Icon/edite_client.png' ),self.DcediteClientsTitle)
        popMenu.addSeparator()
        deleteCleint = popMenu.addAction(QIcon( 'Icon/delete_client.png' ),self.SPDelteClients)

        # show context menu
        action = popMenu.exec_( self.customer_listWidget.mapToGlobal( point ) )
        if action == NewCleint:
            Proograms.Add_ClientsContral(self,0)
        elif action == InfoCleint:
            Proograms.Add_ClientsContral(self,1)
        elif action == EditeCleint:
            Proograms.Add_ClientsContral(self,2)
        elif action == deleteCleint:
            Proograms.Add_ClientsContral(self,3)
        else:
            pass
        ########

    def TabelWidget_Widget_context_menu(self, point):
        RightClick = QMenu()
        R_AddService = RightClick.addAction(QIcon( 'Icon/add_service.png' ),self.DSaddservice)
        RightClick.addSeparator()
        R_open = RightClick.addAction(QIcon( 'Icon/info_client.png' ),self.DSinfoservice )
        RightClick.addSeparator()
        R_Edite = RightClick.addAction(QIcon( 'Icon/edite_service.png' ),self.DSediteservice )
        RightClick.addSeparator()
        R_Delete = RightClick.addAction(QIcon( 'Icon/delete_client.png' ),self.SPDelteService )

        action = RightClick.exec_( self.customer_tableWidget.mapToGlobal( point ) )
        if action == R_AddService:
            Alldialogs.GetRightClickCmd( self,'AddService')
        elif action == R_open:
            Alldialogs.GetRightClickCmd(self,'Open')
        elif action == R_Edite:
            Alldialogs.GetRightClickCmd(self,'Edite')
        elif action == R_Delete:
            Alldialogs.GetRightClickCmd(self,'delete')
        else:
            pass

    #################################################


    def Start_Onstartup(self):
        Proograms.Onstartup_customer(self)

    # Run All Thread In Proogram
    def ThreadAll(self,CmdThread):
        self.Thread = C_Worker(CmdThread)       #object
        ##Start Connect StatusBar Remove
        self.Thread.SginalStatusBar.connect(self.EventsAllThread)
        self.Thread.start()

    def EventsAllThread(self,Cmd):
        ## timer in Class C_Worker 3 Secound After Run
        if Cmd == 'RemoveStatusBar':
            self.statusbar.showMessage('')

from class_proogram import *


#####################################################
#Test And Check My proograms
# if __name__ == '__main__':
#
#     app = QApplication( sys.argv )          # only object not run or show
#     Select = StartClass()
#     Select.show()
#     app.exec_()

#####################################################