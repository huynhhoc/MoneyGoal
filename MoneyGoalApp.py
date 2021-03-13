from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.core.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import numpy as np
import json
from ExpenseModel import ExpenseModel
from NumberUtilities import NumberUtilities
from HelperUtilities import HelperUtilities
class MoneyGoalApp(App):
    #begin fields
    #Data on the main screen
    incomeMonthly =TextInput(multiline=False, halign= "right",input_type ="number", input_filter= "float",readonly=False,size_hint=(1, 1))
    expenseMonthly = TextInput(multiline=False, halign= "right", input_type = "number", input_filter= "float", readonly=False, size_hint=(1, 1))
    totalProfit = TextInput(multiline=False, halign= "right", readonly=True, size_hint=(1, 1))
    income_list = []
    expense_list = []
    rateExpense_list = []
    profit_list =[]
    #end data on the main screen
    # Data on the detail income screen based on currentlyMonth, these variables will be reset and load 
    # when you need to move to other month
    listDetailIncomeDescription = []
    listDetailIncomeMoney = []
    #Data on the detail expense screen based on currentlyMonth, these variables will be reset and load 
    # when you need to move to other month
    listDetailExpenseDescription = []
    listDetailExpenseMoney = []
    #
    currentMonth = "1"
    dataBudget = None #data load from budget.json
    data = None
    labelIncomeMonthly = Label(text="Thu nhập tháng ")
    labelExpenseMonthly = Label(text="Chi tiêu tháng ")
    #end fields
    # Create the screen manager
    sm = ScreenManager()
    mainScreen = Screen(name='main')
    editIncomeScreen = Screen(name='editIncome')
    editExpenseScreen = Screen(name='editExpense')
    #build GUI
    #resetDetailIncome is used to reset listDetailIncome Descrition and Money when you switch to other month
    # you need to call load DetailIncome from budget after reset these variables.
    def resetDetailIncome(self):
        for index in range(0, len(self.listDetailIncomeDescription)):
            self.listDetailIncomeDescription[index].text = ""
            self.listDetailIncomeMoney[index].text = ""
    def resetDetailExpense(self):
        for index  in range(0, len(self.listDetailExpenseDescription)):
            self.listDetailExpenseDescription[index].text = ""
            self.listDetailExpenseMoney[index].text = ""
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        editIncome_layout = BoxLayout(orientation="vertical")
        editExpense_layout = BoxLayout(orientation="vertical")
        
        #create GUI for main layout
        self.createSection1(main_layout)
        self.createHeadingGridDetails(main_layout)
        self.createGridDetails(main_layout)
        self.mainScreen.add_widget(main_layout)
        #create GUI for main layout
        
        #create Edit Income
        self.createScreenEdit(editIncome_layout, HelperUtilities.IncomeType)
        self.editIncomeScreen.add_widget(editIncome_layout)
        #create Edit Income
        #create Edit Expense
        self.createScreenEdit(editExpense_layout,HelperUtilities.ExpenseType)
        self.editExpenseScreen.add_widget(editExpense_layout)
        #create Edit Expense
        
        #loadData
        self.loadDataToMainScreen(HelperUtilities.DataSource)
        #self.loadDataToIncomeScreen(HelperUtilities.DataSource)
        #self.loadDataToExpenseScreen(HelperUtilities.DataSource)
        #loadData
        #Create Screen Manager
        self.sm.add_widget(self.mainScreen)
        self.sm.add_widget(self.editIncomeScreen)
        self.sm.add_widget(self.editExpenseScreen)
        #Create Screen Manager
        return self.sm
    #end build GUI
    #begin methods
    def loadDataToMainScreen(self, jsonData):
        self.dataBudget = ExpenseModel(jsonData)
        self.data = self.dataBudget.data
        if self.data["IncomeMonthly"] !="":
            self.incomeMonthly.text = NumberUtilities.convertNumberToDecimal(self.data["IncomeMonthly"])
        if self.data["ExpenseMonthly"] !="":
            self.expenseMonthly.text = NumberUtilities.convertNumberToDecimal(self.data["ExpenseMonthly"])
        if self.data["TotalProfit"] !="":
            self.totalProfit.text = NumberUtilities.convertNumberToDecimal(self.data["TotalProfit"])
        for index, month in enumerate(ExpenseModel.months):
            self.income_list[index].text = NumberUtilities.appendCommaBeforeDot(self.dataBudget.getIncomeByMonth(month))
            self.expense_list[index].text = NumberUtilities.appendCommaBeforeDot(self.dataBudget.getExpenseByMonth(month))
            self.rateExpense_list[index].text = self.dataBudget.getRateExpenseByMonth(month)
            self.profit_list[index].text = NumberUtilities.appendCommaBeforeDot(self.dataBudget.getProfitByMonth(month))
        self.income_list[index + 1].text = NumberUtilities.appendCommaBeforeDot(self.dataBudget.getIncomeByTotal())
        self.expense_list[index + 1].text = NumberUtilities.appendCommaBeforeDot(self.dataBudget.getExpenseByTotal())
        self.rateExpense_list[index + 1].text = self.dataBudget.getRateExpenseByTotal()
        self.profit_list[index + 1].text = NumberUtilities.appendCommaBeforeDot(self.dataBudget.getProfitByTotal())
    def loadDataToIncomeScreen(self, month):
        detailIncomeByMonth = self.dataBudget.getDetailIncomeByMonth(NumberUtilities.convertToMonth(month))
        try:
            for index in range(0,len(self.listDetailIncomeDescription)):
                self.listDetailIncomeDescription[index].text = detailIncomeByMonth[index]["Description"]
                self.listDetailIncomeMoney[index].text = detailIncomeByMonth[index]["Money"]
        except:
            pass
    def loadDataToExpenseScreen(self, month):
        detailExpenseByMonth = self.dataBudget.getDetailExpenseByMonth(NumberUtilities.convertToMonth(month))
        try:
            for index in range(0,len(self.listDetailExpenseDescription)):
                self.listDetailExpenseDescription[index].text = detailExpenseByMonth[index]["Description"]
                self.listDetailExpenseMoney[index].text = detailExpenseByMonth[index]["Money"]
        except:
            pass
    def createScreenEdit(self, edit_layout, editType):
        self.createHeadingEdit(edit_layout, editType)
        self.createGridLayoutInput(edit_layout, editType)
    def createHeadingEdit(self, edit_layout, editType):
        buttonLayout = BoxLayout()
        backButton = Button(text="<-", pos_hint ={"right":1}, label = "back")
        if editType ==HelperUtilities.ExpenseType:
            nextButton = Button(text="Home", pos_hint ={"right":1}, label = "home")
            self.labelExpenseMonthly.text = "Chi tiêu tháng "
            buttonLayout.add_widget(self.labelExpenseMonthly)
        else:
            nextButton = Button(text="->", pos_hint ={"right":1}, label = "next")
            self.labelIncomeMonthly.text = "Thu nhập tháng "
            buttonLayout.add_widget(self.labelIncomeMonthly)
        buttonLayout.add_widget(backButton)
        buttonLayout.add_widget(nextButton)
        edit_layout.add_widget(buttonLayout)
        edit_layout.add_widget(Button(label=editType))
    def createGridLayoutInput(self, edit_layout, editType):
        labelTitle =["STT", "Mô tả", "Số tiền"]
        gridLayout = BoxLayout()
        row_layoutLabel = BoxLayout()
        for index, col in enumerate(labelTitle):
            if index == 0:
                labItem = Label(text=col, pos_hint={'x': 0, 'center_y': .5},size_hint=(0.1, 0.5))
            elif index == 1:
                labItem = Label(text=col, size_hint=(1, 1))
            else:
                labItem = Label(text=col, size_hint=(0.3, 1))
            row_layoutLabel.add_widget(labItem)
        gridLayout.add_widget(row_layoutLabel)
        edit_layout.add_widget(gridLayout)
        if editType == HelperUtilities.IncomeType:
            self.addDetailInputToGridLayout(edit_layout, self.listDetailIncomeDescription,self.listDetailIncomeMoney,editType)
        else:
            self.addDetailInputToGridLayout(edit_layout, self.listDetailExpenseDescription,self.listDetailExpenseMoney, editType)
    def addDetailInputToGridLayout(self, edit_layout, listDescription,listMoney, editType):
        for index in range(0,15):
            row_layout = BoxLayout()
            labNo = Label(text = str(index+1), pos_hint={'x': 0, 'center_y': .5},size_hint=(0.1, 0.5))
            if index ==0:
                listDescription.append(TextInput(text = "Tổng", halign= "left", readonly= False, size_hint=(1, 1)))
                listMoney.append(TextInput(halign= "right", readonly= True, input_filter= "float", size_hint=(0.3, 1)))
            else:
                listDescription.append(TextInput(halign= "left", readonly= False, size_hint=(1, 1)))
                listMoney.append(TextInput(halign= "right", readonly= False, input_filter= "float", size_hint=(0.3, 1)))
            if editType == HelperUtilities.IncomeType:
                listMoney[index].bind(focus=self.on_focusUpdateIncome)
            else:
                listMoney[index].bind(focus=self.on_focusUpdateExpense)
            row_layout.add_widget(labNo)
            row_layout.add_widget(listDescription[index])
            row_layout.add_widget(listMoney[index])
            edit_layout.add_widget(row_layout)
    def createSection1(self, main_layout):
        #income
        h_layoutIncome = BoxLayout()
        lblIncome = Label(text ="Thu nhập: ")
        h_layoutIncome.add_widget(lblIncome)
        h_layoutIncome.add_widget(self.incomeMonthly)
        self.incomeMonthly.bind(focus=self.on_focus)
        #chitieu
        lblChitieu = Label(text ="Dự kiến chi theo tháng: ")
        h_layoutIncome.add_widget(lblChitieu)
        h_layoutIncome.add_widget(self.expenseMonthly)
        self.expenseMonthly.bind(focus=self.on_focus)
        #tietkiem
        h_layoutTietkiem = BoxLayout(spacing=30)
        lblsave = Label(text ="Khoảng tiết kiệm cuối năm: ")
        h_layoutTietkiem.add_widget(lblsave)
        h_layoutTietkiem.add_widget(self.totalProfit)
        #main_layout.add_widget()
        buttonTT = Button()
        main_layout.add_widget(h_layoutIncome)
        main_layout.add_widget(h_layoutTietkiem)
        main_layout.add_widget(buttonTT)
    def createHeadingGridDetails(self, main_layout):
        labelTitle =["Tháng", "Thu nhập",  "Chi tiêu", "%Chi tiêu", "Tiết kiệm", "Cập nhật"]
        h_layoutLabel = BoxLayout()
        for col in labelTitle:
            labItem = Label(text=col)
            h_layoutLabel.add_widget(labItem)
        main_layout.add_widget(h_layoutLabel)
    def createBoxLayout(self, monthly, index, lbel):
        h_layoutLabel = BoxLayout()
        labMonth = Label(text=monthly)
        incomeMonth = TextInput()
        expenseMonth = TextInput()
        rateExpenseMonth = TextInput()
        profitMonth = TextInput()
        buttonUpdate = Button(
                    text=lbel,
                    label = "edit_"+str(index + 1),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
        self.income_list.append(incomeMonth)
        self.expense_list.append(expenseMonth)
        self.rateExpense_list.append(rateExpenseMonth)
        self.profit_list.append(profitMonth)
        h_layoutLabel.add_widget(labMonth)
        h_layoutLabel.add_widget(self.income_list[index])
        h_layoutLabel.add_widget(self.expense_list[index])
        h_layoutLabel.add_widget(self.rateExpense_list[index])
        h_layoutLabel.add_widget(self.profit_list[index])
        h_layoutLabel.add_widget(buttonUpdate)
        return h_layoutLabel
    def createGridDetails(self, main_layout):
        monthly = ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4","Tháng 5", "Tháng 6", "Tháng 7", "Tháng 8","Tháng 9", "Tháng 10", "Tháng 11", "Tháng 12"]
        for index, month in enumerate(monthly):
            layoutRow = self.createBoxLayout(month, index, "Sửa")
            main_layout.add_widget(layoutRow)
        layoutRow = self.createBoxLayout("Tổng", index+1, "Xuất")
        main_layout.add_widget(layoutRow)
    def caculateMonthly(self, income, expense):
        if income == "":
            income = "0.00"
            self.incomeMonthly.text ="0.00"
        if expense == "":
            expense = "0.00"
            self.expenseMonthly.text ="0.00"
        incomeFloat = float(NumberUtilities.removeCommaToCaculate(income))
        expenseMonthly = float(NumberUtilities.removeCommaToCaculate(expense))
        if incomeFloat == 0.0:
            rateExpenseMonthly ="N/A"
        else:
            rateExpenseMonthly = np.round(expenseMonthly*100.0/incomeFloat)
        profitMontly = 0
        for index in range(0, len(self.income_list)-1):
            self.income_list[index].text = NumberUtilities.appendCommaBeforeDot(str(incomeFloat))
        for index in range (0,len(self.expense_list)-1):
            self.expense_list[index].text = NumberUtilities.appendCommaBeforeDot(str(expenseMonthly))
        for index in range (0,len(self.rateExpense_list)-1):
            self.rateExpense_list[index].text = str(rateExpenseMonthly)+"%"
        for index in range(0, len(self.profit_list)-1):
            profitMontly = profitMontly + (incomeFloat - expenseMonthly)
            self.profit_list[index].text = NumberUtilities.appendCommaBeforeDot(str(profitMontly))
    def saveDataSection1(self):
        self.dataBudget.setIncomeMonthly(NumberUtilities.removeCommaToCaculate(self.incomeMonthly.text))
        self.dataBudget.setExpenseMonthly(NumberUtilities.removeCommaToCaculate(self.expenseMonthly.text))
        self.dataBudget.updateBudget()
    def caculateSummary(self):
        totalIncome = 0
        totalExpense = 0
        totalProfit = 0
        for indexIncome in range(0, len(self.income_list)-1):
            totalIncome += float(NumberUtilities.removeCommaToCaculate(self.income_list[indexIncome].text))
        for indexExpense in range (0,len(self.expense_list)-1):
            totalExpense += float(NumberUtilities.removeCommaToCaculate(self.expense_list[indexExpense].text))
        for indexProfit in range(0, len(self.profit_list)-1):
            totalProfit += float(NumberUtilities.removeCommaToCaculate(self.profit_list[indexProfit].text))
        self.income_list[indexIncome + 1].text = NumberUtilities.appendCommaBeforeDot(str(totalIncome))
        self.expense_list[indexExpense + 1].text = NumberUtilities.appendCommaBeforeDot(str(totalExpense))
        self.rateExpense_list[indexExpense + 1].text = str(np.round(totalExpense*100.0/totalIncome))+"%"
        self.profit_list[indexProfit + 1].text = self.profit_list[indexProfit].text
        self.totalProfit.text = self.profit_list[indexProfit].text
    def updateDataMainScreen(self, jsonFile):
        self.dataBudget.setIncomeMonthly(NumberUtilities.removeCommaToCaculate(self.incomeMonthly.text))
        self.dataBudget.setExpenseMonthly(NumberUtilities.removeCommaToCaculate(self.expenseMonthly.text))
        self.dataBudget.setTotalProfit(NumberUtilities.removeCommaToCaculate(self.totalProfit.text))
        self.dataBudget.setDetailProfit(self.income_list, self.expense_list, self.rateExpense_list, self.profit_list)
        self.dataBudget.updateBudget()
    def caculateProfitbyMonth(self, month, income, expense):
        income = float(NumberUtilities.removeCommaToCaculate(income))
        expense = float(NumberUtilities.removeCommaToCaculate(expense))
        profit = income - expense
        if income == 0.0:
            rate ="N/A"
        else:
            rate   = np.round(expense*100.0/income)
        return str(rate), str(profit)
    def onChangeDatebyMonth(self, month):
        rateExpense, profit = self.caculateProfitbyMonth(month, self.listDetailIncomeMoney[0].text, self.listDetailExpenseMoney[0].text)
        self.dataBudget.setProfitByMonth(month, profit)
        self.dataBudget.setIncomeByMonth(month, self.listDetailIncomeMoney[0].text)
        self.dataBudget.setExpenseByMonth(month, self.listDetailExpenseMoney[0].text)
        self.dataBudget.setRateExpenseByMonth(month, rateExpense)
        self.profit_list[ExpenseModel.months.index(month)].text = NumberUtilities.appendCommaBeforeDot(profit)
        self.rateExpense_list[ExpenseModel.months.index(month)].text = rateExpense + "%"
        self.caculateSummary()
        self.dataBudget.setTotalProfit()
    def updateDetailIncomeByMonth(self, month):
        self.dataBudget.setDetailIncomeByMonth(month, self.listDetailIncomeDescription, self.listDetailIncomeMoney)
        self.onChangeDatebyMonth(month)
        self.dataBudget.updateBudget()
    def updateDetailExpenseByMonth(self, month):
        self.dataBudget.setDetailExpenseByMonth(month, self.listDetailExpenseDescription, self.listDetailExpenseMoney)
        self.onChangeDatebyMonth(month)
        self.dataBudget.updateBudget()
    def on_press_button(self, instance):
        print('You pressed the button! ', instance.text, "id: ", instance.label)
        if instance.label == "tinhtoan":
            self.caculateMonthly(self.incomeMonthly.text, self.expenseMonthly.text)
            self.caculateSummary()
            self.updateDataMainScreen(HelperUtilities.DataSource)
        elif instance.label =="back" or instance.label =="home":
            self.sm.switch_to(self.mainScreen, direction = 'left')
        elif instance.label =="next":
            self.resetDetailExpense()
            self.loadDataToExpenseScreen(self.currentMonth)
            self.sm.switch_to(self.editExpenseScreen)
        elif instance.label == HelperUtilities.IncomeType:
            self.updateDetailIncomeByMonth(NumberUtilities.convertToMonth(self.currentMonth))
        elif instance.label == HelperUtilities.ExpenseType:
            self.updateDetailExpenseByMonth(NumberUtilities.convertToMonth(self.currentMonth))
        else: #Switch to Edit Income
            self.currentMonth = instance.label[instance.label.index("_")+1:]
            self.labelIncomeMonthly.text = "Thu nhập tháng " + self.currentMonth
            self.labelExpenseMonthly.text = "Chi tiêu tháng "+ self.currentMonth
            self.resetDetailIncome()
            self.loadDataToIncomeScreen(self.currentMonth)
            self.sm.switch_to(self.editIncomeScreen)
    def on_focusUpdateIncome(self, instance, value):
        self.changeOnFocus(instance, value)
        totalIncome = 0
        for index, item in enumerate(self.listDetailIncomeMoney):
            if index > 0:
                totalIncome += float(NumberUtilities.removeCommaToCaculate(item.text))
        self.listDetailIncomeMoney[0].text = NumberUtilities.convertNumberToDecimal(str(totalIncome))
        self.income_list[int(self.currentMonth)-1].text = self.listDetailIncomeMoney[0].text
    def on_focusUpdateExpense(self, instance, value):
        self.changeOnFocus(instance, value)
        totalExpense = 0
        for index, item in enumerate(self.listDetailExpenseMoney):
            if index > 0:
                totalExpense += float(NumberUtilities.removeCommaToCaculate(item.text))
        self.listDetailExpenseMoney[0].text = NumberUtilities.convertNumberToDecimal(str(totalExpense))
        self.expense_list[int(self.currentMonth)-1].text = self.listDetailExpenseMoney[0].text
    def changeOnFocus(self, instance, value):
        if value == False:
            instance.text = NumberUtilities.convertNumberToDecimal(instance.text)
        else:
            instance.text = NumberUtilities.removeCommaToCaculate(instance.text)
    def on_focus(self, instance, value):
        self.changeOnFocus(instance, value)
    #end methods
if __name__ == "__main__":
    app = MoneyGoalApp()
    app.run()
