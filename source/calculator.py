"""
   A Class accept user input
   It return the arithmetic output
"""


class Calculator:
    def __init(self):
        pass

    def get_input(self):
        return input('Calculate: ')

    def calculate(self, parm):
        getvalue = eval(parm)
        print(getvalue)
        return getvalue


"""
getInput = Calculator.get_input('self')
Calculator().calculate(get_input)
"""
