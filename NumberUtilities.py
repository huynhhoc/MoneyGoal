import numpy as np
class NumberUtilities:
    @staticmethod
    def appendCommaBeforeDot(strNum):
        if strNum == "":
            return "0"
        num = float(strNum)
        flagNegative =""
        if num < 0:
            num = -1.0 * num
            flagNegative = "-"
        strNum = str(num)
        indexDot = strNum.index(".")
        indexAppend = indexDot - 3
        while indexAppend >= 1:
            strNum = strNum[:indexAppend] + ',' + strNum[indexAppend:]
            indexAppend = indexAppend - 3
        strNum = flagNegative + strNum
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
    @staticmethod
    def convertToMonth(num):
        if num == '1':
            return 'January'
        if num == '2':
            return 'February'
        if num == '3':
            return 'March'
        if num == '4':
            return 'April'
        if num == '5':
            return 'May'
        if num == '6':
            return 'June'
        if num == '7':
            return 'July'
        if num == '8':
            return 'August'
        if num == '9':
            return 'September'
        if num == '10':
            return 'October'
        if num == '11':
            return 'November'
        if num == '12':
            return 'December'
        else:
            pass