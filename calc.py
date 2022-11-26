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
        self.ids.calc_input.text = self.calc_value

    def add_math_symbol(self,sign) :
        self.calc_value += sign 
        self.ids.calc_input.text = self.calc_value

    def add_dot(self):
        symbols = list(['+','-','/','*','**'])

        # Block the possibility to add second dot in fraction
        # Test more to check if this logic really works.

        for symbol in symbols:
            # If symbol is used split the string by symbol

            if symbol in self.calc_value:
                current_values = self.calc_value.split(symbol)

                # If fraction is used do not add second dot
                if symbol in self.calc_value and not '.' in current_values[-1]:
                    self.calc_value += '.'

            elif "." in self.calc_value:
                pass
            else:
                self.calc_value += '.'
            
        self.ids.calc_input.text = self.calc_value

    def remove_last_char(self):
        current_value_list = list(self.ids.calc_input.text)
        current_value_list.pop()
        self.ids.calc_input.text = ''.join(current_value_list)
        # or self.ids.calc_input.text = self.ids.calc_input.text[:-1] ???
        if not len(current_value_list):
              self.clear()

    def make_positive_or_negative(self):
        if "-" in self.calc_value:
            self.calc_value = self.calc_value[1:]
        else:
            self.calc_value = '-' + self.calc_value

        self.ids.calc_input.text = self.calc_value

    def equals(self):
        try:
            self.evaluate(False)
        except:
            self.clear()
        

    def formatResult(self,number):
        if number % 1 == 0:
            return int(number)
        else:
            return number 

    def get_percentage(self):
        if '*' in self.calc_value:
            self.evaluate(True)
        
        else:
            self.clear()

    def evaluate(self,percentage):
        current_value = ''
        result = ''

        if percentage:
            current_value = eval(self.calc_value)
            result = int(current_value)/100
        else:
            result = eval(self.calc_value)

        result = self.formatResult(result)
        self.calc_value = str(result)
        self.ids.calc_input.text = self.calc_value

class CalcApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalcApp().run()