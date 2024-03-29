import json
from NumberUtilities import NumberUtilities
class ExpenseModel:
    jsonFile ='budget.json'
    months = ['January', 'February', 'March','April', 'May', 'June', 'July', 'August','September','October','November','December']
    data = None
    def	__init__(self, jsonFile):
        self.jsonFile = jsonFile
        self.loadBudget()
    def loadBudget(self):
        with open(self.jsonFile) as json_file:
            self.data = json.load(json_file)
    def updateBudget(self):
        fileBudget = open(self.jsonFile, "w+")
        json.dump(self.data, fileBudget)
    def getIncomeMonthly(self):
        return self.data["IncomeMonthly"]
    def getExpenseMonthly(self):
        return self.data["ExpenseMonthly"]
    def getTotalProfit(self):
        return self.data["TotalProfit"]
    def getIncomeByMonth(self, month):
        return self.data[month]["Income"]
    def getExpenseByMonth(self, month):
        return self.data[month]["Expense"]
    def getRateExpenseByMonth(self, month):
        return self.data[month]["RateExpense"]
    def getProfitByMonth(self, month):
        return self.data[month]["Profit"]
    #
    def getIncomeByTotal(self):
        return self.data["Total"]["Income"]
    def getExpenseByTotal(self):
        return self.data["Total"]["Expense"]
    def getRateExpenseByTotal(self):
        return self.data["Total"]["RateExpense"]
    def getProfitByTotal(self):
        return self.data["Total"]["Profit"]
    #Set
    def setIncomeMonthly(self, IncomeMonthly):
        try:
            self.data["IncomeMonthly"] = str(IncomeMonthly)
        except:
            print ('something wrong: ')
    def setExpenseMonthly(self, ExpenseMonthly):
        try:
            self.data["ExpenseMonthly"] = str(ExpenseMonthly)
        except:
            print ('something wrong: ')
    def setTotalProfit(self, TotalProfit):
        try:
            self.data["TotalProfit"] = str(TotalProfit)
        except:
            print('something wrong: ')
    def setTotal_Income(self, income):
        try:
            self.data["Total"]["Income"] = str(income)
        except:
            print('something wrong: ')
    def setTotal_Expense(self, expense):
        try:
            self.data["Total"]["Expense"] = str(expense)
        except:
            print('something wrong: ')
    def setTotal_RateExpense(self, RateExpense):
        try:
            self.data["Total"]["RateExpense"] = str(RateExpense)
        except:
            print('something wrong: ')
    def setTotal_Profit(self, Profit):
        try:
            self.data["Total"]["Profit"] = str(Profit)
        except:
            print('something wrong: ')
    def setDetailProfit(self, income_list, expense_list, rateExpense_list, profit_list):
        for index, month in enumerate(self.months):
            self.setIncomeByMonth(month, income_list[index].text)
            self.setExpenseByMonth(month, expense_list[index].text)
            self.setRateExpenseByMonth(month, rateExpense_list[index].text)
            self.setProfitByMonth(month, profit_list[index].text)
        self.setTotalIncome(income_list[index+1].text)
        self.setTotalExpense(expense_list[index+1].text)
        self.setTotalRateExpense(rateExpense_list[index+1].text)
        self.setTotalProfitByYear(profit_list[index+1].text)
    def setIncomeByMonth(self, month, income):
        self.data[month]["Income"] = NumberUtilities.removeCommaToCaculate(income)
    def setExpenseByMonth(self, month, expense):
        self.data[month]["Expense"] = NumberUtilities.removeCommaToCaculate(expense)
    def setRateExpenseByMonth(self, month,RateExpense):
        self.data[month]["RateExpense"] = NumberUtilities.removeCommaToCaculate(RateExpense)
    def setProfitByMonth(self, month, Profit):
        self.data[month]["Profit"] = NumberUtilities.removeCommaToCaculate(Profit)
    def setTotalIncome(self,totalIncome):
            self.data["Total"]["Income"] = NumberUtilities.removeCommaToCaculate(totalIncome)
    def setTotalExpense(self, totalExpense):
        self.data["Total"]["Expense"] = NumberUtilities.removeCommaToCaculate(totalExpense)
    def setTotalRateExpense(self, TotalRateExpense):
        self.data["Total"]["RateExpense"] = NumberUtilities.removeCommaToCaculate(TotalRateExpense)
    def setTotalProfitByYear(self, TotalProfit):
        self.data["Total"]["Profit"] = NumberUtilities.removeCommaToCaculate(TotalProfit)
    #Set Detail Income by Month
    def getDetailIncomeByMonth(self, month):
        return self.data["DetailIncome"][month]
    def getDetailExpenseByMonth(self, month):
        return self.data["DetailExpense"][month]
    def setDetailIncomeByMonth(self, month, listDetailIncomeDescription, listDetailIncomeMoney):
        for index, item in enumerate(listDetailIncomeDescription):
            try:
                print ("Description: ", item.text)
                self.data["DetailIncome"][month][index]["Description"] = item.text
                self.data["DetailIncome"][month][index]["Money"] = listDetailIncomeMoney[index].text
            except:
                temp = {"Description": item.text, "Money":listDetailIncomeMoney[index].text}
                self.data["DetailIncome"][month].append(temp)
    def setDetailExpenseByMonth(self, month, listDetailExpenseDescription, listDetailExpenseMoney):
        for index, item in enumerate(listDetailExpenseDescription):
            try:
                print ("Description: ", item.text)
                self.data["DetailExpense"][month][index]["Description"] = item.text
                self.data["DetailExpense"][month][index]["Money"] = listDetailExpenseMoney[index].text
            except:
                temp = {"Description": item.text, "Money":listDetailExpenseMoney[index].text}
                self.data["DetailExpense"][month].append(temp)