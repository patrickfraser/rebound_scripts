#Functions take files and plots contents
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

filenumber = 35
text = 'positions/position_test%d.txt' % filenumber

def Vector_builder(text):
    file = open(text, 'r')
    lines = file.readlines()
    file.close()

    radius = []
    vector = []
    for line in lines:
        line = line.strip('\n').split('	')
        vector.append('<' + line[0] + ',' + line[1] + ',' + line[2] + '>')
        radius.append(line[6])
    
    return vector, radius

vector = Vector_builder(text)[0]
radius = Vector_builder(text)[1]

#l = []
#for word in vector:
#    l.append((word)[1:len(word)-1]

f = open( 'POVRay_texts/vector_%d.txt' % filenumber, 'w' )
for i in vector:
    f.write(i + ',')
f.close()

f = open( 'POVRay_texts/radius_%d.txt' % filenumber, 'w' )
for i in radius:
    f.write(i + ',')
f.close()
