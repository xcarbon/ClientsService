import time
from Start_index import *
class C_Worker(QThread):
    SginalStatusBar = pyqtSignal(str)
    def __init__(self,args):
        super( C_Worker, self ).__init__()
        self.args = args

    def run(self):
        try:
            if self.args == 'RemoveStatusBar':
                self.RemoveStatusBar()
            elif self.args == 'Counter':
                self.Counter()

        except Exception as Error:
            Name_Function = 'Page_MyThread_run = '
            print( Name_Function, Error )

    @pyqtSlot(int)
    def Counter(self):
        try:
            x = 0
            while x <100:
                time.sleep(1)
                print(self.count)
                x +=1
        except Exception as Error:
            Name_Function = 'Page_MyThread_Counter = '
            print( Name_Function, Error )

    @pyqtSlot(str)
    def RemoveStatusBar(self):
        try:
            time.sleep(5)
            self.SginalStatusBar.emit('RemoveStatusBar')
        except Exception as Error:
            Name_Function = 'Page_MyThread_RemoveStatusBar = '
            print( Name_Function, Error )
    ############################################



