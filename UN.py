import matplotlib.pyplot as mt
import csv
# Reading csv File.
# pop_table = pd.read_csv('population.csv')
# table = np.array(pop_table)
india = {}
south_asia = {}
saarc = {}
grouped_asian = {}


def main():
    with open('population.csv') as pop_table:
        table = csv.reader(pop_table)

        # this for loop is doing structurize data needed for plotting graph
        for i in table:
            if(i[0] == "India"):
                india[int(i[2])] = float(i[-1])
            elif((i[0] == "Brunei Darussalam" and int(i[2]) == 2014) or
                 (i[0] == "Cambodia" and int(i[2]) == 2014) or
                 (i[0] == "Indonesia" and int(i[2]) == 2014) or
                 (i[0][0:3] == "Lao" and int(i[2]) == 2014) or
                 (i[0] == "Malaysia" and int(i[2]) == 2014) or
                 (i[0] == "Malaysia" and int(i[2]) == 2014) or
                 (i[0] == "Myanmar" and int(i[2]) == 2014) or
                 (i[0] == "Philippines" and int(i[2]) == 2014) or
                 (i[0] == "Singapore" and int(i[2]) == 2014) or
                 (i[0] == "Thailand" and int(i[2]) == 2014) or
                 (i[0] == "Viet Nam" and int(i[2]) == 2014)):
                i1 = i[0].split(" ")
                south_asia[i1[0]] = i[-1]
            elif(i[0] == "Southern Asia"):
                saarc[int(i[2])] = float(i[-1])
            elif(i[0] == "ASIA" and 2004 <= int(i[2]) < 2015):
                grouped_asian[int(i[2])] = float(i[-1])
            else:
                if(len(india.keys()) != 0 and len(south_asia.keys()) != 0 and
                   len(saarc.keys()) == 10 and len(grouped_asian.keys()) != 0):
                    break


def plotting():
    # Generate position for grouped bar
    w = []
    for i in range(len(grouped_asian.keys())):
        if(len(w) == 0):
            w.append(0)
        else:
            w.append(w[-1]+0.4)

    # this section is plotting bar graph of indian population Vs year.
    mt.subplot(221)
    mt.title("India's Population Over Years")
    mt.bar(india.keys(), india.values(), width=0.4)
    mt.xlabel("Year")
    mt.ylabel("Population in 10 lacks")

    # this section is plotting bar graph of South Asian countries in year 2014.
    mt.subplot(222)
    mt.title("South Asian Counties Population of 2014")
    mt.bar(south_asia.keys(), south_asia.values(), width=0.4)
    mt.xlabel("Countries")
    mt.xticks(rotation='vertical')
    mt.ylabel("Population in lacks")

    # this section is plotting bar graph of saarc Countries Population Vs year.
    mt.subplot(223)
    mt.title("saarc Countries Population Over Years")
    mt.bar(saarc.keys(), saarc.values(), width=0.4)
    mt.xlabel("years")
    mt.ylabel("Population in 10 lacks")

    '''
    this section is plotting grouped bar graph of Asian Countries
    between year 2004-2014.
    '''

    mt.subplot(224)
    mt.title("Asian Countries")
    color = ['red', 'blue', 'orange']
    mt.bar(w, grouped_asian.values(), width=0.4, color=color)
    mt.xlabel("Year 2004-2014")
    mt.ylabel("Population in 10 lacks")

    mt.tight_layout()
    mt.show()


main()
plotting()
