"""
The program will read selected data from a csv file into python program and get insight about the trends of road accidents across the globe.
The Road Accidents indicator is measured in number of accidents, number of persons, per million inhabitants and million vehicles.”
The users will be able to take informed decisions based on the outputs from the program. 
The results will give each country an indicator of its road safety as a global measure.
This is a group project. The authors of the program are: @Shweta Chaurasia and @Sanskrit Singh
"""

import matplotlib.pyplot as plt 
import Functions_RD as frd           #importing all functions saved under the name of Functions_RD.py


def main():
    """
    Main Body of Code below:
    """

    csv_list = frd.csvToList("DP_LIVE_23022021042012503_country_name_updated.csv") #loads data from CSV file and store it as list in csv_list

    countries_set = frd.CountrySet(csv_list)                    #gets the set of total countries involved in the CSV file, duplicates removed
    countries_count = len(countries_set)                  #total no. of countries whose data are available in the CSV file

    print("\nTotal number of countries whose data are available:", countries_count,'\n')
    check = input("Would you like to see the list of OECD countries whose data are available? (Y/N): ")
    if check == "Y" or check == 'y':
        for i in countries_set:
            print(i, end = ', ')

    flag = 'Y'                                             #to check if user wants to continue in the later part, flag is set to Yes as default in the beginning
    while flag == 'Y' or flag == 'y':                      #only continues if flag is yes
        
        #asks user to choose an option
        inp_val = input("\n\nPlease enter: \n 0 for Overall Highest number of Road Deaths.\n 1 for Overall Lowest number of Road Deaths.\n 2 to fetch 3 Highest and Lowest Road Deaths as per year entry.\n 3 for Highest and Lowest Road deaths for the latest year of data available.\n Any other character for custom query on country and/or year.\n:: ") 
        
        try:                  #to execute if the user input value is a number between 0 to 3
            inp_val = int(inp_val)
            # inp_val < 4
            # if (inp_val < 4 == True):
            # if(inp_val == i for i in [0,1,2,3]
            #0: Overall Highest number of Road Deaths
            if inp_val == 0:
                reqd_no = input("How many overall highest road deaths data do you want to view? Please Enter: ") #customized to display the requested no. of top road deaths data
                reqd_no = int(reqd_no)                           #user input converted from string to int data type
                max_item_list = frd.FetchHighest(csv_list, reqd_no)  #FetchHighest function called to get highest road deaths data
                print("Overall Highest", reqd_no, "Road Deaths reported data are:\n")
                frd.PrintData(max_item_list, reqd_no)                #PrintData function called to display the data
        
            #1: Overall Lowest number of Road Deaths
            elif inp_val == 1:
                reqd_no = input("How many overall lowest road deaths data do you want to view? Please Enter: ") #customized to display the requested no. of lowest road deaths data
                reqd_no = int(reqd_no)                          #user input converted from string to int data type
                min_item_list = frd.FetchLowest(csv_list, reqd_no)  #FetchLowest function called to get lowest road deaths data
                print("Overall Lowest", reqd_no, "Road Deaths reported data are:\n")
                frd.PrintData(min_item_list, reqd_no)               #PrintData function called to display the data
    
            #2: three Highest and Lowest Road Deaths as per year entry
            elif inp_val == 2:
                year = input("Which year of data would you like to view? Please enter a value in between 1994 to 2019: ")  #asks user to input the year to view the data filtered accordingly
                try:                                               #to catch the error if user inputs invalid format for year 
                    year = int(year)                               #convert year to int data type
                    year_data_list = frd.DataByYear(csv_list, year)    #DataByYear function called to filter the list as per the input year

                    if len(year_data_list) == 0:                    #if there is no data available for input year
                        print("\nNo data available for the entered year") 

                    else:
                        max_data_list = frd.FetchHighest(year_data_list, 3) #fetch top 3 highest road deaths for input year
                        min_data_list = frd.FetchLowest(year_data_list, 3)  #fetch lowest 3 road deaths reported for input year

                        #prints data in user-friendly format
                        print("\nHighest 3 road deaths reported in year", year, "are:")
                        frd.PrintData(max_data_list, 3)
                        print("Lowest 3 road deaths reported in year", year, "are:")
                        frd.PrintData(min_data_list, 3)

                        #also identifies the countries whose data are not available for the input year
                        missing_countries = frd.IdentifyMissingData(countries_set, year_data_list)
                        if len(missing_countries) != 0:
                            print("The countries whose data are not avaible for", year, "are:\n")
                            for country in missing_countries:
                                print(country, end= " ")
                except:                                                            #if invalid year format is entered
                    print("Invalid format entered for year. Please try again")
            
            #3: three Highest and Lowest number of road deaths for the latest year of data available.
            elif inp_val == 3:
                latest_year = frd.LatestYear(csv_list)                      #identifies the latest year
                latest_year_list = frd.DataByYear(csv_list, latest_year)    #filters the original csv list by the latest year
                max_data = frd.FetchHighest(latest_year_list, 3)            #fetches the top 3 highest road deaths reported data
                min_data = frd.FetchLowest(latest_year_list, 3)             #fetches the 3 lowest road deaths reported data
                
                #prints fetched data for user
                print("The latest year whose data available is: ", latest_year,'\n') 
                print("Top 3 road deaths reported in", latest_year, "are:\n")
                frd.PrintData(max_data, 3)
                print("Lowest 3 road deaths reported in", latest_year, "are:\n")
                frd.PrintData(min_data, 3)
            #if input is a number other than 0, 1, 2, 3
            else:
                inp_val.lower()    #raises exception since an integer cannot be converted to lowercase
        
        #if any other character (not 0, 1, 2, 3) entered, goes for custom query on country and year
        except:     
            country = input("Please enter an OECD country: ") #asks user to enter the country
            year = input("Please enter the year (in between 1994 to 2019) to view the data: ")     #asks user to enter the year
            
            #if both country and year inputs are blank
            if country == '' and year == '': 
                print("\nNo data entered for query")

            #if user inputs only year
            elif country == '' and year!= '':
                try:        #to catch error in case users inputs year in invalid format
                    year = int(year)
                    year_list = frd.DataByYear(csv_list, year) #original data list is filtered by input year
                    print("There are", len(year_list), "number of countries data available.")
                    if len(year_list) !=0:
                        inp = input("Would you like to view it? (Y/N): ") #asks user if he/she wants to view all the data fetched
                        if inp == "Y" or inp == 'y':
                            for item in year_list:
                                print("Country:",item[0], "Deaths:", item[2],"per million inhabitants and million vehicles")
                       
                except:       #in user inputs year in invalid format
                    print("\nInvalid format entered for year")

            #if user inputs only country 
            elif country != '' and year == '':
                country_data_list = frd.FilterByCountry(csv_list, country) #filters original csv data list by country
                if len(country_data_list) == 0:
                    print("No data available for the entered country")
                else:
                    x = []
                    y = []
                    for item in country_data_list:
                        x.append(item[1])
                        y.append(item[2])
                    #line graph plot
                    plt.plot(x, y,"-o", color = 'orange', linewidth = 2, markersize = 3, markerfacecolor = 'gray', markeredgecolor = 'red', markeredgewidth = 2, linestyle = '-')# , linewidth = 2, markersize = 4)
                    
                    #title of the plot
                    plt.title("Road Deaths vs. Year for: " +country.upper(), fontdict={'fontsize': 'x-large',        
                                                    'fontweight': 'bold',
                                                    'color': 'black',
                                                    'family': {'helvetica'},
                                                    'verticalalignment': 'baseline',
                                                    'horizontalalignment': 'center'}, 
                                loc='center')

                    #x-axis label
                    plt.xlabel("Year", fontdict={'fontsize': 'large',                                   
                                        'fontweight': 'normal',
                                        'color': 'brown',
                                        'verticalalignment': 'top', 'family': {'arial'}})
                    #y-axis label
                    plt.ylabel("Road Deaths\n (per 10^6 inhabitants & 10^6 vehicles)", fontdict={'fontsize': 'large',               
                                                                'fontweight': 'normal',
                                                                'color': 'brown',
                                                                'verticalalignment': 'bottom',
                                                                'horizontalalignment': 'center', 'family': {'arial'}})
                    #displays the plot
                    plt.show()
            
            #if user inputs both country and year
            else:
                try:        #catches error for invalid format of input year 
                    year = int(year)
                    year_list = frd.DataByYear(csv_list, year)  #filters data for input year
                    if len(year_list) == 0:
                        print("\nNo data available for the entered year")
                    country_data_list = frd.FilterByCountry(year_list, country) #filters data for input country
                    if len(country_data_list) == 0:
                        print("\nNo data available for the entered country and year")
                    else:
                        print("\nThe Deaths reported in", country.upper(), "in year", year, 'was: ',country_data_list[0][2],"per million inhabitants and million vehicles")
                    
                except:      #displays error msg if the input year is in invalid format
                    print("\nInvalid format entered for year")

        flag = input("\n\nWould you like to continue? (Y/N): ")  #asks user if he/she wishes to continue, restarts at while loop if input is Yes, ends the program otherwise
        

    print("Thank you for visitng. Have a nice day!")

if __name__ == "__main__":
    main()
