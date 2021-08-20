#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <...>
#Group Name: <...>
#Class: <...>
#Date: <...>
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
import matplotlib.pyplot as pit
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):
  print("\nThe following dataframe for SEA from 1997 to 2007 are read as follows:")
  #specify ID range to look up
  SEA = df.iloc[228:360, :9]
  print(SEA)
  
  print('\n######################################')
  print('Period: 1997 - 2007')
  print('Region: South East Asia')
  print('The top 3 countries of total visitors that visited singapore:\n')
  
  #Drop year and month cause we dont need it
  NewSEA = SEA.drop(columns=['Year', 'Month'])

  #Convert object to int for calculation
  NewSEA[NewSEA.columns] = NewSEA[NewSEA.columns].astype(int)
  
  #Find total sum 
  TotalSEA = NewSEA.sum()
  
  #Sort values 
  SEA = TotalSEA.sort_values(ascending=False)
  
  #reset int back to objects
  SEA = SEA.reset_index()
  
  #Columns that need to be printed
  SEA.columns = ['Countries', 'Visitors']


  print(SEA.head(3))


  displayChart(SEA)

def displayChart(df):
  #create new variables 
  Top3 = df.head(3)
  Countries = Top3['Countries']
  Visitors = Top3['Visitors']
  #plot the piechart
  figure1,chart = pit.subplots()

  chart.pie(Visitors,
          labels=Countries,
          startangle=90,
          shadow=True,
          autopct='%1.1f%%')

  chart.axis('equal')
  pit.legend()
  #display chart
  pit.show()

  return

#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################