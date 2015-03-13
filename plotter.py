#Functions take files and plots contents
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from pylab import savefig



#DECLARE FILE
filenumber = 41
text = 'positions/position_test%d.txt' % filenumber 

def Parameter_builder(text):
    file = open(text, 'r')
    lines = file.readlines()
    file.close()

    x = []
    y = []
    z = []
    v_x = []
    v_y = []
    v_z = []
    k = []
    for line in lines:
        line = line.strip('\n').split('	')
        x.append(line[0])
        y.append(line[1])
        z.append(line[2])
        v_x.append(line[3])
        v_y.append(line[4])
        v_z.append(line[5])
        k.append(line[6])
    
    return [x, y, z, v_x, v_y, v_z, k]

parameters = Parameter_builder(text)

x = parameters[0]
y = parameters[1]
z = parameters[2]
r = parameters[6]

#Radius
lo = []
for word in r:
    lo.append(float(word))
daphnis = lo.index(max(lo)) #Find Daphnis
n = lo.pop(daphnis)     #Remove Daphnis
l = np.array(lo)/max(lo) #Scale without Daphnis

#CONVERTING STRINGS TO FLOATS
i = []
for word in x:
    i.append(float(word))
i.pop(daphnis)

j = []
for word in y:
    j.append(float(word))
j.pop(daphnis)

k = []
for word in z:
    k.append(float(word))
k.pop(daphnis)

#Y VS X Graph (POSITION GRAPH)
cmap = plt.cm.autumn
fig = plt.figure(1)
ax = fig.add_subplot(111, aspect='equal')
ax.set_xlabel('Y positions')
ax.set_ylabel('X positions')
ax.set_title('Y vs X positions of particles')
ax.axis([min(j), max(j), 0, max(i)])

#Plot particles
for x, y, c, h in zip(j, i, l, l):
        ax.add_artist(Circle(xy=(x, y), radius = h, alpha = 0.5, color = cmap(c**2)))

#Plot Daphnis
ax.add_artist(Circle(xy=(0, 0), radius = n, alpha = 0.5, color = plt.cm.winter(0)))

#savefig('xyz_graphs/positions_YX_%d.png' % filenumber, bbox_inches='tight')



#Y VS Z GRAPH (WAKE GRAPH)
cmap = plt.cm.winter
fig = plt.figure(2)
ax = fig.add_subplot(111, aspect='equal')
ax.set_xlabel('Y positions')
ax.set_ylabel('Z positions')
ax.set_title('Azimuthal Displacement (Wakes)')
ax.axis([min(j), max(j), min(k) + min(k)/10, max(k)+max(k)/10])

#Plot particles
for x, y, c, h in zip(j, k, l, l):
    ax.add_artist(Circle(xy=(x, y), radius = h, alpha = 0.5, color = cmap(c**2)))

#Plot Daphnis
ax.add_artist(Circle(xy=(0, 0), radius = n, alpha = 0.5, color = plt.cm.autumn(0)))
                  
#savefig('xyz_graphs/positions_YZ_%d.png' % filenumber, bbox_inches='tight')
plt.show()

#print('***DONE*** Check xyz_graphs folder')

