

from numpy import *

def difcost(a,b):
    dif=0

    for i in range(shape(a)[0]):
        for j in range(shape(a)[1]):
            dif+=pow(a[i,j]-b[i,j],2)

    return dif
