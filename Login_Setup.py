
from customre import *
from CreateINI import *
from CreateDb import *
from language import *


############################################
class Gui_Login_Setup(Login_Setup,Lang):

    def __init__(self,parent= None):
        try:
            super(Gui_Login_Setup,self).__init__(parent)
            self.Tools = ToolsLogin()   #object class
            self.MakeDb = Db_Create()   #object class
            self.MakeIni = ini()        #object class
        except Exception as Error:
            Name_Function = 'class Gui_Login_Setup , Func __init__ = '
            print( Name_Function, Error )
############################################

############################################
class GuiSetup(Gui_Login_Setup):
    CreateFinsh = pyqtSignal(str)

    def CreateFileini(self):
        self.setWindowTitle(self.SWindowTitle)
        self.setWindowIcon( QIcon( 'Icon\Program_icon.png' ) )
        self.setStyleSheet( sessions.SetupCSS )

        self.show()
        try:
            #if have user admin
            if sessions.InProogramHaveAdmin == None:
                self.HandelAllPushbutton()
                self.IndexSelectedDb()
                self.RegexOn()
            # not have user admin
            elif sessions.InProogramHaveAdmin == False:
                self.SettingPageSetupAdmin()
            else:
                pass
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func CreateFileini = '
            print( Name_Function, Error )
    def RegexOn(self):
        try:
            #Page Register User  And SecurityAnswer
            ErrorInputLine = [self.Page3LineEdit_Username,self.Page3LineEdit_SecurityAnswer]
            self.Tools.F_RegisterNick(ErrorInputLine)
            #page Set Server Create New localhost And Have
            ErrorInputLine2 = [self.frame1_lineEdit_localhost,self.frame1_lineEdit_localhost_HaveDb]
            self.Tools.F_Createlocalhost(ErrorInputLine2)
            #page Set Name database Create And And Have
            ErrorInputLine3 = [self.frame1_lineEdit_databaseName,self.frame1_lineEdit_databaseName_HaveDb]
            self.Tools.F_CreateDb(ErrorInputLine3)
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func RegexOn = '
            print( Name_Function, Error )
        ####
    def   HandelAllPushbutton(self):
        try:
            #page 0 pushputton Next
            self.Page0_pushButton_next.clicked.connect( self.IndexSelectedDb )  #Mysql clicked to page New or Have Db
            #page 2 info Db New Or Connection
            self.page2_pushButton_next.clicked.connect( self.GetDatabaseInfo ) #next For page 3
            self.page2_pushButton_back.clicked.connect( self.IndexSelectedDb ) #Back For page 0
            #page 3 register admin
            self.page3_pushButton_back.clicked.connect(self.GetDatabaseInfo)  # back for page  2 info db
            ### counter methood pages
            #GetDatabaseInfo if run firestTime
            self.QMsgCountSetUpDB = 0
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func HandelAllPushbutton = '
            print( Name_Function, Error )

    def IndexSelectedDb(self):
        try:
            #self.stackedWidget.setCurrentIndex(3)  #Test Quick open dialog
            self.stackedWidget.setCurrentIndex(0)  # set page 0 for creat Database
            HaveDb = self.HaveDb_radioButton.isChecked()
            NewDb = self.NewDb_radioButton.isChecked()
            group = QButtonGroup()
            group.addButton(self.HaveDb_radioButton)
            group.addButton(self.NewDb_radioButton)
            SelectTypeDB = self.Page0comboBoxSelectDbType.currentText()
            if HaveDb:
                if SelectTypeDB != '':
                    self.stackedWidget.setCurrentIndex(1)  # set page have db index
                    del HaveDb,NewDb
                    group.setExclusive( False )
                    self.NewDb_radioButton.setChecked( False )
                    self.HaveDb_radioButton.setChecked( False )
                    group.setExclusive( True )
                    if SelectTypeDB == 'MySQL':
                        self.frame_9.show()
                        self.frame_5.hide()
                        self.pushButtonNextToSelectdbMySQL_Have.clicked.connect(self.GetinfoHaveMySQL) # Chooes Msql Has
                        self.pushButtonBackToSelectdbMySQL_Have.clicked.connect(self.IndexSelectedDb) #Back BackToSelectdbMySQL_Have
                    elif SelectTypeDB == 'SQLite':  # Type SQLite
                        ## Go Methood Havd Db SQLite
                        self.frame_9.hide()
                        self.frame_5.show()
                        self.toolButton_3.clicked.connect( self.GetPathChoose )                   # Chooes SQLite Has
                        self.pushButtonBackToSelectdbSQLite.clicked.connect(self.IndexSelectedDb) #Back BackToSelectdbSQLite
                    else:
                        pass
            elif NewDb:
                if SelectTypeDB !='':
                    del HaveDb, NewDb
                    group.setExclusive( False )
                    self.NewDb_radioButton.setChecked( False )
                    self.HaveDb_radioButton.setChecked( False )
                    group.setExclusive( True )
                    # self.stackedWidget.setCurrentIndex( 2 )  # set page New db index
                    self.InputInfoDb.hide()  # this for HaveDb
                    self.Label_ErrorConnection.hide()  # this for Error Connections
                    if SelectTypeDB == 'MySQL':   #type MySQL
                        self.SeletedNameDb.setText(str(SelectTypeDB))
                        self.SetTypeSelectedDb = 'MySQL'
                        # here for user connection selected
                        sessions.DatabaseTypeConn = self.SetTypeSelectedDb
                        self.GetDatabaseInfo()
                    elif SelectTypeDB == 'SQLite': #Type SQLite
                        self.SeletedNameDb.setText(str(SelectTypeDB))
                        self.SetTypeSelectedDb = 'SQLite'
                        # here for user connection selected
                        sessions.DatabaseTypeConn = self.SetTypeSelectedDb
                        #Checker db file in path here
                        if os.path.isfile(sessions.NamedbSQLite ):
                            print('ملف قاعدة البيانات المحلية موجود')
                            QMessageBox.about( self, self.InfoTitle, self.SHaveDbLocl)
                            self.MakeIni.Make_ini( 'InfoServer' )
                            print('تم انشاء ملف ini')
                        else:
                            # Create Data Base SLQLite in db and and file ini
                            BackMsg = self.Tools.F_SQLGetManyOnlyCcommitWithForLoop(sessions.CreateTabelSQL)
                            if BackMsg:
                                self.MakeIni.Make_ini('InfoServer')
                                print('تم ان شاء قاعدة البيانات باقي الحين معلومات دخول الادمن ')
                                self.SettingPageSetupAdmin()
                            else:
                                print('لم يتم ان شاءقاعدة البيانات')
                    else:
                        pass
                else:
                    pass
            else:
                pass
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func IndexSelectedDb = '
            print( Name_Function, Error )

    def GetDatabaseInfo(self):
        try:
            #Cmd Setting out Gui
            GetInputNameserver = self.frame1_lineEdit_localhost.text()
            GetInputUsernameDb = self.frame1_lineEdit_username.text()
            GetInputPasswordDb = self.frame1_lineEdit_password.text()
            GetInputNameDatabase = self.frame1_lineEdit_databaseName.text()
            #show Stackedwidget page 3 for create admin
            self.stackedWidget.setCurrentIndex( 2 )  # set page 0 for creat Database
            # and GetInputUsernameDb and GetInputPasswordDb
            if (GetInputNameserver and GetInputNameDatabase and GetInputUsernameDb != ''):
                sessions.TypeDb = 'MySQL'
                sessions.NameServer = GetInputNameserver
                sessions.UserNameDb = GetInputUsernameDb
                sessions.PasswordDb = GetInputPasswordDb
                sessions.NameDb = GetInputNameDatabase
                CheckInfoDataBase = self.Tools.F_inputUserGuiTest() # text info input
                if CheckInfoDataBase:
                    print('اتصال ناجح')
                    BackMsgCheckNameDb = self.MakeDb.CheckDataBase()
                    if BackMsgCheckNameDb: # If True , I have this dataName
                        print('يوجد قاعدة بيانات بهذا الاسم')
                        QMessageBox.about( self, self.WrongTitle, self.SHaveDbGlobl)
                    else:
                        ' اذا غير موجودة قاعدة البيانات'
                        ''' انشاء قاعدة البيانات والجداول'''
                        BackMsgCreateDb = self.MakeDb.CreateDataBase()
                        if BackMsgCreateDb:
                            print('تم انشاء قاعدة البيانات بنجاح')
                            self.MakeIni.Make_ini('InfoServer')
                            # Go To Page Create Admin
                            self.SettingPageSetupAdmin()
                        else:
                            print('لم يتم انشاء قاعد البيانات يوجد مشكلة')
                else:
                    print( 'فشل الاتصال الرجاء' )
                    self.Label_ErrorConnection.show()  # show label status Connection
            else:
                if self.QMsgCountSetUpDB >= 1:
                    print( 'الرجاء ادخال جميع الحقول' )
                    QMessageBox.about( self, self.WrongTitle, self.SEnterFields )
                else:
                    self.QMsgCountSetUpDB += 1
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func GetDatabaseInfo = '
            print( Name_Function, Error )

    def SettingPageSetupAdmin(self):   #setting for open

        try:
            self.stackedWidget.setCurrentIndex(3)
            self.page3_pushButton_back.hide()  # pushputtin Back
            self.page3_pushButton_next.clicked.connect(self.SetupAdmin)
            #Page Register User
            ErrorInputLine = [self.Page3LineEdit_Username,self.Page3LineEdit_SecurityAnswer,]
            self.Tools.F_RegisterNick(ErrorInputLine)
            # SetupAdmin if run firestTime
            self.QMsgCountSetUpAdmin = 0
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func SettingPageSetupAdmin = '
            print( Name_Function, Error )

    def SetupAdmin(self):
        try:
            GetInputUserName = self.Page3LineEdit_Username.text()
            GetInputPassword = self.Page3LineEdit_Pass.text()
            GetInputRplayPassword = self.Page3LineEdit_RplyPass.text()
            GetInputSecurityQuestion = self.Page3_comboBoxSecurityQuestion.currentText()
            GetInputSecurityAnswer = self.Page3LineEdit_SecurityAnswer.text()
            if GetInputUserName and GetInputPassword and GetInputRplayPassword and GetInputSecurityQuestion and GetInputSecurityAnswer:
                if GetInputPassword == GetInputRplayPassword:
                    print( ' تفريغ جدول الادمن لعدم تطابق العضوية ' )
                    if sessions.DatabaseTypeConn == 'MySQL':
                        self.Tools.F_SQLGetManyOnlyCcommit( " TRUNCATE TABLE admin " )
                    elif sessions.DatabaseTypeConn == 'SQLite':
                        print( ' تفريغ جدول الادمن لعدم تطابق العضوية ' )
                        self.Tools.F_SQLGetManyOnlyCcommit(""" DELETE FROM admin """)
                        self.Tools.F_SQLGetManyOnlyCcommit(""" UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'admin' """ )
                        self.Tools.F_SQLGetManyOnlyCcommit(""" VACUUM """)
                    else:
                        pass
                    ''' تشفير كلمة المرور للمدير '''
                    GetInputPassword = self.Tools.F_MD5( GetInputPassword)
                    GetInputSecurityQuestion = self.Tools.F_Encrypt(GetInputSecurityQuestion,sessions.SyAd )
                    GetInputSecurityAnswer   = self.Tools.F_Encrypt(GetInputSecurityAnswer,sessions.SyAd )
                    CmdSQL = """INSERT INTO `admin`(Name_admin,Pass_admin,Question_admin,Answer_admin)
                    VALUES ('{}','{}','{}','{}')
                    """.format(GetInputUserName, GetInputPassword, GetInputSecurityQuestion, GetInputSecurityAnswer)
                    BackMsgCreateAdmin = self.Tools.F_SQLGetManyOnlyCcommit(CmdSQL)
                    if BackMsgCreateAdmin:
                        print( 'تم انشاء اسم المستخدم بنجاح' )
                        sessions.InProogramHaveAdmin = True  #Set For have Admin
                        self.CreateFinsh.emit('DoneCreatAdmin')
                    else:
                        print( 'لم يتم انشاء اسم المستخدم بنجاح' )
                        print('1062, "Duplicate entry 3 for key PRIMARY"'  'خطاء يوجد اسم نفسه')
                    self.close()
                    return True
                else:
                    print('كلمة المرور غير مطابقة')
                    QMessageBox.about( self, self.WrongTitle, self.SPassNotmatch )
            else:
                if self.QMsgCountSetUpAdmin >= 1:
                    QMessageBox.about( self, self.WrongTitle, self.SEnterFields )
                    print( 'الرجاء ادخال جميع الحقول' )
                else:
                    self.QMsgCountSetUpAdmin += 1
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func SetupAdmin = '
            print( Name_Function, Error )
    ###################################################
    ### Methood have database Tow Type
    ############ MySQL ####################
    def GetinfoHaveMySQL(self):
        try:
            GetInputNameserver = self.frame1_lineEdit_localhost_HaveDb.text()
            GetInputUsernameDb = self.frame1_lineEdit_username_HaveDb.text()
            GetInputPasswordDb = self.frame1_lineEdit_password_HaveDb.text()
            GetInputNameDatabase = self.frame1_lineEdit_databaseName_HaveDb.text()
            if (GetInputNameserver and GetInputNameDatabase and GetInputUsernameDb != ''):
                sessions.TypeDb = 'MySQL'
                sessions.NameServer = GetInputNameserver
                sessions.UserNameDb = GetInputUsernameDb
                sessions.PasswordDb = GetInputPasswordDb
                sessions.NameDb = GetInputNameDatabase
                CheckInfoDataBase = self.Tools.F_inputUserGuiTest()  # text info input
                if CheckInfoDataBase:
                    print( 'اتصال ناجح' )
                    sessions.DatabaseTypeConn = 'MySQL'
                    BackMsgCheckNameDb = self.MakeDb.CheckDataBase()
                    if BackMsgCheckNameDb:  # If True , I have this data
                        print( ' قاعد البيانات متوفرة' )
                        self.StatusMsgCheckDbHave.setText( 'جاري فحص قاعدة البيانات' )
                        BackMsgCheckTabelAndCount = self.MakeDb.CheckCount_NameTabel()
                        if BackMsgCheckTabelAndCount:
                            if (sessions.AceessCountTabelInDb == sessions.InProogramCountTabel) and (sessions.AceessNameTabelInDb == sessions.InProogramNameTabel):
                                self.StatusMsgCheckDbHave.setText( 'قاعة البيانات متوافقه مع البرنامج , تم الاعدادات بنجاح' )
                                self.MakeIni.Make_ini( 'InfoServer' )
                                self.close()
                                sessions.InProogramHaveAdmin = True
                                self.CreateFinsh.emit( 'RunLogin' )
                            else:
                                self.StatusMsgCheckDbHave.setText('بيانات الاتصال بالقاعدة صحيح , القاعدة غير متوافقه مع البرنامج' )
                                print( 'بيانات الاتصال بالقاعدة صحيح ,, هناك خلل في تطابق البيانات ' )
                        else:
                            print('اهني احط اذا كانت القاعدة مافيها جداول انشاء الجداول')
                            self.StatusMsgCheckDbHave.setText( 'بيانات الاتصال بالقاعدة صحيح ,, القاعدة غير متوافقه مع البرنامج' )
                            print('بيانات الاتصال بالقاعدة صحيح ,, هناك خلل في تطابق البيانات ')
                    else:
                        print('لا يوجد قاعدة بيانات بهذا الاسم ')
                        self.StatusMsgCheckDbHave.setText('لا يوجد قاعدة بيانات بهذا الاسم')
                else:
                    print( 'فشل الاتصال' )
                    self.StatusMsgCheckDbHave.setText( 'فشل الاتصال' )
            else:
                if self.QMsgCountSetUpDB >= 1:
                    print( 'الرجاء ادخال جميع الحقول' )
                    QMessageBox.about( self, self.WrongTitle, self.SEnterFields )
                else:
                    self.QMsgCountSetUpDB += 1
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func GetinfoHaveMySQL = '
            print( Name_Function, Error )
    ############ SQLite ####################

    def GetPathChoose(self):
        try:
            #SelectFile = QFileDialog.getExistingDirectory(self, "Select Directory") open folder
            SelectFile,_= QFileDialog.getOpenFileName(self,"Open File",'*.db')
            if SelectFile != '':
                self.lineEdit_5.setText(SelectFile)
                if(os.path.isfile(SelectFile) == True):
                    self.labelCheckDbSQLite.setText('جاري فحص القاعدة')
                    BackMsgSlitpathe= self.SplitPath(SelectFile)
                    if BackMsgSlitpathe:
                        BackMsgSQLiteCheckTabelCaount = self.MakeDb.CheckCount_NameTabel()
                        if (BackMsgSQLiteCheckTabelCaount == True) and (
                                sessions.AceessCountTabelInDb == sessions.InProogramCountTabel):
                            self.MakeIni.Make_ini('InfoServer')
                            self.labelCheckDbSQLite.setText( 'قاعدة البيانات متوافقة مع نظام البرنامج' )
                            self.pushButtonNextToSelectdbSQLite.clicked.connect( self.GetPathChooseFinsh)
                        else:
                            self.labelCheckDbSQLite.setText( 'قاعدة البيانات غير متوافقة مع نظام البرنامج' )
                        print( 'هناك خطاء في معلومات الاتصال ' )
                    else:
                        pass
                else:
                    print('No File')
            else:
                print(SelectFile)
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func GetPathChoose = '
            print( Name_Function, Error )

    def SplitPath(self,Path):
        try:
            sessions.NamedbSQLite = Path        #GetNameFile
            sessions.DatabaseTypeConn = 'SQLite'
            with open( sessions.FileName, 'w' ) as Cf:  # create file setting empyt for test
                Cf.write( '' )
            return True
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func SplitPath = '
            print( Name_Function, Error )

    def GetPathChooseFinsh(self):
        try:
            sessions.InProogramHaveAdmin = True
            self.close()
            self.CreateFinsh.emit('RunLogin')
        except Exception as Error:
            Name_Function = 'class GuiSetup , Func GetPathChooseFinsh = '
            print( Name_Function, Error )



