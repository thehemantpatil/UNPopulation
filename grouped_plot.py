import solve
import matplotlib.pyplot as mt


def grouped():
    # Generate position for grouped bar
    w = []
    for i in range(len(solve.grouped_asian.keys())):
        if(len(w) == 0):
            w.append(0)
        else:
            w.append(w[-1]+0.4)

    '''
    this section is plotting grouped bar graph of Asian Countries
    between year 2004-2014.
    '''
    mt.subplot(224)
    mt.title("Asian Countries")
    color = ['red', 'blue', 'orange']
    mt.bar(w, solve.grouped_asian.values(), width=0.4, color=color)
    mt.xlabel("Year 2004-2014")
    mt.ylabel("Population in 10 lacks")
