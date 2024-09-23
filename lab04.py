import math as M
import random as R
def calculate(x):
    y=M.exp(x**2)/M.cos(x+x**4)-(x+x**3)**(1/4)
    return y
print(calculate(R.randrange(1,10)))