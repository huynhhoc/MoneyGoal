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
        try:
            self.data["ExpenseMonthly"] = str(ExpenseMonthly)
        except:
            print ('something wrong: ')
    def setTotalProfit(self, TotalProfit):
        try:
            self.data["TotalProfit"] = str(TotalProfit)
        except:
            print('something wrong: ')

    def setDetailProfit(self, income_list, expense_list, rateExpense_list, profit_list):
        months = ['January', 'February', 'March','April', 'May', 'June', 'July', 'August','September','October','November','December']
        for index, month in enumerate(months):
            self.setIncomeByMonth(month, income_list[index].text)
            self.setExpenseByMonth(month, expense_list[index].text)
            self.setRateExpenseByMonth(month, rateExpense_list[index].text)
            self.setProfitByMonth(month, profit_list[index].text)
        self.setTotalIncome(income_list[index+1].text)
        self.setTotalExpense(expense_list[index+1].text)
        self.setTotalRateExpense(rateExpense_list[index+1].text)
        self.setTotalProfit(profit_list[index+1].text)
    def setIncomeByMonth(self, month, income):
        self.data[month]["Income"] = str(income)
    def setExpenseByMonth(self, month, expense):
        self.data[month]["Expense"] = str(expense)
    def setRateExpenseByMonth(self, month,RateExpense):
        self.data[month]["RateExpense"] = str(RateExpense)
    def setProfitByMonth(self, month, Profit):
        self.data[month]["Profit"] = str(Profit)
    def setTotalIncome(self,totalIncome):
            self.data["Total"]["Income"] = str(totalIncome)
    def setTotalExpense(self, totalExpense):
        self.data["Total"]["Expense"] = str(totalExpense)
    def setTotalRateExpense(self, TotalRateExpense):
        self.data["Total"]["RateExpense"] = str(TotalRateExpense)
    def setTotalProfit(self, TotalProfit):
        self.data["Total"]["Profit"] = str(TotalProfit)
    #Set