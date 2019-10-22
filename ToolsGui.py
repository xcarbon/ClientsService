from customre import *
from ConnactionDb import *
from encrypted import kyserText
from hashlib import md5

class ToolsLogin(C_ConnactionDb):
    ObjEncrypt = kyserText()
    ########## Start Block SQL Commeends  ###########
    #this methood only Check database befor Create
    def F_SQLCheckDb(self,Cmd):
        try:
            CheckDb = self.F_inputUserGuiTest()
            if CheckDb:
                with self.connTestAndCreateDb.cursor() as SendSQL:
                    SendSQL.execute(Cmd)
                    Back = SendSQL.fetchall()
                    return Back
            else:
                print(CheckDb)
        except Exception as Error:
            Name_Function = 'Class_ToolsGui_F_SQLGetManyOnlySelect  = '
            print( Name_Function, Error )
    #this methood only Create database after Check
    def F_SQLCreatDb(self,Cmd):
        try:
            CheckDb = self.F_inputUserGuiTest()
            if CheckDb:
                with self.connTestAndCreateDb.cursor() as SendSQL:
                    SendSQL.execute(Cmd)
                    self.connTestAndCreateDb.commit()
                return CheckDb
            else:
                return CheckDb
        except Exception as Error:
            Name_Function = 'Class_ToolsGui_F_SQLGetManyOnlyCcommit = '
            print( Name_Function, Error )

    # this methood Create Tabel loop CMD SQL any  any CMD loop For commit
    def F_SQLGetManyOnlyCcommitWithForLoop(self,Cmd):
        try:
            if sessions.DatabaseTypeConn == 'MySQL':
                CheckDb = self.F_ConnactionDb()
                if CheckDb:
                    with self.connection.cursor() as SendSQL:
                        for x in Cmd:
                            SendSQL.execute( x )
                        return True
                else:
                    return CheckDb
            elif sessions.DatabaseTypeConn == 'SQLite':
                CheckDb = self.F_ConnactionDb()
                if CheckDb:
                    return CheckDb

                else:
                    #if db local not has Create
                    Join = sqlite3.connect( sessions.NamedbSQLite )
                    coon = Join.cursor()
                    for x in Cmd:
                        coon.execute( x )
                    coon.close()
                    Join.close()

                    return True
        except Exception as Error:
            Name_Function = 'Class_ToolsGuiF_SQLGetManyOnlyCcommitWithForLoop = '
            print( Name_Function, Error )
#########################################################
#########################################################
    #SQLite Lits type To Dictionary typw
    def dict_factory(delf,cursor, row):
        try:
            d = {}
            for idx, col in enumerate( cursor.description ):
                d[col[0]] = row[idx]
            return d
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func dict_factory = '
            print( Name_Function, Error )

    # for only selectd query
    def F_SQLGetManyOnlySelect(self,Cmd):
        try:
            if sessions.DatabaseTypeConn == 'MySQL':
                CheckDb = self.F_ConnactionDb()
                if CheckDb:
                    with self.connection.cursor() as SendSQL:
                        SendSQL.execute(Cmd)
                        Back = SendSQL.fetchall()
                        return Back
                else:
                    print(CheckDb)
            elif sessions.DatabaseTypeConn == 'SQLite':
                CheckDb = self.F_ConnactionDb()
                if CheckDb:
                    Join = sqlite3.connect( sessions.NamedbSQLite )
                    Join.row_factory = self.dict_factory
                    coon = Join.cursor()
                    coon.execute(Cmd)
                    Back = coon.fetchall()
                    coon.close()
                    Join.close()
                    return Back
                else:
                    print( CheckDb )

        except Exception as Error:
            Name_Function = 'Class_ToolsGui_F_SQLGetManyOnlySelect  = '
            print( Name_Function, Error )

    #for create or insert or update or delete
    def F_SQLGetManyOnlyCcommit(self,Cmd):
        try:
            if sessions.DatabaseTypeConn == 'MySQL':
                CheckDb = self.F_ConnactionDb()
                if CheckDb:
                    with self.connection.cursor() as SendSQL:
                        SendSQL.execute(Cmd)
                        self.connection.commit()
                    return CheckDb
                else:
                    return CheckDb
            elif sessions.DatabaseTypeConn == 'SQLite':
                CheckDb = self.F_ConnactionDb()
                if CheckDb:
                    Join = sqlite3.connect( sessions.NamedbSQLite )
                    coon = Join.cursor()
                    coon.execute( Cmd )
                    Join.commit()
                    coon.close()
                    Join.close()
                    return True
                else:
                    print( CheckDb )
        except Exception as Error:
            Name_Function = 'Class_ToolsGuiF_SQLGetManyOnlyCcommit = '
            print( Name_Function, Error )

    ########## End Block SQL Commeends  ###########

    def F_Genertion(self):
        pass

    def F_Encrypt(self, plainText, Mfta7):
        try:
            BackDic = self.ObjEncrypt.keydic( Mfta7 )
            Send = self.ObjEncrypt.Encrypt( plainText, BackDic )
            return Send
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_Encrypt = '
            print( Name_Function, Error )

    def F_Decrypt(self, plainText, Mfta7):
        try:
            # BackDic = self.Encrypt.keydic(Mfta7)
            Send = self.ObjEncrypt.decryptText( plainText, Mfta7 )
            return Send
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_Decrypt = '
            print( Name_Function, Error )


    def F_RegisterNick(self,RegisterNick):
        try:
            ######### for curreancy
            reg_ex = QRegExp("[a-zA-Z,ا-ي,ئ,ؤ,أ,إ,لإ,آ]([A-Za-z0-9 ,ا-ي,ء,ئ,ؤ,أ,إ,لإ,آ,])+")
            for line in RegisterNick:
                input_validator = QRegExpValidator( reg_ex, line )
                line.setValidator( input_validator )

        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_RegisterNick = '
            print( Name_Function, Error )

    def F_Createlocalhost(self,BlockLine):
        try:
            #regx Blocl !@#$#%^&*()_+ in set info server >> name server >> name database
            reg_ex = QRegExp("[a-zA-Z0-9]([A-Za-z0-9,:,/,.])+")
            for line in BlockLine:
                input_validator = QRegExpValidator( reg_ex, line )
                line.setValidator( input_validator )
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_Createlocalhost = '
            print( Name_Function, Error )

    def F_CreateDb(self,BlockLine):
        try:
            #regx Block !@#$#%^&*()_+ in set info server >> name server >> name database
            reg_ex = QRegExp("[a-zA-Z]([A-Za-z0-9,_])+")
            for line in BlockLine:
                input_validator = QRegExpValidator( reg_ex, line )
                line.setValidator( input_validator )
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_CreateDb = '
            print( Name_Function, Error )

    def F_MD5(self,Text):
        try:
            Text = md5( Text.encode() ).hexdigest()
            return Text
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_MD5 = '
            print( Name_Function, Error )

