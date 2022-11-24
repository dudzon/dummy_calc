from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty

Window.size = (500,700)

class MyLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calc_value = ''

    def clear(self):
        self.calc_value = '0'
        self.ids.calc_input.text = self.calc_value
    
    def on_button_press(self,button_value):

        if  self.calc_value == '0':
            self.calc_value = self.calc_value[1:]
        self.calc_value +=  str(button_value)
        print(self.calc_value,'calcValue')
        
        self.ids.calc_input.text = self.calc_value
        # print(calc_value,'calcValue')

    def add_math_symbol(self,sign) :
        self.calc_value += sign 
        self.ids.calc_input.text = self.calc_value

    def add_dot(self):
        if "." in self.ids.calc_input.text:
            pass
        else:
            self.calc_value += '.'
            self.ids.calc_input.text = self.calc_value

    def equals(self):
        addition_symbol = "+"

        # 1. Addition
        if addition_symbol in self.calc_value:
            str_list = self.calc_value.split(addition_symbol)
            num_list = list(map(int,str_list))
            result = sum(num_list)
            self.ids.calc_input.text = str(result)
            

        
        



class CalcApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalcApp().run()