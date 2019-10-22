from Login_Setup import Gui_Login_Setup
from customre import *
import sessions

###Class Click label Forgot pass
# class ClickLabel(QLabel,QLineEdit):
#     try:
#         clicked = pyqtSignal(str)
#         PressKyebordEnter = pyqtSignal(str)
#         @pyqtSlot()
#         def mousePressEvent(self, event):
#             self.clicked.emit()
#             QLabel.mousePressEvent(self, event)
#
#         @pyqtSlot()
#         def keyPressEvent(self,event):
#             self.PressKyebordEnter.emit()
#             print(event)
#             QLineEdit.keyPressEvent(self,event)
#
#     except Exception as Error:
#         Name_Function = 'class ClickLabel = '
#         print( Name_Function, Error )
############################################

class Login(Gui_Login_Setup):
    AdminPassTrue = pyqtSignal( str )
    ChangeAdminPass = pyqtSignal(str)

    #class login
    def Start(self):
        try:
            self.setWindowTitle(self.LWindowTitle)
            self.setWindowIcon( QIcon('Icon/Program_icon.png'))
            self.setStyleSheet(sessions.LoginCSS)
            self.setFixedWidth(500)
            self.setFixedHeight(400)
            self.scrollAreaWidgetContents.setFixedHeight(400)
            self.scrollArea.setFixedHeight( 600 )
            BackMsgBlock = self.TimeBlockError('Comparison',sessions.SetTimeUnBlock)
            if BackMsgBlock == 'UnBlock':
                self.show()
                self.settingLoginIn()
            else:
                sessions.SetTimeBlock = 'Block'
                print('محظور الرجاء الدخول بعد ',BackMsgBlock)
                QMessageBox.about( self, self.AlertTitle, self.LBlocked + '[ {} '.format(BackMsgBlock) + self.LTimeBlock + ' ]')
                return False
        except Exception as Error:
            Name_Function = 'class Login , Func Start = '
            print( Name_Function, Error )

    def settingLoginIn(self):
        try:
            self.CountLoginError = 0
            ####Frame Forgot pass
            self.CountFotgotError = 0
            self.frame_Forgot_Errorquetion.hide()
            #############################
            self.stackedWidget.setCurrentIndex(4)
            self.ErrorNameOrPassword.hide()     #Error user or Pass
            self.moreIfJoin.hide()   #Fream Enter Error 3 more
            self.ForeGetlabel.hide()   #label Forget password

            #Page  loginUser
            ErrorInputLine = [self.frame3_lineEdit_username]
            self.Tools.F_RegisterNick(ErrorInputLine)

            #Set Focus
            self.frame3_lineEdit_username.setFocus()
            #click pushboutton or enter pressed LineEdite
            self.LoginJoinStander.clicked.connect(self.LoginAdminAccept)
            self.frame3_lineEdit_username.returnPressed.connect(self.LoginAdminAccept)
            self.frame3_lineEdit_pass.returnPressed.connect(self.LoginAdminAccept)
            #ForGet Label Clicked
            self.ForeGetlabel.mousePressEvent = self.ForgetPass

        except Exception as Error:
            Name_Function = 'class Login , Func settingLoginIn = '
            print( Name_Function, Error )

    def LoginAdminAccept(self):
        try:
            GetInputUserName = self.frame3_lineEdit_username.text()
            GetInputPassword = self.frame3_lineEdit_pass.text()
            if GetInputUserName and GetInputPassword != '':
                BackMsgConnect = self.Tools.F_ConnactionDb()
                if BackMsgConnect:
                    GetInputPassword = self.Tools.F_MD5( GetInputPassword)
                    CmdSQL = """SELECT `id_admin`, `Name_admin`, `Pass_admin` FROM `admin` 
                    WHERE `id_admin` = 1 
                    AND `Name_admin` LIKE '{}' 
                    AND `Pass_admin` LIKE '{}'
                    """.format(GetInputUserName,GetInputPassword)
                    CheckBoolenUserPass = self.Tools.F_SQLGetManyOnlySelect(CmdSQL)
                    if len(CheckBoolenUserPass) != 0:
                        sessions.UserNameAdmin = CheckBoolenUserPass[0]['Name_admin']   #username admin
                        sessions.SetTimeUnBlock = 'None'
                        self.MakeIni.Make_ini( 'ErrorLogin' )
                        print('المعلومات صحيحة جاري تشغيل البرنامج')
                        sessions.StartProogramAccsses = True
                        self.close()
                        self.AdminPassTrue.emit('Done')
                    else:
                        print('اسم المستخدم او كلمة المرور غير صحيحة')
                        self.CountLoginError += 1
                        self.LoginError()
                else:
                   print( 'اتصال غير ناجح' )
            else:
                QMessageBox.about( self,self.WrongTitle,self.LEnterUP )
                print('الرجاء ملئ الحقول')
        except Exception as Error:
            Name_Function = 'class Login , Func LoginAdminAccept = '
            print( Name_Function, Error )

    def LoginError(self):
        try:
            self.ErrorNameOrPassword.show()
            self.moreIfJoin.show()
            self.ForeGetlabel.show()
            self.countErrorJoin.setText( str( self.CountLoginError ) )
            if self.CountLoginError == 3 :
                countErrorNow = 5 - self.CountLoginError
                print(countErrorNow)
                QMessageBox.about( self, self.AlertTitle ,self.LHaveCount + '{}'.format(countErrorNow) + self.LForgetUp)
                print('تنبية بعد المحاولات سيتم حضرك 15 دقيقة')
            elif self.CountLoginError == 5:
                #caputuer Time Error For Block
                CaupterTimeError = self.TimeBlockError('Capture',None)
                #Recording time Error
                self.MakeIni.Make_ini('ErrorLogin')
                QMessageBox.about( self, self.AlertTitle,self.LBlock )
                self.close()
            else:
                print('عدد محاولات الدخول الخاطئه')
        except Exception as Error:
            Name_Function = 'class Login , Func LoginError = '
            print( Name_Function, Error )

    def ForgetPass(self,event):
        try:
            self.FrameRestPass.hide()  #if answer is couurct show frame rest pass
            self.frame_RestQuetionAndAnswers.hide()       # if want change quetion and answers secruty
            self.stackedWidget.setCurrentIndex(5)
            self.forgot_answersecurty_lineEdit.setFocus()
            self.forgot_answersecurty_lineEdit.returnPressed.connect( self.ForgetPassCheckAnswersSecruty )
            self.forgot_pushButton_join.clicked.connect(self.ForgetPassCheckAnswersSecruty)
        except Exception as Error:
            Name_Function = 'class Login , Func ForgetPass = '
            print( Name_Function, Error )

    def ForgetPassCheckAnswersSecruty(self):
        try:
            GetSelectQuetion = self.forgot_quetionsecurty_comboBox.currentText()
            InputAnswerSecruty = self.forgot_answersecurty_lineEdit.text()
            if InputAnswerSecruty != '':
                BackMsgConnect = self.Tools.F_ConnactionDb()
                if BackMsgConnect:
                    GetSelectQuetion = self.Tools.F_Encrypt(GetSelectQuetion,sessions.SyAd )
                    InputAnswerSecruty = self.Tools.F_Encrypt(InputAnswerSecruty,sessions.SyAd )
                    CmdSQL = """SELECT `id_admin`, `Question_admin`, `Answer_admin` FROM `admin` 
                                    WHERE `id_admin` = 1 
                                    AND `Question_admin` LIKE '{}' 
                                    AND `Answer_admin` LIKE '{}'
                                    """.format( GetSelectQuetion, InputAnswerSecruty )
                    BackMsgCheckAnswer = self.Tools.F_SQLGetManyOnlySelect(CmdSQL)
                    if len(BackMsgCheckAnswer) != 0:
                        print('الجواب السؤال صحيح')
                        self.ForGoteChangePass()
                    else:
                        print( 'الجواب خطاء' )
                        self.CountFotgotError += 1
                        self.ForGoteError()
                else:
                    print( 'اتصال غير ناجح' )
            else:
                QMessageBox.about( self, self.WrongTitle, self.LEnterQ_A )
                print('الرجاء ملئ الحقول')

        except Exception as Error:
            Name_Function = 'class Login , Func ForgetPassCheckAnswersSecruty = '
            print( Name_Function, Error )

    def ForGoteError(self):
        try:
            self.frame_Forgot_Errorquetion.show()
            self.countErrorJoin_2.setText( str( self.CountFotgotError ) )

            if self.CountFotgotError == 3 :
                countErrorNow = 5 - self.CountFotgotError
                QMessageBox.about( self, self.AlertTitle,self.LHaveCount + '{}'.format(countErrorNow)+ self.LForgetQAUP)
                print('تنبية بعد المحاولات سيتم حضرك 15 دقيقة')
            elif self.CountFotgotError == 5:
                #caputuer Time Error For Block
                CaupterTimeError = self.TimeBlockError('Capture',None)
                #Recording time Error
                self.MakeIni.Make_ini('ErrorLogin')
                QMessageBox.about( self, self.AlertTitle,self.LBlock)
                self.close()
            else:
                pass

        except Exception as Error:
            Name_Function = 'class Login , Func ForGoteError = '
            print( Name_Function, Error )

    def ForGoteChangePass(self):
        try:
            self.frame_Quetion_Answers_Join.hide()
            self.frame_Quetion_Answers_Join_2.hide()
            self.frame_RestQuetionAndAnswers.show()
            self.FrameRestPass.show()
            self.forgot_newpassword.setFocus()
            self.forgot_RetypePassword.returnPressed.connect( self.SaveNewPass )
            self.forgot_pushButton_Save.clicked.connect(self.SaveNewPass)
            self.checkBoxRestQuetion_Answer_Secruty.toggled.connect(self.CheckBox)
        except Exception as Error:
            Name_Function = 'class Login , Func ForGoteChangePass = '
            print( Name_Function, Error )

    def CheckBox(self):
        try:
            status = self.checkBoxRestQuetion_Answer_Secruty.checkState()
            if status:
                self.frame_Quetion_Answers_Join.show()
            else:
                self.frame_Quetion_Answers_Join.hide()
        except Exception as Error:
            Name_Function = 'class Login , Func CheckBox = '
            print( Name_Function, Error )

    def SaveNewPass(self):
        try:
            GetNewPass = self.forgot_newpassword.text()
            GetRetypePassword = self.forgot_RetypePassword.text()
            if GetNewPass == GetRetypePassword:
                GetNewPass = self.Tools.F_MD5(GetNewPass)
                status = self.checkBoxRestQuetion_Answer_Secruty.checkState()
                if status:
                    GetQuetionNew = self.forgot_quetionsecurty_comboBox.currentText()
                    GetAnswersNew = self.forgot_answersecurty_lineEdit.text()
                    #encrypt
                    GetQuetionNew = self.Tools.F_Encrypt(GetQuetionNew,sessions.SyAd )
                    GetAnswersNew = self.Tools.F_Encrypt(GetAnswersNew,sessions.SyAd )
                    CmdSQL = """UPDATE `admin` SET
                    Question_admin = '{}', Answer_admin = '{}', Pass_admin = '{}'
                    WHERE `id_admin` = 1 
                    """.format( GetQuetionNew, GetAnswersNew,GetNewPass )
                    BackMsgSaveAll = self.Tools.F_SQLGetManyOnlyCcommit(CmdSQL)
                    if BackMsgSaveAll:
                        print('تم تغير السوال السري والجواب والباسورد')
                        self.close()
                        self.ChangeAdminPass.emit('RunLogin')
                    else:
                        print( 'لم يتم تغير السوال السري والجواب والباسورد' )
                else:
                    CmdSQLOnlyPassChange = """ UPDATE `admin` SET Pass_admin = '{}' WHERE `id_admin` = 1 """.format(GetNewPass )
                    BackMsgSaveOnlyPass = self.Tools.F_SQLGetManyOnlyCcommit(CmdSQLOnlyPassChange)
                    if BackMsgSaveOnlyPass:
                        print('تم تغير الرقم السري بنجاح')
                        self.close()
                        self.ChangeAdminPass.emit('RunLogin')
                    else:
                        print('لم يتم تغير الرقم السري ')
            else:
                print('كلمة المرور غير متطابقة')
                QMessageBox.about( self, self.AlertTitle,self.SPassNotmatch )
        except Exception as Error:
            Name_Function = 'class Login , Func SaveNewPass = '
            print( Name_Function, Error )
    ##########################################
    #Method service for class Login
    def TimeBlockError(self,Cmd,Timer):
        try:
            if Cmd == 'Capture':
                # cuptuer Time Now
                TimeNowCapture = sessions.datetime.now()
                # add Minutes for time orginal
                AddTimeBlocked = TimeNowCapture + sessions.timedelta(minutes=5)  # final Time Blocked
                # Class object Time
                ToClassObjectTimeStr = AddTimeBlocked.strftime('%Y/%m/%d %H:%M:%S')
                sessions.SetTimeUnBlock = ToClassObjectTimeStr
                if sessions.SetTimeUnBlock != None:
                    return True
                else:
                    return  False
            elif Cmd == 'Comparison':
                if Timer != 'None':
                    # String To Object Class Time
                    ToObjectTimeClass = sessions.datetime.strptime(Timer, '%Y/%m/%d %H:%M:%S')
                    # Get Time Now Calss to String Strip Microsecoend and transfer to class Time
                    GetTime = sessions.datetime.now()
                    GetTimeSrtip = GetTime.strftime('%Y/%m/%d %H:%M:%S')
                    ToClassTimer = sessions.datetime.strptime( GetTimeSrtip, '%Y/%m/%d %H:%M:%S' )
                    if ToClassTimer >= ToObjectTimeClass:
                        return 'UnBlock'
                    elif ToClassTimer <= ToObjectTimeClass:
                        ##T ime remaining to remove the ban ##
                        # String To Object Class Time
                        ToObjectTimeClass = sessions.datetime.strptime( Timer, '%Y/%m/%d %H:%M:%S')
                        # Get Time Now Calss to String Strip Microsecoend and transfer to class Time
                        GetTime = sessions.datetime.now()
                        GetTimeSrtip = GetTime.strftime( '%Y/%m/%d %H:%M:%S' )
                        ToClassTimer = sessions.datetime.strptime( GetTimeSrtip, '%Y/%m/%d %H:%M:%S')
                        TheRestTime = ToObjectTimeClass - ToClassTimer
                        return TheRestTime
                    else:
                        pass

                else:
                    return 'UnBlock'
            else:
                pass
        except Exception as Error:
            Name_Function = 'class Login , Func TimeBlockError = '
            print( Name_Function, Error )


# if __name__ == '__main__':
#     app = QApplication( sys.argv )
#     objLogin = Login().Start()
#     objLogin.show()
#     app.exec_()