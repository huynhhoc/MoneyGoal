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
class MoneyGoalApp(App):
    #begin fields
    incomeMonthly =TextInput(multiline=False, halign= "right",input_type ="number", input_filter= "float",readonly=False,size_hint=(1, 1))
    expenseMonthly = TextInput(multiline=False, halign= "right", input_type = "number", input_filter= "float", readonly=False, size_hint=(1, 1))
    totalProfit = TextInput(multiline=False, halign= "right", readonly=True, size_hint=(1, 1))
    data = None
    # Create the screen manager
    sm = ScreenManager()
    mainScreen = Screen(name='main')
    editIncomeScreen = Screen(name='editIncome')
    editExpenseScreen = Screen(name='editExpense')
    currentMonth = "1"
    income_list = []
    expense_list = []
    rateExpense_list = []
    profit_list =[]
    #end fields
    #build GUI
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
        self.createScreenEdit(editIncome_layout, "income")
        self.editIncomeScreen.add_widget(editIncome_layout)
        #create Edit Income
        #create Edit Expense
        self.createScreenEdit(editExpense_layout,"expense")
        self.editExpenseScreen.add_widget(editExpense_layout)
        #create Edit Expense
        
        #loadData
        # TO-DO
        dataBudget = ExpenseModel('budget.json')
        dataBudget.loadBudget()
        self.data = dataBudget.data
        print (self.data["IncomeMonthly"])
        if self.data["IncomeMonthly"] !="":
            self.incomeMonthly.text = self.convertNumberToDecimal(self.data["IncomeMonthly"])
        #loadData
        
        #Create Screen Manager
        self.sm.add_widget(self.mainScreen)
        self.sm.add_widget(self.editIncomeScreen)
        self.sm.add_widget(self.editExpenseScreen)
        #Create Screen Manager
        return self.sm
    #end build GUI
    #begin methods
    def createScreenEdit(self, edit_layout, editType):
        self.createHeadingEdit(edit_layout, editType)
        self.createGridLayoutInput(edit_layout)
    def createHeadingEdit(self, edit_layout, editType):
        labMonth = Label(text="Chi tiêu tháng " + self.currentMonth + ":" + "editType: "+ editType)
        buttonLayout = BoxLayout()
        backButton = Button(text="<-", pos_hint ={"right":1}, label = "back")
        if editType =="expense":
            nextButton = Button(text="Home", pos_hint ={"right":1}, label = "home")
        else:
            nextButton = Button(text="->", pos_hint ={"right":1}, label = "next")
        buttonLayout.add_widget(labMonth)
        buttonLayout.add_widget(backButton)
        buttonLayout.add_widget(nextButton)
        edit_layout.add_widget(buttonLayout)
        edit_layout.add_widget(Button())
    def createGridLayoutInput(self, edit_layout):
        listDescription = []
        listMoney = []
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
        for index in range(0,15):
            row_layout = BoxLayout()
            labNo = Label(text = str(index+1), pos_hint={'x': 0, 'center_y': .5},size_hint=(0.1, 0.5))
            listDescription.append(TextInput(halign= "left", readonly= False, size_hint=(1, 1)))
            listMoney.append(TextInput(halign= "right", readonly= False, input_filter= "float", size_hint=(0.3, 1)))
            row_layout.add_widget(labNo)
            row_layout.add_widget(listDescription[index])
            row_layout.add_widget(listMoney[index])
            listMoney[index].bind(focus=self.on_focus)
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
            income = "1.00"
            self.incomeMonthly.text ="1.00"
        if expense == "":
            expense = "0.00"
            self.expenseMonthly.text ="0.00"
        incomeFloat = float(self.removeCommaToCaculate(income))
        expenseMonthly = float(self.removeCommaToCaculate(expense)) #incomeFloat*float(RateExpense)/100
        rateExpenseMonthly = np.round(expenseMonthly*100.0/incomeFloat)
        profitMontly = 0
        for index in range(0, len(self.income_list)-1):
            self.income_list[index].text = self.appendCommaBeforeDot(str(incomeFloat))
        for index in range (0,len(self.expense_list)-1):
            self.expense_list[index].text = self.appendCommaBeforeDot(str(expenseMonthly))
        for index in range (0,len(self.rateExpense_list)-1):
            self.rateExpense_list[index].text = str(rateExpenseMonthly)+"%"
        for index in range(0, len(self.profit_list)-1):
            profitMontly = profitMontly + (incomeFloat - expenseMonthly)
            self.profit_list[index].text = self.appendCommaBeforeDot(str(profitMontly))
    def caculateSummary(self):
        totalIncome = 0
        totalExpense = 0
        totalProfit = 0
        for indexIncome in range(0, len(self.income_list)-1):
            totalIncome += float(self.removeCommaToCaculate(self.income_list[indexIncome].text))
        for indexExpense in range (0,len(self.expense_list)-1):
            totalExpense += float(self.removeCommaToCaculate(self.expense_list[indexExpense].text))
        for indexProfit in range(0, len(self.profit_list)-1):
            totalProfit += float(self.removeCommaToCaculate(self.profit_list[indexProfit].text))
        self.income_list[indexIncome + 1].text = self.appendCommaBeforeDot(str(totalIncome))
        self.expense_list[indexExpense + 1].text = self.appendCommaBeforeDot(str(totalExpense))
        self.rateExpense_list[indexExpense + 1].text = str(np.round(totalExpense*100.0/totalIncome))+"%"
        self.profit_list[indexProfit + 1].text = self.profit_list[indexProfit].text
        self.totalProfit.text = self.profit_list[indexProfit].text
    def on_press_button(self, instance):
        print('You pressed the button! ', instance.text, "id: ", instance.label)
        if instance.label == "tinhtoan":
            self.caculateMonthly(self.incomeMonthly.text, self.expenseMonthly.text)
            self.caculateSummary()
            #update data
            dataBudget = ExpenseModel('budget.json')
            dataBudget.setIncomeMonthly(self.removeCommaToCaculate(self.incomeMonthly.text))
            dataBudget.updateBudget()
        elif instance.label =="back" or instance.label =="home":
            self.sm.switch_to(self.mainScreen, direction = 'left')
        elif instance.label =="next":

            self.sm.switch_to(self.editExpenseScreen)
        else:
            self.currentMonth = instance.label[instance.label.index("_")+1:]
            print ("self.currentMonth:", self.currentMonth)
            self.sm.switch_to(self.editIncomeScreen)
    def on_focus(self, instance, value):
        if value == False:
            instance.text = self.convertNumberToDecimal(instance.text)
        else:
            instance.text = self.removeCommaToCaculate(instance.text)
    def convertNumberToDecimal(self, num):
        strValue = num
        if "." not in strValue:
            strValue = strValue + ".00"
        if "," in strValue:
            return strValue
        else:
            return self.appendCommaBeforeDot(strValue)
    def appendCommaBeforeDot(self, strNum):
        indexDot = strNum.index(".")
        indexAppend = indexDot - 3
        while indexAppend >= 1:
            strNum = strNum[:indexAppend] + ',' + strNum[indexAppend:]
            indexAppend = indexAppend - 3
        return strNum
    def removeCommaToCaculate(self, strNum):
        if "," in strNum:
            strNum = strNum.replace(",","")
        return strNum
    #end methods
if __name__ == "__main__":
    app = MoneyGoalApp()
    app.run()
