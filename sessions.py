from datetime import datetime,timedelta
import os


#############CSS
SetupCSS =  open( 'Icon/Setup.css' ).read()
LoginCSS = open('Icon/Login.css' ).read()
CustomreCSS =  open( 'Icon/customre.css' ).read()
###########################################
path = os.getcwd() + '\\'
FileName = 'Setting.ini'
###########################################
StatusMySql = False
#set info db create & connection
#type connection
DatabaseTypeConn = ''
###########################################
#MySQL
TypeDb = ''
NameServer = ''
UserNameDb = ''
PasswordDb = ''
NameDb = ''
###########################################
#SQLite
#connSQLite = None
PathdbSQLiteOBJ = ''           # this path only in program on start (this path forever auotChange
NamedbSQLite = 'Data.db'
###########################################
#info join
UserNameAdmin = None
SetTimeUnBlock = 'None'
SetTimeBlock = None
###########################################
# Check and Read Server aceess count and Name Tabel & Server info & DataBase in file ini
AceessTypeDb = None
AceessNameServer = None
AceessUserNameDb = None
AceessPassDb = None
AceessNameDB = None
AceessCountTabelInDb = None
AceessNameTabelInDb = []
# orginal Comparison
#dataBase Varibale
InProogramCountTabel = 3
InProogramNameTabel = ['admin','customers','service']
InProogramHaveAdmin = None
SetSelectLang = 'Eng'
#all login Ture Run Programs
StartProogramAccsses = None
#my Contral system Database and info files
###########################################
## 1 to 112 limet
#for programs text
SyDb = 88
#for info admin
SyAd = 70
#for file ini
SyFi = 45
###########################################
CreateTabel = ["""CREATE TABLE `admin` (
                  `id_admin` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                  `Name_admin` varchar(50) NOT NULL,
                  `Pass_admin` varchar(250) NOT NULL,
                  `Question_admin` varchar(500) NOT NULL,
                  `Answer_admin` varchar(500) NOT NULL,
                  `Lang_admin` varchar(3) NOT NULL DEFAULT 'eng'
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
                """,
                """CREATE TABLE `customers` (
                  `id_customer` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                  `name_customer` varchar(50) NOT NULL,
                  `phone_customer` varchar(50) DEFAULT NULL,
                  `email_customer` varchar(50) DEFAULT NULL,
                  `country_customer` varchar(50) DEFAULT NULL,
                  `note_customer` text,
                  `startservice_customer` date NOT NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
                """,
                """CREATE TABLE `service` (
                  `id_service` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                  `typeService` varchar(20) NOT NULL,
                  `name_domain` varchar(50) NOT NULL,
                  `startservice` date NOT NULL,
                  `endservice` date NOT NULL,
                  `info_domain` text DEFAULT NULL,
                  `priceCompany` decimal(13,3) DEFAULT '0.000',
                  `priceMe` decimal(13,3) DEFAULT '0.000',
                  `id_tabel_customer` int(11) DEFAULT NULL,
                  KEY `id_cuetomer` (`id_tabel_customer`),
                  CONSTRAINT `id_cuetomer` FOREIGN KEY (`id_tabel_customer`) REFERENCES `customers` (`id_customer`) ON DELETE CASCADE ON UPDATE CASCADE
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
                """]
###########################################

CreateTabelSQL = ["""CREATE TABLE `admin` (
                  `id_admin` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  `Name_admin` varchar(50) NOT NULL,
                  `Pass_admin` varchar(250) NOT NULL,
                  `Question_admin` varchar(500) NOT NULL,
                  `Answer_admin` varchar(500) NOT NULL,
                  `Lang_admin` varchar(3) NOT NULL DEFAULT 'eng'
                ) 
                """,
                """CREATE TABLE `customers` (
                  `id_customer` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  `name_customer` varchar(50) NOT NULL,
                  `phone_customer` varchar(50) DEFAULT NULL,
                  `email_customer` varchar(50) DEFAULT NULL,
                  `country_customer` varchar(50) DEFAULT NULL,
                  `note_customer` text,
                  `startservice_customer` date NOT NULL
                ) 
                """,
                """CREATE TABLE `service` (
                  `id_service` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  `typeService` varchar(20) NOT NULL,
                  `name_domain` varchar(50) NOT NULL,
                  `startservice` date NOT NULL,
                  `endservice` date NOT NULL,
                  `info_domain` text DEFAULT NULL,
                  `priceCompany` decimal(13,3) DEFAULT '0.000',
                  `priceMe` decimal(13,3) DEFAULT '0.000',
                  `id_tabel_customer` int(11) DEFAULT NULL,
                  FOREIGN KEY (`id_tabel_customer`) REFERENCES `customers` (`id_customer`) ON DELETE CASCADE ON UPDATE CASCADE
                ) 

                """]
###########################################
# Aboutinfo1 = """
# <!DOCTYPE html>
# <html>
#
# <head>
#
#     <style>
#         body {
#             margin: 0;
#             background-color: transparent;
#             color: darkorange;
#             text-align: center;
#             font-size: 30px;
#             padding: 0;
#         }
#     </style>
# </head>
#
# <body>
#     <p>M3foOos</p>
# </body>
#
# </html>
# """
# Aboutinfo2 = """<!DOCTYPE html>
# <html>
#
# <head>
#     <script language=JavaScript>
#         var message = "";
#         function clickIE() {
#             if (document.all) {
#                 (message);
#                 return false;
#             }
#         }
#
#         function clickNS(e) {
#             if (document.layers || (document.getElementById && !document.all)) {
#                 if (e.which == 2 || e.which == 3) {
#                     (message);
#                     return false;
#                 }
#             }
#         }
#         if (document.layers) {
#             document.captureEvents(Event.MOUSEDOWN);
#             document.onmousedown = clickNS;
#         } else {
#             document.onmouseup = clickNS;
#             document.oncontextmenu = clickIE;
#         }
#
#         document.oncontextmenu = new Function("return false")
#     </script>
#     <style>
#         body {
#             background-color: black;
#         }
#
#         body .About {
#             align-content: center;
#             text-align: center;
#             color: aliceblue;
#             height: 200px;
#         }
#     </style>
# </head>
#
# <body>
#     <MARQUEE class="About" direction="up" scrollamount="1">
#         <h1></h1>
#         
#     </MARQUEE>
#
# </body>
#
# </html>
#             """
def __Delete__():
    del AceessTypeDb
    del AceessNameServer
    del AceessUserNameDb
    del AceessPassDb
    del AceessNameDB
    del AceessCountTabelInDb
    del AceessNameTabelInDb
    del InProogramCountTabel
    del InProogramNameTabel
    del InProogramHaveAdmin
    del CreateTabel

#
# if __name__ == '__main__':
#     pass

