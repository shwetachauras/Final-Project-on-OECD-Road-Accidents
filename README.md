## Final Project


### Introduction and Purpose of the project 

- The program will read selected data from a csv file into python program and get insight about the trends of road accidents across the globe.
- The Road Accidents indicator is measured in number of accidents, number of people, per million inhabitants and million vehicles.
- The countries' acronym have been replaced with their full name for user's convenience.
- The users will be able to take informed decisions based on the outputs from the program. 
- The results will give each country an indicator of its road safety as a global measure.
- This is a group project. The authors of the program are: @Shweta Chaurasia and @Sanskrit Singh

### Module(s) used in the Program
This program uses module "matplotlib.pyplot". It can be installed using the command:
- python -m pip install -U pip
- python -m pip install -U matplotlib
- For more info, please refer to: [matplotlib](https://matplotlib.org/stable/users/installing.html)

### Running the Program
- In the beginning, the program displays the total number of countries whose data are available and asks user if he/she wants to view those countries. 
- Subsequently, it asks user to input number between 0 to 3 for predefined query or any other character for customized query.
![Screenshot of Program Running](https://github.com/90812-Intro/final-project-shweta-sanskrit-final-project/blob/f10ec0106c4826daea3d5aa65a9ad5d9f49ba143/Screen%20Shot%20-%20User%20Options%20Display.png)

- The user will be guided to further inputs through the message displayed as per the user's selection.
- In every input event, the user will be basically asked to type year and/or country and/or the number of highest and lowest road deaths data he/she is fetching.
- The program displays the data accordingly in comprehensible format for the user to read.
- For custom query part (when user inputs any other character but 0 to 2), the user will be asked to input 'country' and/or 'year' for which he/she desires to see the data. In the event user only inputs 'country' and leaves 'year' blank, the program plots and displays a graph of no. of deaths in the input country vs. all the year.
- The program also dispalys appropriate error messages to guide the user through if the data doesn't exist for the input value or if the inputs are of invalid format instead of crashing the program.
![Program running part 1](https://github.com/90812-Intro/final-project-shweta-sanskrit-final-project/blob/ce656dfc962f2d92f4d7be1fd3c0b5120a0f88b5/Screen%20Shot%20-%20program%20running%20-%20part%201.png)
![Program running part 2](https://github.com/90812-Intro/final-project-shweta-sanskrit-final-project/blob/fce02a0acf197cd75706a6903596ea205bd03f75/Screen%20Shot%20-%20program%20running%20-%20part%202.png)
![Program running part 3](https://github.com/90812-Intro/final-project-shweta-sanskrit-final-project/blob/ce656dfc962f2d92f4d7be1fd3c0b5120a0f88b5/Screen%20Shot%20-%20program%20running%20-%20part%203.png)
![Program running part 3](https://github.com/90812-Intro/final-project-shweta-sanskrit-final-project/blob/ba9b3577a2f1b9034f936ec35795b6ee5b949924/Python_graph_plot.png)
![Program running part 4](https://github.com/90812-Intro/final-project-shweta-sanskrit-final-project/blob/ce656dfc962f2d92f4d7be1fd3c0b5120a0f88b5/Screen%20Shot%20-%20program%20running%20-%20part%204.png)

### Breakdown of ideas and their assignment under each team member

| Sl. No. | Idea | Team Member |
| ---------- | --------------------------------------------------------------------------------------------------------- | ----------------------------- |
| 1 | Define a function csvToList to import the list of data from csv file and:      i.	Strip any new line character      ii.	Convert them into a list | Shweta |
| 2 | Define a function CountrySet to create a set of total countries whose data are available in the csv file for each year | Sanskrit |
| 3 | Define a function FetchHighest to fetch the 'n' number of highest road deaths data. The function asks user to input the number of data he/she wants to view. | Shweta |
| 4 | Define a function FetchLowest to fetch the 'n' number of lowest road deaths data. The function asks user to input the number of data he/she wants to view. | Shweta |
| 5 | Define a function DataByYear to filter data based on year | Sanskrit |
| 6 | Define a function FilterByCountry to filter data based on country | Shweta |
| 7 | Define a function PrintData to print data of Country, Year and no. of Road Deaths | Sanskrit |
| 8 | Define a function LatestYear to fetch the data of the latest year available | Shweta |
| 9 | Define a function IdentifyMissingData to identify a list of countries whose data on road deaths is missing for a given year | Sanskrit |
| 10 | Take input from user in between 0 to 3 or any other character for difference choices to fetch data on road deaths. The choices are categorized based on (i) overall highest road deaths (ii) overall lowest road deaths (iii) highest and lowest road deaths as per the choice of year (iv) Highest and Lowest Road Deaths for the latest year (v) Custom query on OECD country and year, respectively. | Shweta |
| 11 | If the user inputs only country or only year, customize the program to show the data accordingly instead of throwing error. Display an error message if the user inputs a country or year for which data is not available. ALso, it displays a plot of road deaths vs. year in the event user only country and leaves year blank | Sanskrit |
| 12 | Input validation by ‘try’ and ‘except’ to catch error if the user inputs incorrect year format | Sanskrit |
