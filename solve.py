import csv

india, south_asia, saarc, grouped_asian = {}, {}, {}, {}


def solve():
    with open('population.csv') as pop_table:
        table = csv.reader(pop_table)

        # this for loop is doing structurize data needed for plotting graph
        for i in table:
            """
                - filter out indian population over year
                - second elif is for to fiter out population of
                    south east asian countries in year 2014.
                    There are have total 10 countries in South east Asia.
                - Third elif is for to filter out southern asian countries
                    Population of all the years.
                - Fourth elif loop filter out the population of Asia from year
                    2004 to 2014
                - Last else is for to break the loop if got all the
                    expected values. It will reduce the extra iteration.
            """
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
