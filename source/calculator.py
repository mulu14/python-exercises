"""
   A Class accept user input
   It return the arithmetic output
"""


class Calculator:
    def __init(self):
        pass

    def get_input(self):
        return input('Calculate: ')

    def calculate(self, param):
        getvalue = eval(param)
        print(getvalue)
        return getvalue


"""
get_input = Calculator.get_input('self')
Calculator().calculate(get_input)
"""