############################################
    ########## Start Block Regx Exception ##########
    def F_Line_RegisterNick(self,RegisterNick):
        try:
            ######### for curreancy
            reg_ex = QRegExp("[a-zA-Z,ا-ي,ئ,ؤ,أ,إ,لإ,آ]([A-Za-z0-9 ,ا-ي,ء,ئ,ؤ,أ,إ,لإ,آ,])+")
            for line in RegisterNick:
                input_validator = QRegExpValidator( reg_ex, line )
                line.setValidator( input_validator )
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_Line_RegisterNick = '
            print( Name_Function, Error )

    def F_Line_Email(self,Email):
        try:
            ######### for curreancy
            reg_ex = QRegExp( "([A-Za-z0-9@.])+" )
            for line in Email:
                input_validator = QRegExpValidator( reg_ex, line )
                line.setValidator( input_validator )
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_Line_Email = '
            print( Name_Function, Error )

    def F_Line_Country(self,Country):
        try:
            ######### for curreancy
            reg_ex = QRegExp("([A-Za-z0-9 /,ا-ي,ء,ئ,ؤ,أ,إ,لإ,آ,])+" )
            for line in Country:
                input_validator = QRegExpValidator( reg_ex, line )
                line.setValidator( input_validator )
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_Line_Country = '
            print( Name_Function, Error )

    def F_Line_Phone(self,Phone):
        try:
            ######### for curreancy
            reg_ex = QRegExp( "([+0-9 /])+" )
            for line in Phone:
                input_validator = QRegExpValidator( reg_ex, line )
                line.setValidator( input_validator )
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_Line_Phone = '
            print( Name_Function, Error )

    def F_Line_curreancy(self,listLinecurreancy):
        try:
            ######### for curreancy
            reg_ex = QRegExp( "(\d{0,9})?[.]{1}(\d{3})?" )
            for line in listLinecurreancy:
                input_validator = QRegExpValidator( reg_ex, line )
                line.setValidator( input_validator )
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_Line_curreancy = '
            print( Name_Function, Error )

    def F_Line_Domain(self,listLineDomain):
        try:
            ######### for curreancy
            reg_ex = QRegExp( "[A-Za-z]+[A-Za-z0-9/:.]+[.]?[.A-Za-z0-9]+[.][.A-Za-z0-9/]+" )
            for line in listLineDomain:
                input_validator = QRegExpValidator( reg_ex, line )
                line.setValidator( input_validator )
        ########## Started Block Regx Exception ##########
        except Exception as Error:
            Name_Function = 'class ToolsLogin , Func F_Line_Domain = '
            print( Name_Function, Error )