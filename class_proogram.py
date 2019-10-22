from Start_index import *

class Proograms(StartClass,Lang):
    """Class for Clients """
    def Onstartup_customer(self):
        try:
            Proograms.LoadAllDataClientsTabelWidget(self)   # load all service clients not select
            Proograms.LoadDataWidget(self)                  # load clients
            Proograms.HandelButtons(self)                   #all pushbutton home programs

        except Exception as Error:
            Name_Function = 'class_proogram_Onstartup_customer  = '
            print( Name_Function, Error )

    def LoadDataWidget(self):
        '''widget get all Clients for data base'''
        try:
            CMDSQL = """ SELECT * FROM `customers` ORDER BY name_customer ASC """
            Back = self.Tools.F_SQLGetManyOnlySelect(CMDSQL)
            self.customer_listWidget.clear()
            if len(Back) != 0:
                self.lcdNumber.display(len(Back))
                for coloum in Back:
                    self.customer_listWidget.addItem(coloum['name_customer'])
        except Exception as Error:
            Name_Function = 'class_proogram_LoadDataWidget  = '
            print( Name_Function, Error )

    def LoadDataTabelWidget(self,Id):
        '''if selected Client get all service in tabel from database'''
        try:
            CMDSQL = """ SELECT 
                    service.id_service,service.typeService,service.name_domain,service.startservice,
                    service.endservice,service.info_domain,service.priceCompany,
                    service.priceMe,customers.name_customer,service.id_tabel_customer,
                    customers.id_customer
            FROM service
            INNER JOIN customers 
            WHERE customers.id_customer = service.id_tabel_customer 
            AND customers.id_customer = '{}' """.format(Id)
            Back = self.Tools.F_SQLGetManyOnlySelect(CMDSQL)
            self.label_7.clear()  # clear name client
            if len(Back) != 0:
                self.label_7.setText(str(Back[0]['name_customer']))  #set name client
                xx = len(Back)
                self.customer_tableWidget.setRowCount(0)
                self.customer_tableWidget.setColumnCount(9)
                self.customer_tableWidget.hideColumn(8)   # id cloumn clients
                for Row in range(xx):
                    Column = 0
                    self.customer_tableWidget.insertRow( Row )
                    for ss,vv in Back[Row].items():
                        if ss == 'id_customer':
                            Column += 1
                            continue
                        elif ss == 'info_domain':
                            #Decryption
                            texter = self.Tools.F_Decrypt(vv,sessions.SyDb)
                            #print(texter)
                            self.customer_tableWidget.setItem(Row,Column,
                                     QTableWidgetItem(str(texter)) )
                        elif ss == 'name_domain':
                            #Decryption
                            texter = self.Tools.F_Decrypt(vv,sessions.SyDb)
                            self.customer_tableWidget.setItem(Row,Column,QTableWidgetItem(str(texter)) )
                        else:
                            self.customer_tableWidget.setItem( Row, Column,QTableWidgetItem( str( vv ) ) )
                        Column += 1
            else:
                print('لا يوجد خدمات لهذا العميل')
                self.customer_tableWidget.setRowCount( 0 )  # clear tbael all services clients
        except Exception as Error:
            Name_Function = 'class_proogram_LoadDataTabelWidget  = '
            print( Name_Function, Error )


    def LoadAllDataClientsTabelWidget(self):
        '''if start Programs or clicked bouttun get all service for all Client in tabel from database'''
        self.label_5.hide()  # hide label services client
        self.label_7.hide()  #hide label name client
        self.label_4.show()  # Services of all customers
        DeleteRow = self.customer_tableWidget.setRowCount( 0 )  # clear tbael all services clients
        self.customer_lineEdit_14.clear()  # clear id client
        try:
            CMDSQL = """
            SELECT 
               service.id_service,service.typeService,service.name_domain,service.startservice,
               service.endservice,service.info_domain,service.priceCompany,
               service.priceMe,customers.name_customer,service.id_tabel_customer,
               customers.id_customer
            FROM service
            INNER JOIN customers 
            WHERE customers.id_customer = service.id_tabel_customer 
            """
            Back = self.Tools.F_SQLGetManyOnlySelect(CMDSQL)
            if len(Back) != 0:
                self.customer_tableWidget.setRowCount(0)
                self.customer_tableWidget.showColumn( 8 )
                self.customer_tableWidget.setColumnCount(9) # AVG all Count Columns
                for Row in range(len(Back)):
                    Column = 0
                    self.customer_tableWidget.insertRow( Row )
                    for ss,vv in Back[Row].items():
                        if ss == 'id_customer':
                            Column += 1
                            continue
                        elif ss == 'info_domain':
                            #Decryption
                            texter = self.Tools.F_Decrypt(vv,sessions.SyDb)
                            self.customer_tableWidget.setItem(Row,Column,
                                     QTableWidgetItem(str(texter)) )
                        elif ss == 'name_domain':
                            #Decryption
                            texter = self.Tools.F_Decrypt(vv,sessions.SyDb)
                            self.customer_tableWidget.setItem(Row,Column,QTableWidgetItem(str(texter)) )
                        else:
                            self.customer_tableWidget.setItem( Row, Column,QTableWidgetItem( str( vv ) ) )
                        Column += 1
            else:
                print('None Data')
        except Exception as Error:
            Name_Function = 'class_proogram_LoadDataTabelWidget  = '
            print( Name_Function, Error )

    def HandelButtons(self):
        try:
            self.customer_listWidget.itemClicked.connect( lambda: Proograms.current_customer(self))
            self.customer_allService.clicked.connect( lambda: Proograms.LoadAllDataClientsTabelWidget(self))
        except Exception as Error:
                Name_Function = 'class_proogram_HandelButtons = '
                print( Name_Function, Error )

    def current_customer(self):
        ''' if clicked client in listwidgets get text name and send db Because he get id client and then
            set Id Client in lineEdite id client
        '''
        try:
            DeleteRow =self.customer_tableWidget.setRowCount(0) #clear tbael all services clients
            selectgroup = self.customer_listWidget.currentRow()
            #selectClient = self.customer_listWidget.currentItem().text()
            self.label_4.hide()  #Services of all customers
            self.label_5.show()  #show servics client
            self.label_7.show()  #show name client
            if selectgroup != -1:
                Name_selected = self.customer_listWidget.currentItem().text()
                CMDSQL = """ SELECT * FROM `customers` WHERE name_customer = '{}' ORDER BY name_customer ASC """.format(Name_selected)
                Back = self.Tools.F_SQLGetManyOnlySelect(CMDSQL)
                if len(Back) != 0:
                    self.customer_lineEdit_14.setText( str( Back[0]['id_customer'] ) )
                    Proograms.LoadDataTabelWidget(self,self.customer_lineEdit_14.text())
                else:
                    pass
        except Exception as Error:
                Name_Function = 'class_proogram_current_customer = '
                print( Name_Function, Error )
