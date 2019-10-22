class kyserText():
    def keydic(self,key):
        AAr = 'أؤإNثرVWذXزىيAسDEـفهFGHضطظؿIJKLOقكwلMمنPQRSعغxyػؼؽؾTUYZئاBبةتabcجحdefghijklmnopqrخCدsuشصtوvz'
        #AAr2 = 'ءًٌٍَُِّْٕٔٓ٭ٴٰٯٵٷٸٹٺڀٿپٽٻځڂڃڄڅچڌڋڊډڈڇڍڎڏڐڑڒژڗږڕڔړڙښڛڜڝڞڤڣڢڡڠڟڥڦڧڨکڪڰگڮڭڬګڱڲڳڴڵڶڼڻںڹڸڷڽھڿۀہۂۈۇۆۅۄۃۉۊۋیۍێۓےۑېۏۖۗۘۙۚ۠۟۞۝ۣۜۛۡۢۤۥۦ۪۬۫۩ۭۨۧ۴ۺ۶۵ۻۼ۽۾ﹰﹱﹹﹸﹷﹶﹴﹲﹺﹻﹼﹽﹾﹿﺅﺋﺆﺈﻌﻋﻊﻐ'
        AAr3 = '0123456789٠١٢٣٤٥٦٧٨٩ '
        #AAr4 = string.punctuation
        CharAr = AAr + AAr3 #+ AAr4  + AAr2
        #AAr2 = 'ABCDEFGHذرزسشصضطظعغػؼؽؾؿـفقكلمنهوىيIJKLMNOPQRSTUVأؤإئابةتثجحخدWXYZabcdefghijklmnopqrstuvwxyz'
        # print(AAr)
        Counts = len(CharAr) -1
        res = {}
        for e in CharAr:
            res[e] = CharAr[key]
            key += 1
            if key > Counts:
                key = 0
        return res
    def Encrypt(self, Mytext, dic):
        CodeText = ''
        for i in Mytext:
            if i == '\n' or i not in dic:  # or i in Nu or i in NuAr or i == " "
                CodeText += i
            else:
                CodeText += dic[i]
        return CodeText
    def decryptText(self,Text,key):
        codeText = Text

        dic = self.keydic(-key)
        T = self.Encrypt(codeText,dic)
        return T

