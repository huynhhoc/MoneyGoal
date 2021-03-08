from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

dropdownlist = DropDown()
options = 2
method = ['1.Chi tiêu tháng','2.Tổng tiết kiệm cuối năm']

for i in range(options):
    indiv_op = Button(text = method[i], size_hint_y = None, height = 30)
    indiv_op.bind(on_release = lambda indiv_op: dropdownlist.select(indiv_op.text))
    dropdownlist.add_widget(indiv_op)

mainMethod = Button(text ='1.Chi tiêu tháng', size_hint =(0.3, None),  height = 30)
mainMethod.bind(on_release = dropdownlist.open)

dropdownlist.bind(on_select = lambda instance, x: setattr(mainMethod, 'text', x))

print ("Ket qua: ",  mainMethod.text)
if __name__ == '__main__':
    runTouchApp(mainMethod)