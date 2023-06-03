# SciPy Integration https://docs.scipy.org/doc/scipy/tutorial/integrate.html

from scipy import integrate
from math import *
import termcolor


def integrate_expression(expression, a, b):
    """ 
    This function takes an expression, a lower bound a, and an upper bound b
    and calculates the integral of the expression over the interval [a, b].
    """

    try:

        def f(x):
            return eval(expression)

        result, error = integrate.quad(f, a, b)

        return result
    except:
        print("  error: could not evaluate expression.")
        return None


while True:
    expression = input("> ")
    if expression == "exit" or expression == "quit":
        break
    a = float(input("a: "))
    b = float(input("b: "))
    print()
    result = integrate_expression(expression, a, b)
    if result is not None:
        colored_result = termcolor.colored(result, "cyan")
        print("  " + colored_result)
    print()