from ToolsGui import ToolsLogin
import sessions

class Db_Create():
    '''this class for Make Database and check tabel and info connection'''
    Checker = ToolsLogin()      #object Connection
    def CheckDataBase(self):
        ''' read file ini '''
        try:
            if sessions.DatabaseTypeConn == 'MySQL':
                CmdSQL = '''SHOW DATABASES LIKE '{}' '''.format( sessions.NameDb )
                BackMsg = self.Checker.F_SQLCheckDb(CmdSQL)
                if type(BackMsg) == type([]):
                    sessions.AceessNameDB = True   
                    print( 'قاعدة البيانات متوفرة' )
                    return True
                else:
                    return False
            elif sessions.DatabaseTypeConn == 'SQLite':
                if sessions.os.path.isfile( sessions.NamedbSQLite ):#sessions.path +
                    return True
                else:
                    return False
            else:
                pass
        except Exception as Error:
            Name_Function = 'class_Db_Create_CheckDataBase  = '
            print( Name_Function, Error )

    def CheckCount_NameTabel(self):
        ''' read file ini '''
        try:
            if sessions.DatabaseTypeConn == 'MySQL':
                CmdSQL = '''show tables from {}'''.format( sessions.NameDb )
                BackMsg = self.Checker.F_SQLGetManyOnlySelect(CmdSQL)  # self check count tabel
                if BackMsg != () and len(BackMsg)<= len(sessions.InProogramNameTabel):       # Not None
                    sessions.AceessCountTabelInDb = len(BackMsg)            #count Tabel
                    for Row in BackMsg:
                       for key,vlaues in Row.items():
                           sessions.AceessNameTabelInDb.append(vlaues)      #name tabel
                    return True
                else:
                    print('لايوجد جداول بهذ القاعدة')
                    return False
            elif sessions.DatabaseTypeConn == 'SQLite':
                CmdSQL = """SELECT name FROM sqlite_master where type='table'"""
                BackMsg = self.Checker.F_SQLGetManyOnlySelect(CmdSQL)  # self check count tabel
                if BackMsg != [] and BackMsg != None:       # Not None
                    sessions.AceessCountTabelInDb = len(BackMsg) - 1            #count Tabel
                    for Row in BackMsg:
                       for key,value in Row.items():
                           if value == 'sqlite_sequence':
                                continue
                           else:
                               sessions.AceessNameTabelInDb.append( value )  # name tabel
                    return True
                else:
                    print('لايوجد جداول بهذ القاعدة')
                    return False
            else:
                pass
        except Exception as Error:
            Name_Function = 'class_Db_Create_CheckCount_NameTabel  = '
            print( Name_Function, Error )

    def CheckAdminInDb(self):
        try:
            if sessions.DatabaseTypeConn == 'MySQL':
                CMdSQLCheckAdimn = """SELECT `id_admin` FROM `admin` WHERE id_admin = 1 """
                CheckAdmin = self.Checker.F_SQLGetManyOnlySelect(CMdSQLCheckAdimn)
                if CheckAdmin:
                    sessions.InProogramHaveAdmin = True
                    return True
                else:
                    sessions.InProogramHaveAdmin = False
                    return False  # is admin not have
            elif sessions.DatabaseTypeConn == 'SQLite':
                CMdSQLCheckAdimn = """SELECT `id_admin` FROM `admin` WHERE id_admin = 1 """
                CheckAdmin = self.Checker.F_SQLGetManyOnlySelect( CMdSQLCheckAdimn )
                if CheckAdmin:
                    sessions.InProogramHaveAdmin = True
                    return True
                else:
                    sessions.InProogramHaveAdmin = False
                    return False  # is admin not have
            else:
                pass
        except Exception as Error:
            Name_Function = 'class_Db_Create_CheckAdminInDb  = '
            print( Name_Function, Error )

    def CreateDataBase(self):
        try:
            CmdSQL = """CREATE DATABASE {}""".format(sessions.NameDb)
            BackMsgCreateDb = self.Checker.F_SQLCreatDb(CmdSQL)
            if BackMsgCreateDb:
                print( 'تم زراعه القاعدة بنجاح' )
                BackMsgeCreateTabel = self.Checker.F_SQLGetManyOnlyCcommitWithForLoop(sessions.CreateTabel)
                if BackMsgeCreateTabel:
                    print('تم زراعه الجداول بنجاح')
                    return True
                else:
                    print('لم يتم زراعه الجداول')
            else:
                print('لم يتم زراعه قاعدة البيانات')
                return False

        except Exception as Error:
            Name_Function = 'class_Db_Create_CreateDataBase  = '
            print( Name_Function, Error )
