class NumberUtilities:
    @staticmethod
    def appendCommaBeforeDot(strNum):
        if strNum == "":
            return "0"
        indexDot = strNum.index(".")
        indexAppend = indexDot - 3
        while indexAppend >= 1:
            strNum = strNum[:indexAppend] + ',' + strNum[indexAppend:]
            indexAppend = indexAppend - 3
        return strNum
    @staticmethod
    def removeCommaToCaculate(strNum):
        if strNum == "":
            return "0"
        if "," in strNum:
            strNum = strNum.replace(",","")
        return strNum
    @staticmethod
    def convertNumberToDecimal(num):
        if num == "":
            return "0"
        strValue = num
        if "." not in strValue:
            strValue = strValue + ".00"
        if "," in strValue:
            return strValue
        else:
            return NumberUtilities.appendCommaBeforeDot(strValue)