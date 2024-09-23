import math as M
import random as R
def calculate(x,y,a,t):
    Z=M.pi*2.33*(x*M.sin(y)+y*M.cos(a))+M.exp(a**t)
    return Z
x=R.randrange(1,10)
y=R.randrange(2,8)
a=R.randrange(3,7)
t=R.randrange(4,6)
print(calculate(x,y,a,t))