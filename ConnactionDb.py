import pymysql
import sqlite3
import sessions
from customre import QMessageBox
from language import *



class C_ConnactionDb(Lang):
    """connection For Proograms"""
    def F_ConnactionDb(self):
        self.dialogConnection = QMessageBox().setGeometry(0,0,0,0)
        if sessions.DatabaseTypeConn == 'MySQL':
            try:
                self.connection = pymysql.connect(
                    host=sessions.NameServer,
                    user=sessions.UserNameDb,
                    password=sessions.PasswordDb,
                    db=sessions.NameDb,
                    autocommit=True,
                    # charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor )
                return True
            except Exception as FindError:
                print( FindError )
                if '10061' in str( FindError ):
                    print( 'ServerNotConnection' )
                    QMessageBox.about( self.dialogConnection, self.WrongTitle ,self.CServerOff)
                elif '11001' in str( FindError ):
                    print( 'ErrorServer' )
                    QMessageBox.about( self.dialogConnection, self.WrongTitle ,self.CServerNameError)
                elif '1045' in str( FindError ):
                    print( 'ErrorUserNameOrPassword' )
                    QMessageBox.about( self.dialogConnection, self.WrongTitle ,self.CUserPassError)
                elif '1049' in str( FindError ):
                    print( 'ErrorNamedatabase' )
                    QMessageBox.about( self.dialogConnection, self.WrongTitle ,self.CDbError)
                else:
                    Name_Function = 'Page_ConnactionDb_F_ConnactionDb = '
                    print( Name_Function, FindError )
                return False
        elif sessions.DatabaseTypeConn == 'SQLite':
            """ create a database connection to a SQLite database """
            try:
                if sessions.os.path.isfile( sessions.NamedbSQLite ):#sessions.PathdbSQLiteOBJ +
                    return True
                else:
                    return False

            except Exception as FindError:
                print( FindError )
                sessions.PathdbSQLiteOBJ = None

    def F_inputUserGuiTest(self):
        # only Test input user info server and Create dataBase
        self.dialogConnection = QMessageBox().setGeometry(0,0,0,0)
        try:
            self.connTestAndCreateDb = pymysql.connect(
                host=sessions.NameServer,
                user=sessions.UserNameDb,
                password=sessions.PasswordDb,
                cursorclass=pymysql.cursors.DictCursor )
            return True
        except Exception as FindError:
            print( FindError )
            if '10061' in str( FindError ):
                print( 'ServerNotConnection')
                QMessageBox.about( self.dialogConnection, self.WrongTitle ,self.CServerOff)
            elif '11001' in str( FindError ):
                print( 'ErrorServer')
                QMessageBox.about( self.dialogConnection, self.WrongTitle ,self.CServerNameError)
            elif '1045' in str( FindError ):
                print( 'ErrorUserNameOrPassword' )
                QMessageBox.about( self.dialogConnection, self.WrongTitle ,self.CUserPassError)
            elif '1049' in str( FindError ):
                print( 'ErrorNamedatabase' )
                QMessageBox.about( self.dialogConnection, self.WrongTitle ,self.CDbError)
            else:
                Name_Function = 'Page_ConnactionDb_F_inputUserGuiTest = '
                print( Name_Function, FindError )
            return False