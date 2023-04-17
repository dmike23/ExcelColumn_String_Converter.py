import pandas
import os

cwd = os.getcwd()
print('Current Working Directory is: ', cwd)

#read the whole sheet
checklist_data_df = pandas.read_excel('checklist.xlsx', sheet_name='Field check')

#read only Field name column
checkColumn_data_df = pandas.read_excel('checklist.xlsx', sheet_name='Field check', usecols=['Field Name'])

# print whole sheet data
print(checklist_data_df)
#print column names
print(checklist_data_df.columns.ravel())
print(checklist_data_df['Field Name'].tolist())

print(checkColumn_data_df)