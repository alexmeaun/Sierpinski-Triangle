import matplotlib.pyplot as plt
from random import choice

def trans1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1, y1

def trans2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    return x1,y1

def trans3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    return x1,y1
    
transformations = [trans1, trans2, trans3]
a1 = [0]
b1 = [0]
a = 0
b = 0

for i in range(10000000):
    trans = choice(transformations)
    a,b = trans((a,b))
    a1.append(a)
    b1.append(b)
    
plt.plot(a1, b1, '*')
    

    
    
    
    
    
    
    