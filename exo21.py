from math import pi, sin
from numpy import linspace
f = open('sine.csv', 'w', encoding='utf8')
for phi in linspace(0, 2 * pi, 100):
    s = f'{phi}, {sin(phi)}\n'
    # print(s)
    f.write(s)
f.close()
