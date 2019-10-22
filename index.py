from Start_index import *
from Login_Setup import *

class Controller:

    def __init__(self):
        pass

    def Start(self):
        self.StartProograms =  Check()   #object Check
        self.StartProograms.AdminTrue.connect(self.Login)
        self.StartProograms.AdminFalse.connect( self.Create )
        self.StartProograms.ErrorDataBase.connect( self.Create )
        self.Checker = self.StartProograms.Run()

        if self.Checker == False:
            sys.exit(sys.argv)

    def Create(self):
        self.Create = GuiSetup()
        self.Create.CreateFileini()  # mark(1)  i am not have admin
        self.Create.CreateFinsh.connect(self.Login)

    def StartCustomer(self):
        try:
            # # run chieck all file and setup or login in if true change  sessions.StartProogramAccsses = True
            if sessions.StartProogramAccsses:
                self.Customer = StartClass()
                self.Customer.show()
            else:
                print('Error')
        except Exception as Error:
            Name_Function = '__name__ = '
            print( Name_Function, Error )

    def Login(self):
        self.RunLogin = Login()
        BackMsg = self.RunLogin.Start()
        self.RunLogin.AdminPassTrue.connect(self.StartCustomer)
        self.RunLogin.ChangeAdminPass.connect( self.Login )

        if BackMsg == False:
            sys.exit( sys.argv )

def StartMain():
    try:

        appss = QApplication( sys.argv )          # only object not run or show
        appss.setApplicationName('Customer program')
        appss.setApplicationVersion("1.0 Beta")
        appss.setObjectName('Customer')
        OBcontroller = Controller()
        OBcontroller.Start()
        sys.exit( appss.exec_())

    except Exception as Error:
        Name_Function = 'StartMain = '
        print( Name_Function, Error )



if __name__ == '__main__':
    StartMain()



