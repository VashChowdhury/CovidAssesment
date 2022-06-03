import pickle
import numpy as np

def load_with_pickle(fileName):
    """
    Simple method to load an object from a binary pickle file
    :param fileName: Path where object was saved
    :return: Object that was saved in file
    """
    file = open(fileName, "rb")
    obj = pickle.load(file)
    file.close()
    return obj


class CovidRecord:
    """
    A simple class to hold record data from NYT database
    """

    def __init__(self, _date='', _county='', _state='', _fips=0, _cases=0, _death=0):
        """
        Default constructor for transforming each line of the file into data point

        :param _date: Date covid case was recorded
        :param _county: County in which data was recorded
        :param _state: State in which data was recorded
        :param _fips: Federal Information Processing Standards code
        :param _cases: Number of total cases recorded
        :param _death: Number of total deaths recorded
        """
        self.date = _date
        self.county = _county
        self.state = _state

        if _fips == '':
            self.fips = 0
        else:
            self.fips = int(_fips)
        self.cases = int(_cases)

        if _death == '':
            self.death = 0
        else:
            self.death = int(_death)


# all student code goes in the lines below here
if __name__ == "__main__":
    # load covid data as list of CovidRecord objects
    data = load_with_pickle('covid_data.pickle')

    # each element in data is a CovidRecord object. Each of which contains
    # date, county, state, fips, cases, and deaths

    # for example, we can print out the data for the first point in the US counties file
    point = data[0]

    #print("Data: ", point.date, " County: ", point.county, " State: ", point.state,
          #" FIPS: ", point.fips, " Cases: ", point.cases, " Deaths: ", point.death)

    # write code to address the following question:
    # When was the first positive COVID case in Rockingham County and Harrisonburg?

    firstcaserh = []  # set empty list for first case
    for x in data: #for loop for variable x in the data set
        if x.fips == 51165.0:  #if x value for fips equals rockingham fips value
            firstcaserh.append(x.date)   #add the date into the list
            print('The first postive Covid Case in Rockingham County was on ' + str(firstcaserh[0]))  #print out the statement with index of 0, first case
            break

    firstcasehb = []  # repeat above for harrisonburg
    for y in data:
        if y.fips == 51660.0:
            firstcasehb.append(y.date)
            print('The first positive Covid Case in Harrisonburg was on ' + str(firstcasehb[0]))
            break

    # write code to address the following question:
    # What day was the greatest number of new daily cases recorded in Harrisonburg and Rockingham County?

    greatestdaterh = []  #set empty list for dates in rh
    caserh = []   #set empty lists for cases in rh
    greatestdatehb = []   #set empty list for dates in hb
    casehb = [] #set empty lists for cases in hb

    greatestcaserh = []  #empty list for the differences of cases in rockingham
    greatestcasehb = [] #empty list for the differences of cases in harrisonburg

    for x in data:  # same as above however, append dates and cases into the two empty lists above
        if x.fips == 51165.0:
            greatestdaterh.append(x.date)

    for x in data:
        if x.fips == 51165.0:
            caserh.append(x.cases)

    #print(greatestdaterh)
    #print(caserh)


    greatestcaserh = [caserh[i+1]-caserh[i] for i in range(len(caserh) - 1)]  # find the difference and set into new list
    greatestcaserh

    #print(greatestcaserh)

    #print((max(greatestcaserh)))

    i = 0    #set i - 0 to itterate through loop
    while i < len(greatestcaserh): #while loop in cases
        if greatestcaserh[i] == max(greatestcaserh): #if equal to the max
            print('The date with the greatest covid case in Rockingham is ' + greatestdaterh[i+1]) #print index of the date with the max case
            break
        else: # if its not found, keep iteerating
            i += 1

# repeat everyhing for harrisonburg
    for y in data:
        if y.fips == 51660.0:
            greatestdatehb.append(y.date)

    for y in data:
        if y.fips == 51660.0:
            casehb.append(y.cases)

    #print(greatestdatehb)
    #print(casehb)

    greatestcasehb = [casehb[i + 1] - casehb[i] for i in range(len(casehb) - 1)]
    greatestcasehb

    i = 0
    while i < len(greatestcasehb):
        if greatestcasehb[i] == max(greatestcasehb):
            print('The date with the greatest covid case in Harrisonburg is ' + greatestdatehb[i+1])
            break
        else:
            i += 1

    #print(greatestcaserh)


    # write code to address the following question:
    # In terms of absolute number of cases, when was the worst seven-day period in the city/county for new COVID cases?

    mov_avg_list_rh = []    #set empty list for moving avg
    for x in range(len(greatestcaserh)):  #for loop for x in the greatest case(diff)
        avg_rh = (sum(greatestcaserh[x:x+6]))/7  # find average by finding sum and dividing by 7 days
        mov_avg_list_rh.append(avg_rh) #append into new list

    i = 0
    while i < len(mov_avg_list_rh): #while loop
        if mov_avg_list_rh[i] == max(mov_avg_list_rh): #if new list index is equal to the max
            print('The date with the absolute greatest covid cases in Rockingham is between ' + greatestdaterh[i + 1] + ' and ' + greatestdaterh[i+7]) #print the dates for the seven day periods
            break
        else:
            i += 1 #itterate through

    mov_avg_list_hb = []  # repeat all for hb
    for y in range(len(greatestcasehb)):
        avg_hb = (sum(greatestcasehb[y:y + 6])) / 7
        mov_avg_list_hb.append(avg_hb)

    i = 0
    while i < len(mov_avg_list_hb):
        if mov_avg_list_hb[i] == max(mov_avg_list_hb):
            print('The date with the absolute greatest covid cases in Harrisonburg is between ' + greatestdatehb[i + 1] + ' and ' +
                  greatestdatehb[i + 7])
            break
        else:
            i += 1