#####################################################

#####################################################
    def Add_ClientsContral(self,CmdContral):
        try:
            if CmdContral == 0:     #Add Client
                self.obj_Add_Client = dialogClients(self)
                self.obj_Add_Client.customer_pushButton_5.show()           #push Add
                self.obj_Add_Client.customer_pushButton_4.hide()           #push Edite
                self.obj_Add_Client.customer_pushButton_5.clicked.connect( lambda: Proograms.Add_Clients(self))
                self.obj_Add_Client.setWindowTitle( self.DCaddClientsTitle)
                self.obj_Add_Client.setWindowIcon( QIcon( 'Icon/add_client.png' ) )
                self.obj_Add_Client.exec_()
                del self.obj_Add_Client
            elif CmdContral == 1:     #Info Client
                idClient = self.customer_lineEdit_14.text()
                if idClient != '':
                    self.obj_Info = dialogClients(self)
                    self.obj_Info.customer_pushButton_5.hide()  # push Add
                    self.obj_Info.customer_pushButton_4.hide()  # push Edite
                    CMDSQL = """ SELECT * FROM `customers` WHERE id_customer = {} """.format(int(idClient))
                    Back = self.Tools.F_SQLGetManyOnlySelect(CMDSQL)
                    if len(Back) != 0:
                        #name client
                        self.obj_Info.customer_lineEdit_3.setText(str( Back[0]['name_customer']))
                        #get name client now
                        self.NameKnow = self.obj_Info.customer_lineEdit_3.text()
                        #phone client
                        texter = self.Tools.F_Decrypt(Back[0]['phone_customer'], sessions.SyDb )
                        self.obj_Info.customer_lineEdit_4.setText(str( texter))
                        #emaile client
                        texter = self.Tools.F_Decrypt(Back[0]['email_customer'], sessions.SyDb )
                        self.obj_Info.customer_lineEdit_5.setText(str(texter))
                        #country client
                        self.obj_Info.customer_lineEdit_6.setText(str( Back[0]['country_customer']))
                        # Start Transfer Date
                        StrDateNow = str(Back[0]['startservice_customer'])
                        ToObject = QDate.fromString(StrDateNow,'yyyy-MM-dd')
                        self.obj_Info.customer_dateEdit.setDate(ToObject)
                        # End Transfer Date
                        texter = self.Tools.F_Decrypt(Back[0]['note_customer'], sessions.SyDb )
                        self.obj_Info.customer_textEdit.setText(str(texter))  # notes
                        self.obj_Info.customer_lineEdit_3.setReadOnly( True )   # name
                        self.obj_Info.customer_lineEdit_4.setReadOnly( True )   # phone
                        self.obj_Info.customer_lineEdit_5.setReadOnly( True )   # email
                        self.obj_Info.customer_lineEdit_6.setReadOnly( True )   # country
                        self.obj_Info.customer_dateEdit.setReadOnly( True )  # date
                        self.obj_Info.customer_textEdit.setReadOnly( True )  # notes
                    self.obj_Info.setWindowTitle(self.DCinfoClientTitle)
                    self.obj_Info.setWindowIcon(QIcon('Icon/info_client.png'))
                    self.obj_Info.exec_()
                    del self.obj_Info
                else:
                    QMessageBox.about( self, self.WrongTitle, self.PSelectClient)
            elif CmdContral == 2:   #Edite Client
                idClient = self.customer_lineEdit_14.text()
                if idClient != '':
                    self.obj_Edite = dialogClients(self)
                    self.obj_Edite.customer_pushButton_5.hide()  # push Add
                    self.obj_Edite.customer_pushButton_4.show()  # push Edite
                    #get Info Clients For Edite
                    CMDSQL = """ SELECT * FROM `customers` WHERE id_customer = '{}' """.format(int(idClient))
                    Back = self.Tools.F_SQLGetManyOnlySelect(CMDSQL)
                    if (Back) != 0:
                        # name client
                        self.obj_Edite.customer_lineEdit_3.setText(str( Back[0]['name_customer'] ) )
                        # get name client now
                        self.NameKnow = self.obj_Edite.customer_lineEdit_3.text()
                        # phone client
                        texter = self.Tools.F_Decrypt(Back[0]['phone_customer'], sessions.SyDb )
                        self.obj_Edite.customer_lineEdit_4.setText(str(texter) )
                        # emaile client
                        texter = self.Tools.F_Decrypt(Back[0]['email_customer'], sessions.SyDb )
                        self.obj_Edite.customer_lineEdit_5.setText(str(texter) )
                        # country client
                        self.obj_Edite.customer_lineEdit_6.setText(str( Back[0]['country_customer'] ) )
                        # Start Transfer Date
                        StrDateNow = str(Back[0]['startservice_customer'])
                        ToObject = QDate.fromString(StrDateNow,'yyyy-MM-dd')
                        self.obj_Edite.customer_dateEdit.setDate(ToObject)
                        # End Transfer Date
                        texter = self.Tools.F_Decrypt(Back[0]['note_customer'], sessions.SyDb )
                        self.obj_Edite.customer_textEdit.setText(str(texter))  # notes
                    else:
                        pass
                    self.obj_Edite.customer_pushButton_4.clicked.connect( lambda: Proograms.Edite_Clients(self) )
                    self.obj_Edite.setWindowTitle(self.DcediteClientsTitle)
                    self.obj_Edite.setWindowIcon(QIcon( 'Icon/edite_client.png'))
                    self.obj_Edite.exec_()
                    del self.obj_Edite
                else:
                    QMessageBox.about( self, self.WrongTitle, self.PSelectClient)
            elif CmdContral == 3:     #delete Client
                getIdClients = self.customer_lineEdit_14.text()
                if getIdClients != '':
                    BackAnswer = QMessageBox.question( self, self.WarningTitle,self.PDelete,QMessageBox.Yes | QMessageBox.No, QMessageBox.No )
                    if BackAnswer == QMessageBox.Yes:
                        CMDSQL = """ DELETE FROM `customers` WHERE id_customer = '{}' """.format(int(getIdClients))
                        BackMsg = self.Tools.F_SQLGetManyOnlyCcommit(CMDSQL)
                        if BackMsg:
                            Proograms.LoadDataWidget(self)  # load listWidget Clients
                            Proograms.LoadAllDataClientsTabelWidget(self)  # load all service clients
                            self.statusbar.showMessage( 'تم الحذف بنجاح' )
                            self.ThreadAll('RemoveStatusBar')
                        else:
                            print( 'لم يتم الحذف يوجد مشكلة ' )
                    else:
                        pass
                else:
                    QMessageBox.about( self,self.WrongTitle, self.PSelectClient)
        except Exception as Error:
                Name_Function = 'class_proogram_Add_ClientsContral = '
                print( Name_Function, Error )
