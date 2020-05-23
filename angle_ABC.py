import math
def length(AB,BC):
    ca = AB**2 + BC**2
    ca = math.sqrt(ca)
    tan = AB/BC
    k = math.atan(tan)
    l = math.degrees(k)
    val = str(int(round(l)))  +'°'
    return val
print(length(10,10))