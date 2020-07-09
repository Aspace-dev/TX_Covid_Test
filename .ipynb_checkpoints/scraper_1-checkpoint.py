# Importing modules
import csv
import os
import requests
import pandas as pd
import xlrd

# Assigning URL to variable
county_case_url = "https://dshs.texas.gov/coronavirus/TexasCOVID19DailyCountyCaseCountData.xlsx"

# Using requests to get the excel file
response = requests.get(county_case_url)
with open('TexasCOVID19DailyCountyCaseCountData.xlsx', 'wb') as output:
    output.write(response.content)

# Assigning data to data frame
county_case_df = pd.read_excel('TexasCOVID19DailyCountyCaseCountData.xlsx')

# Removing Excel file
os.remove('TexasCOVID19DailyCountyCaseCountData.xlsx')

# Printing the first ten rows of the county case data frame
print(county_case_df.head())