###################################################
    def Add_Clients(self):
        try:
            NewName = self.obj_Add_Client.customer_lineEdit_3.text()        #name clients
            NewPhone = self.obj_Add_Client.customer_lineEdit_4.text()       #phone clients
            NewEmail = self.obj_Add_Client.customer_lineEdit_5.text()       #emaile clients
            NewCountry = self.obj_Add_Client.customer_lineEdit_6.text()     #country clients
            NewDateTime = self.obj_Add_Client.customer_dateEdit.text()  #datetime start service clintes
            NewNote = self.obj_Add_Client.customer_textEdit.toPlainText()
            CheckNameInDb = Proograms.Client_chick( self, NewName )
            if CheckNameInDb:
                NewPhone = self.Tools.F_Encrypt(NewPhone,sessions.SyDb )
                NewEmail = self.Tools.F_Encrypt(NewEmail,sessions.SyDb )
                NewNote  = self.Tools.F_Encrypt(NewNote,sessions.SyDb )
                #### End encryption
                CMDSQL = """
                INSERT INTO `customers` 
                (name_customer,phone_customer,country_customer,email_customer,startservice_customer,note_customer) 
                VALUES ('{}','{}','{}','{}','{}','{}')
                """.format(NewName,NewPhone,NewCountry,NewEmail,NewDateTime,NewNote )
                BackMsseage = self.Tools.F_SQLGetManyOnlyCcommit(CMDSQL)
                if BackMsseage:
                    self.statusbar.showMessage( 'تم الاضافة بنجاح' )
                    self.ThreadAll('RemoveStatusBar')
                    self.customer_listWidget.addItem( NewName )
                    Proograms.LoadDataWidget( self )       #refresh list clients
                else:
                    print('لم يتم الاضافة يوجد مشكلة ')
            else:
                QMessageBox.about( self, self.WrongTitle, self.PHaveClient )
        except Exception as Error:
                Name_Function = 'class_proogram_Add_Clients = '
                print( Name_Function, Error )

    def Edite_Clients(self):
        try:
            idClient = int(self.customer_lineEdit_14.text())
            U_Name = self.obj_Edite.customer_lineEdit_3.text()  # name clients
            U_Phone = self.obj_Edite.customer_lineEdit_4.text()  # phone clients
            U_Email = self.obj_Edite.customer_lineEdit_5.text()  # emaile clients
            U_Country = self.obj_Edite.customer_lineEdit_6.text()  # country clients
            U_DateTime = self.obj_Edite.customer_dateEdit.text()  # datetime start service clintes
            U_Note = self.obj_Edite.customer_textEdit.toPlainText()
            CheckNameInDb = Proograms.Client_chick( self, U_Name )
            if CheckNameInDb == True or self.NameKnow == U_Name:  # smae name client
                U_Phone = self.Tools.F_Encrypt(U_Phone, sessions.SyDb )
                U_Email = self.Tools.F_Encrypt(U_Email, sessions.SyDb )
                U_Note = self.Tools.F_Encrypt(U_Note, sessions.SyDb )
                CMDSQL = """ UPDATE `customers`
                        SET name_customer = '{}' ,phone_customer = '{}' ,email_customer = '{}',
                        country_customer = '{}' ,note_customer = '{}' ,startservice_customer = '{}'
                        WHERE id_customer = '{}' 
                        """.format(U_Name, U_Phone, U_Email, U_Country, U_Note, U_DateTime, idClient)
                BackMsg = self.Tools.F_SQLGetManyOnlyCcommit(CMDSQL)
                if BackMsg:
                    self.statusbar.showMessage( 'تم التحديث بنجاح' )
                    Proograms.LoadDataWidget( self )
                    Proograms.LoadDataTabelWidget( self, idClient )
                    self.ThreadAll('RemoveStatusBar')
                else:
                    print('لم يتم التحديث توجد مشكلة')
            else:
                QMessageBox.about( self, self.WrongTitle, self.PHaveClient )
                pass
        except Exception as Error:
                Name_Function = 'class_proogram_Edite_Clients = '
                print( Name_Function, Error )

    def Client_chick(self,NewName):
        '''chike name Client dublecate not avalbial '''
        try:
            CMDSQL = """ SELECT `name_customer` FROM `customers` WHERE `name_customer` = '{}' """.format(NewName)
            Back = self.Tools.F_SQLGetManyOnlySelect(CMDSQL)
            if len(Back) != 0:
                return False
            else:
                return True
        except Exception as Error:
            Name_Function = 'class_proogram_Add_Client_chick = '
            print( Name_Function, Error )


