import matplotlib.pyplot as mt
import solve


# this section is plotting bar graph of South Asian countries in year 2014.
def south():
    mt.subplot(222)
    mt.title("South Asian Counties Population of 2014")
    mt.bar(solve.south_asia.keys(), solve.south_asia.values(), width=0.4)
    mt.xlabel("Countries")
    mt.xticks(rotation='vertical')
    mt.ylabel("Population in lacks")