class Check(Gui_Login_Setup):
    AdminTrue = pyqtSignal(str)
    AdminFalse = pyqtSignal(str)
    ErrorDataBase = pyqtSignal(str)

    '''this class for setting startup proograms not have ini'''
    def Run(self):
        try:
            SendCMD= self.MakeIni.CheckFile()
            if SendCMD:
                BackInfoConnIni = self.MakeIni.Read_ini()
                if BackInfoConnIni:
                    if sessions.DatabaseTypeConn == 'MySQL':
                        BackMsgCheckConnect = self.Tools.F_ConnactionDb()
                        if BackMsgCheckConnect:
                            BackMgCheckDb = self.MakeDb.CheckDataBase()
                            if BackMgCheckDb:
                                #Check Name Tabel And count And Have admin
                                BackMgCheckCount_NameDb = self.MakeDb.CheckCount_NameTabel()       #Check tabel name and count
                                if (BackMgCheckCount_NameDb == True) and (sessions.InProogramCountTabel == sessions.AceessCountTabelInDb
                                    )and (sessions.InProogramNameTabel == sessions.AceessNameTabelInDb):
                                    print( 'قاعدة البيانات ومعلومات البيانات متطابقة ' )
                                    BackMsgCheckAdmin = self.MakeDb.CheckAdminInDb()
                                    if BackMsgCheckAdmin:
                                        print('يوجد بيانات لتسجيل الدخول المدير')
                                        self.AdminTrue.emit( 'AdminTrue' )
                                    else:
                                        print('لا يوجد يوجد بيانات لتسجيل الدخول المدير ')
                                        # if have Row in Tabel Admin != 1  Empty the table (TRUNCATE)
                                        sessions.AceessNameTabelInDb.clear()  # remove list count name tabel becouse loob and doubel
                                        self.AdminFalse.emit('NoHasAdmin')
                                else:
                                    print('خطاء تطابق عدد واسمائها')
                                    self.ErrorDataBase.emit('TabelAndNameError')
                            else:
                                print('قاعدة البيانات غير متوفرة')
                                self.ErrorDataBase.emit('TabelAndNameError')
                        else:
                            print('لايوجد اتصال')
                            return False
                    elif sessions.DatabaseTypeConn == 'SQLite':
                        ''' اشيك على ملف القاعدة المحلية '''
                        BackMsgSQLiteCheck = self.MakeDb.CheckDataBase()
                        if BackMsgSQLiteCheck:
                            """ قاعدة البيانات موجوة اهني اشيك على الجداول والادمن اذا اوكية اردها ترو 
                             واذا الادمن مو جود اردها فولس على شان يفتح علي دايلوق الادمن """
                            BackMsgSQLiteCheckTabelCaount = self.MakeDb.CheckCount_NameTabel()
                            if (BackMsgSQLiteCheckTabelCaount == True) and (sessions.AceessCountTabelInDb == sessions.InProogramCountTabel):
                                BackMsgCheckAdmin = self.MakeDb.CheckAdminInDb()
                                if BackMsgCheckAdmin:
                                    self.AdminTrue.emit( 'AdminTrue' )
                                else:
                                    sessions.AceessNameTabelInDb.clear()  # remove list count name tabel becouse loob and doubel
                                    print('معلومات المدير غير موجود')
                                    self.AdminFalse.emit('NoHasAdmin')
                            else:
                                print('عدد الجداول او اسماء الجداول غير متطابقة و افتح له الستب')
                                print( 'ملف الاتصال وقاعدة البيانات المحلية موجودة , خطاء في التطابق ' )
                                self.ErrorDataBase.emit('TabelAndNameError')
                        else:
                            QMessageBox.about( self, self.InfoTitle, self.SNotHasdbLocal + sessions.NamedbSQLite )
                            print('ملف الاتصال موجود بس قاعدة البيانات المحلية غير موجودة ')
                            self.ErrorDataBase.emit('NoHasDataBase')
                    else:
                        print( 'لايوجد معلومات الاتصال بنوع قاعدة البيانات' )
                        self.ErrorDataBase.emit('NOHasNameDataBase')
                else:
                    print( 'معلومات الاتصال غير صحيحة' )
                    self.ErrorDataBase.emit('INFOConnectionError')
            else:
                self.ErrorDataBase.emit('FileError')
        except Exception as Error:
            Name_Function = 'Class Check_Run  = '
            print( Name_Function, Error )


from StartLogin import Login


