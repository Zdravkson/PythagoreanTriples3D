from math import gcd
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def genTriples(k):
    n,m = 1,2
    while m*m+1<k:                  
        if n>=m: n,m = m%2,m+1      
        z = m*m+n*n                  
        if z >= k: n=m;continue     
        if gcd(n,m) == 1:           
            yield m*m-n*n,2*m*n,z   
        n += 2 

fig = plt.figure() 
ax = plt.axes(projection='3d')

xdata = []
ydata = []
zdata = []

triplesnum = 0

for x,y,z in genTriples(100):
    xdata.append(x)
    ydata.append(y)
    zdata.append(z)
    triplesnum += 1

print("Number of triples is: " + str(triplesnum))

ax.scatter3D(xdata, ydata, zdata)
plt.show()