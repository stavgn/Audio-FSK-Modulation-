class Payload:
    def __init__(self,text):
        self.rawData = str(text)
        self.bitArray = []
        self.__asciiArray = []
        self.bits_length = 0
        self.__Convert2BitsArray()

    def __split2Array(self):
        return list(self.rawData)

    def __ascii(self, char):
        return ord(char)

    def __Convert2BitsArray(self):
        string_array = self.__split2Array()
        self.__asciiArray = [self.__ascii(c) for c in string_array]
        for i in self.__asciiArray:
            for j in list("{0:08b}".format(i)):
                self.bitArray.append(int(j))
        self.bits_length = len(self.bitArray)

    def plotBinaryData(self):
        pass