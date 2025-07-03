from pkg.calculator import Calculator
from pkg.render import render

calculator = Calculator()
expression = "2 * 3 + 4"
result = calculator.evaluate(expression)
print(render(expression, result))