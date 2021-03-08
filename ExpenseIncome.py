class ExpenseIncome:
    def __int__(self, id = 0, profit = 0, income = 0, expense = 0):
        self.profit = profit
        self.income = income
        self.expense = expense
        self.id = id
class Income:
    def __int__(self, money = 0, id = 0, description = 0):
        self.money = money
        self.id = id
        self.description =description
class Expense:
    def __int__(self, money = 0, id = 0, description = 0):
        self.money = money
        self.id = id
        self.description =description