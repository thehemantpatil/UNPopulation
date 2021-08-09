import pandas as pd
import matplotlib.pyplot as mt
import numpy as np

# Reading csv File.
pop_table = pd.read_csv('population.csv')
table = np.array(pop_table)
India = {}
South_Asian = {}
Saarc = {}
Grouped_Asian = {}

# this for loop is doing structurize data needed for plotting graph
for i in table:
    if(i[0] == "India"):
        India[i[2]] = i[-1]
    elif((i[0] == "Brunei Darussalam" and i[2] == 2014)
            or (i[0] == "Cambodia" and i[2] == 2014)
            or (i[0] == "Indonesia" and i[2] == 2014)
            or (i[0][0:3] == "Lao" and i[2] == 2014)
            or (i[0] == "Malaysia" and i[2] == 2014)
            or (i[0] == "Malaysia" and i[2] == 2014)
            or (i[0] == "Myanmar" and i[2] == 2014)
            or (i[0] == "Philippines" and i[2] == 2014)
            or (i[0] == "Singapore" and i[2] == 2014)
            or (i[0] == "Thailand" and i[2] == 2014)
            or (i[0] == "Viet Nam" and i[2] == 2014)):
        i1 = i[0].split(" ")
        South_Asian[i1[0]] = i[-1]
    elif(i[0] == "Southern Asia"):
        Saarc[i[2]] = i[-1]
    elif(i[0] == "ASIA" and 2004 <= i[2] < 2015):
        Grouped_Asian[i[2]] = i[-1]
    else:
        if(len(India.keys()) != 0 and len(South_Asian.keys()) != 0
           and len(Saarc.keys()) == 10 and len(Grouped_Asian.keys()) != 0):
            break
# Generate position for grouped bar
w = []
for i in range(len(Grouped_Asian.keys())):
    if(len(w) == 0):
        w.append(0)
    else:
        w.append(w[-1]+0.4)

# this section is plotting bar graph of indian population Vs year.
mt.subplot(221)
mt.title("India's Population Over Years")
mt.bar(India.keys(), India.values(), width=0.4)
mt.xlabel("Year")
mt.ylabel("Population in 10 lacks")

# this section is plotting bar graph of South Asian countries in year 2014.
mt.subplot(222)
mt.title("South Asian Counties Population of 2014")
mt.bar(South_Asian.keys(), South_Asian.values(), width=0.4)
mt.xlabel("Countries")
mt.xticks(rotation='vertical')
mt.ylabel("Population in lacks")

# this section is plotting bar graph of SAARC Countries Population Vs year.
mt.subplot(223)
mt.title("Saarc Countries Population Over Years")
mt.bar(Saarc.keys(), Saarc.values(), width=0.4)
mt.xlabel("years")
mt.ylabel("Population in 10 lacks")

'''
 this section is plotting grouped bar graph of Asian Countries
 between year 2004-2014.
'''

mt.subplot(224)
mt.title("Asian Countries")
color = ['red', 'blue', 'orange']
mt.bar(w, Grouped_Asian.values(), width=0.4, color=color)
mt.xlabel("Year 2004-2014")
mt.ylabel("Population in 10 lacks")

mt.tight_layout()
mt.show()
