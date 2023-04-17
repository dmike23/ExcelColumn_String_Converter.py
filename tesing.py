import pandas
import os

cwd = os.getcwd()
print('Current Working Directory is: ', cwd)

#read column Available
checkColumn_data_df = pandas.read_excel('pythonRef1.xlsx', sheet_name='Sheet1', usecols=['Available'])

#grab column as a list
avi = list(checkColumn_data_df.Available)
avi_strings = [str(x) for x in avi]
print(avi_strings)