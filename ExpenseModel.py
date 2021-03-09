import json
class ExpenseModel:
    jsonFile ='budget.json'
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
    def getIncomeMonthly(self, data):
        return self.data["IncomeMonthly"]
    def getExpenseMonthly(self, data):
        return self.data["ExpenseMonthly"]
    def getTotalProfit(self, data):
        return self.data["TotalProfit"]
    def getIncomeByMonth(self, month, data):
        return self.data[month]["Income"]
    def getExpenseByMonth(self, month, data):
        return self.data[month]["Expense"]
    def getRateExpenseByMonth(self, month, data):
        return self.data[month]["RateExpense"]
    def getProfitByMonth(self, month, data):
        return self.data[month]["Profit"]
    #Set
    def setIncomeMonthly(self, IncomeMonthly):
        try:
            self.data["IncomeMonthly"] = str(IncomeMonthly)
        except:
            print ('something wrong: ')
    def setExpenseMonthly(self, ExpenseMonthly):
        self.data["ExpenseMonthly"] = str(ExpenseMonthly)
    def setTotalProfit(self, TotalProfit):
        self.data["TotalProfit"] = str(TotalProfit)
    #def setIncomeByMonth(self, month):
    #    self.data[month]["Income"]
    #def setExpenseByMonth(self, month):
    #    self.data[month]["Expense"]
    def setRateExpenseByMonth(self, month,RateExpense):
        self.data[month]["RateExpense"] = str(RateExpense)
    def setProfitByMonth(self, month, Profit):
        self.data[month]["Profit"] = str(Profit)
    #Set