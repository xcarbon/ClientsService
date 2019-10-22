import configparser
import sessions

class ini():
    '''this class Make ini for checker & read & edite file Setting System'''
    config = configparser.ConfigParser()
    def CheckFile(self):
        try:
            #if FileName in os.path.isdir(path):
            if sessions.os.path.isfile(sessions.path+sessions.FileName):
                return True
            else:
                return False
        except Exception as Error:
            Name_Function = 'class_ini_CheckFile  = '
            print( Name_Function, Error )

    def Make_ini(self,CMD):
        try:
            if not sessions.os.path.isfile( sessions.path + sessions.FileName ):
                if CMD == 'InfoServer':

                    if sessions.DatabaseTypeConn == 'MySQL':
                        self.config['TypeDataBase'] = {'DbConn':sessions.DatabaseTypeConn}
                        self.config['Server'] = {
                            'typeDb': sessions.TypeDb,
                            'server': sessions.NameServer,
                            'username': sessions.UserNameDb,
                            'password': sessions.PasswordDb,
                            'nameDb' : sessions.NameDb
                                            }
                        with open( sessions.FileName, 'w' ) as configfile:
                            self.config.write( configfile )
                    elif sessions.DatabaseTypeConn == 'SQLite':
                        self.config['TypeDataBase'] = {'DbConn':sessions.DatabaseTypeConn}
                        self.config['LocalDb'] = {
                            'typeDbsql': sessions.DatabaseTypeConn,
                            'nameDbsql' : sessions.NamedbSQLite
                                            }
                        with open( sessions.FileName, 'w' ) as configfile:
                            self.config.write( configfile )
                    else:
                        pass

                elif CMD == 'InfoSystem':
                    
                    pass
            else:
                sessions.os.remove( sessions.path + sessions.FileName )
                self.Make_ini( 'InfoServer' )
            #respones Block
            if CMD == 'ErrorLogin':
                self.config['TimerBlock'] = {
                    'unblocktime': sessions.SetTimeUnBlock,
                }
                with open( sessions.FileName, 'w' ) as configfile:
                    self.config.write( configfile )

        except Exception as Error:
            Name_Function = 'class ini , Func Make_ini = '
            print( Name_Function, Error )

    def Read_ini(self):
        try:
            self.config.sections()
            self.config.read(sessions.path + sessions.FileName)
            SerchWord = self.config.sections()
            if SerchWord != []:
                for titel in SerchWord:
                    if titel == 'TypeDataBase':
                        ReadTypeConn = self.config['TypeDataBase']
                        for Read in ReadTypeConn:
                            if Read == 'dbconn':
                                sessions.DatabaseTypeConn = ReadTypeConn[Read]
                    elif titel == 'Server':
                        ReadInfo = self.config['Server']
                        for info in ReadInfo:
                            if info == 'typedb':
                                sessions.TypeDb = ReadInfo[info]
                                sessions.DatabaseTypeConn = ReadInfo[info]
                            elif info == 'server':
                                sessions.NameServer = ReadInfo[info]
                            elif info == 'username':
                                sessions.UserNameDb = ReadInfo[info]
                            elif info == 'password':
                                sessions.PasswordDb = ReadInfo[info]
                            elif info == 'namedb':
                                sessions.NameDb = ReadInfo[info]
                            else:
                                pass
                        del ReadInfo
                    elif titel == 'LocalDb':
                        ReadInfo2 = self.config['LocalDb']
                        for info2 in ReadInfo2:
                            if info2 == 'typedbsql':
                                sessions.DatabaseTypeConn = ReadInfo2[info2]
                            elif info2 == 'namedbsql':
                                sessions.NamedbSQLite = ReadInfo2[info2]
                            else:
                                pass
                        del ReadInfo2
                    elif titel == 'TimerBlock':
                        ReadInfo3 = self.config['TimerBlock']
                        for info2 in ReadInfo3:
                            if info2 == 'unblocktime':
                                sessions.SetTimeUnBlock = ReadInfo3[info2]
                            else:
                                pass
                        del ReadInfo3
                    else:
                        pass
                return True
            else:
                return False
        except Exception as ErrorReadIni:
            print('Class ini , Function Read ini = ',ErrorReadIni)
            return False