###############################################################

###############################################################

class Alldialogs(StartClass,Lang):
    """ This class for rigth click in tabel for clients servics """
    def GetRightClickCmd(self,action):
        try:
            if action == 'AddService':
                self.obj = dialogDomain(self)
                getIdClients = self.customer_lineEdit_14.text()
                getNameSelect = self.customer_listWidget.currentItem()
                if getIdClients != '' and getNameSelect !=None:
                    self.obj.Domain_pushButton_Edite.hide()  #pushputton save
                    self.obj.Domain_pushButton.show()        #pushbutton Add
                    # id user
                    self.obj.Domain_lineEdit_7.setText(self.customer_lineEdit_14.text() )
                    # name user
                    self.obj.Domain_lineEdit_8.setText(str( getNameSelect.text() ) )
                    self.obj.Domain_pushButton.clicked.connect(lambda:Alldialogs.AddService(self))
                    self.obj.setWindowTitle( self.DSaddservice )
                    self.obj.setWindowIcon( QIcon( 'Icon/add_service.png' ) )
                    self.obj.exec_()
                    del self.obj
                else:
                    QMessageBox.about( self, self.WrongTitle, self.PSelectClient )
            elif action == 'Open':
                self.InfoRow = dialogDomain(self)
                self.InfoRow.Domain_pushButton.hide()
                self.InfoRow.Domain_pushButton_Edite.hide()
                RowSelect = self.customer_tableWidget.selectedItems()
                getIdClients = self.customer_lineEdit_14.text()
                getNameSelect = self.customer_listWidget.currentItem()
                if RowSelect !=[] and getIdClients != '':
                    idService = RowSelect[0].text()
                    NameService = RowSelect[1].text()
                    # id user
                    self.InfoRow.Domain_lineEdit_7.setText( self.customer_lineEdit_14.text() )
                    # name user
                    self.InfoRow.Domain_lineEdit_8.setText( str( getNameSelect.text() ) )
                    # id service
                    self.InfoRow.Domain_lineEdit.setText(RowSelect[0].text())
                    # name service
                    self.InfoRow.Domain_lineEdit_9.setText(RowSelect[1].text())
                    # Domain Name
                    GetText = RowSelect[2].text()
                    self.InfoRow.Domain_lineEdit_2.setText(str(GetText))
                    # Start Transfer Date
                    StartDateService = RowSelect[3].text()
                    ToObject1 = QDate.fromString( StartDateService,'yyyy-MM-dd')
                    self.InfoRow.Domain_dateEdit_4.setDate(ToObject1)
                    EndDateService = RowSelect[4].text()
                    ToObject2 = QDate.fromString( EndDateService, 'yyyy-MM-dd' )
                    self.InfoRow.Domain_dateEdit_5.setDate(ToObject2)
                    # End Transfer Date
                    # notes
                    GetText = RowSelect[5].text()
                    self.InfoRow.Domain_textEdit.setText(str(GetText))
                    self.InfoRow.Domain_lineEdit_23.setText(RowSelect[6].text())
                    self.InfoRow.Domain_lineEdit_24.setText(RowSelect[7].text())
                    #readonly
                    self.InfoRow.Domain_lineEdit_7.setReadOnly( True )  # id user
                    self.InfoRow.Domain_lineEdit_8.setReadOnly( True )  # name user
                    self.InfoRow.Domain_lineEdit.setReadOnly( True )  # id service
                    self.InfoRow.Domain_lineEdit_9.setReadOnly( True )  # name service
                    self.InfoRow.customer_comboBox.setDisabled(True)    #type Service
                    self.InfoRow.Domain_lineEdit_2.setReadOnly( True )  # #Domain Name
                    self.InfoRow.Domain_dateEdit_4.setReadOnly( True )  #Start Service
                    self.InfoRow.Domain_dateEdit_5.setReadOnly( True )  #End Service
                    self.InfoRow.Domain_textEdit.setReadOnly( True )  # notes
                    self.InfoRow.Domain_lineEdit_23.setReadOnly( True )  # notes
                    self.InfoRow.Domain_lineEdit_24.setReadOnly( True )  # notes
                    self.InfoRow.setWindowTitle( self.DSinfoservice )
                    self.InfoRow.setWindowIcon( QIcon( 'Icon/info_client.png' ) )
                    self.InfoRow.exec_()
                    del self.InfoRow
                else:
                    QMessageBox.about( self, self.WrongTitle, self.PSelectClient )

            elif action == 'Edite':
                self.obj_Edfit = dialogDomain(self)
                listLinecurreancy = [self.obj_Edfit.Domain_lineEdit_23, self.obj_Edfit.Domain_lineEdit_24]
                self.Tools.F_Line_curreancy(listLinecurreancy)    #get Regex pricess line
                listLineDomain= [self.obj_Edfit.Domain_lineEdit_2]
                self.Tools.F_Line_Domain(listLineDomain)          #ger Regex line domain
                self.obj_Edfit.Domain_pushButton.hide()
                self.obj_Edfit.Domain_pushButton_Edite.show()
                RowSelect = self.customer_tableWidget.selectedItems()
                getIdClients = self.customer_lineEdit_14.text()
                getNameSelect = self.customer_listWidget.currentItem()
                if RowSelect !=[] and getIdClients != '':
                    idService = RowSelect[0].text()
                    NameService = RowSelect[1].text()
                    # id user
                    self.obj_Edfit.Domain_lineEdit_7.setText( self.customer_lineEdit_14.text() )
                    # name user
                    self.obj_Edfit.Domain_lineEdit_8.setText( str( getNameSelect.text() ) )
                    # id service
                    self.obj_Edfit.Domain_lineEdit.setText(RowSelect[0].text())
                    # name service
                    self.obj_Edfit.Domain_lineEdit_9.setText(RowSelect[1].text())
                    # Domain Name
                    GetText = RowSelect[2].text()
                    self.obj_Edfit.Domain_lineEdit_2.setText(str(GetText))
                    # Start Transfer Date
                    StartDateService = RowSelect[3].text()
                    ToObject1 = QDate.fromString( StartDateService,'yyyy-MM-dd')
                    self.obj_Edfit.Domain_dateEdit_4.setDate(ToObject1)
                    EndDateService = RowSelect[4].text()
                    ToObject2 = QDate.fromString( EndDateService, 'yyyy-MM-dd' )
                    self.obj_Edfit.Domain_dateEdit_5.setDate(ToObject2)
                    # End Transfer Date

                    #note
                    GetText = RowSelect[5].text()
                    self.obj_Edfit.Domain_textEdit.setText(str(GetText))
                    self.obj_Edfit.Domain_lineEdit_23.setText(RowSelect[6].text())
                    self.obj_Edfit.Domain_lineEdit_24.setText(RowSelect[7].text())
                    self.obj_Edfit.Domain_pushButton_Edite.clicked.connect( lambda: Alldialogs.EditeService(self))
                    self.obj_Edfit.setWindowTitle( self.DSediteservice )
                    self.obj_Edfit.setWindowIcon( QIcon( 'Icon/edite_service.png' ) )
                    self.obj_Edfit.exec_()
                    del self.obj_Edfit
                else:
                    QMessageBox.about( self, self.WrongTitle, self.PSelectClient)
            elif action == 'delete':
                RowSelect = self.customer_tableWidget.selectedItems()
                getIdClients = self.customer_lineEdit_14.text()
                if RowSelect !=[] and getIdClients != '':
                    IdService = int(RowSelect[0].text())
                    BackAnswer = QMessageBox.question( self, self.WarningTitle, self.PDelete,QMessageBox.Yes | QMessageBox.No, QMessageBox.No )
                    if BackAnswer == QMessageBox.Yes:
                        CMDSQL = """DELETE FROM `service` WHERE id_service = '{}' """.format(IdService)
                        BackMsg = self.Tools.F_SQLGetManyOnlyCcommit(CMDSQL)
                        if BackMsg:
                            ReloadIdUser = int(self.customer_lineEdit_14.text())        #id Client
                            Proograms.LoadDataTabelWidget(self,ReloadIdUser)
                            self.statusbar.showMessage( 'تم الحذف بنجاح' )
                            self.ThreadAll('RemoveStatusBar')
                        else:
                            print('لايمكنك الحذف توجد مشكلة ')
                    else:
                        pass
                else:
                    QMessageBox.about( self, self.WrongTitle, self.PSelectClient)
        except Exception as Error:
                Name_Function = 'class_Alldialogs_GetRightClickCmd = '
                print( Name_Function, Error )

    def AddService( self):
        try:
            IdClients = int(self.obj.Domain_lineEdit_7.text())
            TypeService = self.obj.customer_comboBox.currentText()
            NameDomain =  self.obj.Domain_lineEdit_2.text()
            StarService = self.obj.Domain_dateEdit_4.text()
            EndService = self.obj.Domain_dateEdit_5.text()
            Info = self.obj.Domain_textEdit.toPlainText()
            PriceCompany = self.obj.Domain_lineEdit_23.text()
            PriceMe = self.obj.Domain_lineEdit_24.text()
            if NameDomain and PriceCompany and PriceMe  !='':
                NameDomain = self.Tools.F_Encrypt(NameDomain, sessions.SyDb )
                Info = self.Tools.F_Encrypt(Info, sessions.SyDb )
                CMDSQL = """ INSERT INTO `service`(typeService,name_domain,startservice,endservice,info_domain,
                priceCompany,priceMe,id_tabel_customer)
                VALUES ('{}','{}','{}','{}','{}',{},{},'{}')
                """.format(TypeService,NameDomain,StarService,EndService,Info,PriceCompany,PriceMe,IdClients)
                BackMsg = self.Tools.F_SQLGetManyOnlyCcommit(CMDSQL)
                if BackMsg:
                    Proograms.LoadDataTabelWidget(self,IdClients)
                    self.statusbar.showMessage( 'تم الاضافة بنجاح' )
                    self.ThreadAll('RemoveStatusBar')
                else:
                    print('لايمكنك الاضافة يوجد مشكلة ')
            else:
                print('حقل الدومين مطلوب')
        except Exception as Error:
                Name_Function = 'class_Alldialogs_AddService = '
                print( Name_Function, Error )

    def EditeService(self):
        try:
            idService = int( self.obj_Edfit.Domain_lineEdit.text() )
            U_TypeService = self.obj_Edfit.customer_comboBox.currentText()
            U_Domain = self.obj_Edfit.Domain_lineEdit_2.text()
            U_StartService = self.obj_Edfit.Domain_dateEdit_4.text()
            U_EndService = self.obj_Edfit.Domain_dateEdit_5.text()
            U_Info = self.obj_Edfit.Domain_textEdit.toPlainText()
            U_PriceCompany = self.obj_Edfit.Domain_lineEdit_23.text()
            U_Priceme = self.obj_Edfit.Domain_lineEdit_24.text()
            if U_Domain !='':
                U_Domain = self.Tools.F_Encrypt(U_Domain, sessions.SyDb )
                U_Info = self.Tools.F_Encrypt(U_Info, sessions.SyDb )
                CMDSQL = """ UPDATE `service` SET typeService = '{}' ,name_domain = '{}' ,startservice = '{}' ,
                endservice = '{}' ,info_domain = '{}' ,priceCompany ='{}' ,
                priceMe = '{}' 
                WHERE id_service = '{}'
                """.format(U_TypeService,U_Domain,U_StartService,U_EndService,U_Info,U_PriceCompany,U_Priceme,idService)
                BackMsg = self.Tools.F_SQLGetManyOnlyCcommit(CMDSQL)
                if BackMsg:
                    ReloadIdUser = int(self.obj_Edfit.Domain_lineEdit_7.text())
                    Proograms.LoadDataTabelWidget(self,ReloadIdUser)
                    self.statusbar.showMessage( 'تم التعديل بنجاح' )
                    self.ThreadAll('RemoveStatusBar')
                else:
                    print('لم يتم التعديل يوجد مشكلة')
            else:
                print('الرجاء كتابة اسم الدومين الحقول فاضية')
        except Exception as Error:
            Name_Function = 'class_Alldialogs_EditeService = '
            print( Name_Function, Error )

