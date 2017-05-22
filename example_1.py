# Edited by Jin Zhang
#Here I want to show two ways to extract the data 
# I want to get the following data from test.txt file
# 300 400 500 600 700
# 130 140 150 160 170
# 420 520 620 720 820
# 45.6 78.9 98.7 65.4 43.1
#####################

import numpy as np
#######################First way
m=[]
p=[]
with open ("example_1.txt") as test:
    data = test.readlines()
    length = len(data)
    for i in range(2,6):
        j = data[i]
        j = j.split()
        m.extend(j)
for i in range(len(m)):
    if not m[i].islower():
        k = m[i]
        k = k.split()
        p.extend(k)
k = np.asarray(p, dtype = np.float64)
k = k.reshape(4,6)
np.savetxt("output", k)
print(k)

#######################Second way
##m=[]
##p=[]
##with open ("example_1.txt") as test:
##    content = [x.rstrip() for x in test] # delete all the blank
##    n = content[2:6]   #display 3 to 6 row
##    for i in range(len(n)):
##        j = n[i]
##        h = j.split()
##        m.extend(h)
##for i in range(len(m)):
##    if not m[i].islower():
##        k = m[i]
##        k = k.split()
##        p.extend(k)
##k = np.asarray(p, dtype = np.float64)
##k = k.reshape(4,6)        
##np.savetxt("output", k)
##print(k)

        

