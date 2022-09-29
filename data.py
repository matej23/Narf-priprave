#importing pandas as pd
import pandas as pd
  
# Read and store content
# of an excel file 
read_file = pd.read_excel ("Test.xlsx")
  
# Write the dataframe object
# into csv file
read_file.to_csv ("Test.csv", 
                  index = None,
                  header=True)
    
# read csv file and convert 
# into a dataframe object
df = pd.DataFrame(pd.read_csv("Test.csv"))
  
# show the dataframe




##PISANJE V CSV IZ PYTHON 

#import csv
#
#header = ['name', 'area', 'country_code2', 'country_code3']
#data = [
#    ['Albania', 28748, 'AL', 'ALB'],
#    ['Algeria', 2381741, 'DZ', 'DZA'],
#    ['American Samoa', 199, 'AS', 'ASM'],
#    ['Andorra', 468, 'AD', 'AND'],
#    ['Angola', 1246700, 'AO', 'AGO']
#]
#
#with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#    writer = csv.writer(f)
#
#    # write the header
#    writer.writerow(header)
#
#    # write multiple rows
#    writer.writerows(data)



#PODATKI IZ CSV V PYTHON

#import csv
#rows = []
#with open("Salary_Data.csv", 'r) as file:
#    csvreader = csv.reader(file)
#    header = next(csvreader)
#    for row in csvreader:
#        rows.append(row)
#print(header)
#print(rows)