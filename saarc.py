import matplotlib.pyplot as mt
import solve


# this section is plotting bar graph of saarc Countries Population Vs year.
def saarc():
    mt.subplot(223)
    mt.title("saarc Countries Population Over Years")
    mt.bar(solve.saarc.keys(), solve.saarc.values(), width=0.4)
    mt.xlabel("years")
    mt.ylabel("Population in 10 lacks")
