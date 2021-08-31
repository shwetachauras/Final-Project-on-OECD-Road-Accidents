def csvToList(csv_file):
    """
    This functions reads data from a csv file
    Accepts a csv file as paramter
    Returns a list of lists, with data of only 0, 5 and 6 columns 
    (i.e. country name, year and number of road deaths) of csv file.
    Header of the file is ignored.
    """
    with open (csv_file) as file_read_list:
        csv_list = []                     #an empty list is created to store data from csv file
        row_idx = 0
        for row in file_read_list:
            if row_idx > 0:
                temp_row = row.strip().split(",")  #stripping the data off any characters
                selected_items = [temp_row[0].strip('/"'), int(temp_row[5].strip('/"')), float(temp_row[6].strip('/"'))]  #selecting 0, 5 and 6 cols of csv file
                csv_list.append(selected_items)   #appending the data to csv_list
            row_idx += 1
        return csv_list          


def CountrySet(item_list):
    """
    This function is to create a set of countries to remove the duplicates
    Accepts a list of lists (loaded from csv file)
    Returns a set of item of first column index (i.e. a set of country in our case)
    """
    countries_item_set = set()           #an empty set created to store items
    for item in item_list:
        countries_item_set.add(item[0])  #index 0 of the list refers to countries, these are added to the set
    return countries_item_set                  


def FetchHighest(item_list, req_no):
    """
    This function is to fetch the highest road deaths data
    Accepts a list of lists (loaded from csv file) and a number 'req_no'
    Returns top 'req_no' of the highest data from the list
    """
    max_item = []                   #variable defined as empty list to store a single highest data element list
    max_item_list = []              #variable defined as empty list to store the list of highest data elements lists

    for outer_idx in range(req_no):  #outer index loop runs it 'req_no' of times to fetch the top (req_no of) highest data
        inner_idx = 0               #inner index is for the internal loop within the list and begins with 0 every time outer index loop runs
        max_idx = 0                 #to identify and pop the highest data element from the list
        max_val = 0                 #to store the highest data element
   
        for item in item_list:       #runs loop within the csv items list
            item[2] = float(item[2]) #converts string to float value for road deaths data 
            if max_val < item[2]:    
                max_val = item[2]  
                max_idx = inner_idx   #stores the highest data index in max_idx after comparison
                max_item = item       #stores the highest data element in max_item after comparison
            inner_idx += 1            #increment on inner index after each loop to maintain its consistency with the index of element in list
        max_item_list.append(max_item) #at the end of for loop, appends the highest data element to max_item_list
        item_list.pop(max_idx)         #pops out the highest data index from the original item list for next 'outer index' loop to fetch next highest data element
        outer_idx += 1                  #increment of outer index after each loop on outer index range
    return max_item_list                #returns the list of top 'req_no' of highest data elements 


def FetchLowest(item_list, req_no):
    """
    This function is to fetch the lowest  road deaths data
    Accepts a list of lists (loaded from csv file)and a number 'req_no'
    Returns 'req_no' of the lowest data from the list
    """
    min_item = []                     #variable defined as empty list to store a single lowest data element list
    min_item_list = []                #variable defined as empty list to store the list of total lowest data elements lists

    for outer_idx in range(req_no):   #runs the loop 'req_no' of times to fetch the top (req_no of) lowest data
        inner_idx = 0                 #inner index is for the internal loop within the list and begins with 0 every time outer index loop runs
        min_idx = 0                   #to identify and pop the lowest data element from the list
        min_val = 0                   #to store the lowest data element
   
        for item in item_list:        #runs loop within the csv items list
            item[2] = float(item[2])  #converts string to float value for road deaths data 
            if min_val == 0:
                min_val = item[2]
            if min_val > item[2]:
                min_val = item[2]  
                min_idx = inner_idx    #stores the lowest data index in max_idx after comparison
                min_item = item        #stores the lowest data element in max_item after comparison
            inner_idx += 1             #increment on inner index after each loop to maintain its consistency with the index of element in list
        min_item_list.append(min_item) #at the end of for loop, appends the lowest data element to max_item_list
        item_list.pop(min_idx)         #pops out the lowest data index from the original item list for next 'outer index' loop to fetch next highest data element
        outer_idx += 1                 #increment of outer index after each loop on outer index range
    return min_item_list               #returns the list of top 'req_no' of lowest data elements 


def DataByYear(item_list, year):
    """
    This function filters data on the basis of year
    Accepts a list of lists (loaded from csv file) and an input year
    Returns a list of data filtered as per the input year
    """
    year_data_list = []                #empty list created to store the data filtered by year
    for item in item_list:             #iterates over each item in items list
        if int(item[1]) == year:       #checks if the year in data matches to the input year
            year_data_list.append(item) #appends items to year_data_list only for those whose year matches to the input year

    if year_data_list == 0:             #checks if there is no data available for input year
        return []                       #returns an empty list
    else:
        return year_data_list           #return data filtered as per year if there is data available for the input year


def FilterByCountry(item_list, country):
    """
    This function filters data on the basis of country
    Accepts a list (loaded from csv file) and an input country
    Returns a list of data filtered as per the input country
    DataByYear could be accomodated to include this function as well
    But a separate function is created for country filter to simplify the code as year and country have differet column index and data types
    """
    country_data_list = []                     #empty list created to store the data filtered by country
    for item in item_list:                     #iterates over each item in items list 
        if country.lower() == item[0].lower(): #checks if the country in data matches to the input country, both strings converted to lower to avoid case mismatch
            country_data_list.append(item)     #appends items to country_data_list only for those whose country matches to the input country
   
    if country_data_list == []:                #checks if there is no data available for input country 
        return []                              #returns an empty list
    else:
        return(country_data_list)              #return data filtered as per country if there is data available for the input country


def PrintData(item_list, req_no):
    """
    This functions prints data in comprehensible format by accepting a list and an input number
    """
    for i in range(req_no):                #runs the loop input number of times to print the data
        print(i+1,".", "Road Deaths reported: ", item_list[i][2],"per million inhabitants & million vehicles", "\tin year: ", item_list[i][1], "\tand in country: ", item_list[i][0])
    print("\n")


def LatestYear(item_list):
    """
    This functions finds out the latest year whose data are available in the csv file list
    Accepts a list 
    Returns the highest value of year whose data are available in the list
    """
    latest_year = 0               #variable defined as 0 first to store the latest year 
    for item in item_list:        #runs the loop for every item in item list
        if latest_year < item[1]: 
            latest_year = item[1]
    return(latest_year)            #returns the latest year after the comparison is completed


def IdentifyMissingData(countries_set, year_data_list):
    """
    This function is to identify a list of countries whose data on road deaths is missing for a given year
    Accepts a set of total countries whose data are available in the csv file, and a list of data filtered by 'year'
    Returns the set of countries whose data are missing for a given year
    """
    year_country_set = CountrySet(year_data_list)     #creates a set of countries whose data is available for a particular year
    missing_countries = []                          #empty list created to store the missing countries
    if len(countries_set) == len(year_country_set): 
        return 0                                    #returns 0 if the total countries set is equal in length to the set of countries for a particular year
    else:
        missing_countries = countries_set - year_country_set #takes the differences of total countries set and the a particular year countries set
        return(missing_countries)                   #returns the difference as missing countries set
