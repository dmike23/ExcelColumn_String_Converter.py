import pandas
import os
import openpyxl
import ast

cwd = os.getcwd()
print('Current Working Directory is: ', cwd)

#read column Available
checkColumn_data_df = pandas.read_excel('pythonRef1.xlsx', sheet_name='Sheet1', usecols=['Available'])

#grab column as a list
avi = list(checkColumn_data_df.Available)
avi_strings = [str(x) for x in avi] #remove ints

#print(checkColumn_data_df)
print(avi_strings)

#list to string
to_string = ", ".join(avi_strings)

print(to_string)

words = to_string.split(', ')
#replace substring in string nan for N
words = ['N' if word == 'nan' else 'Y' for word in words]
print(words)

#convert modified string back to list
#modified_list = words.split(",")

#print result
#print("The list after substring replacement : " + str(modified_list))

#back to df
export_df = pandas.DataFrame(words, columns=['Updt'])
print(export_df)
#write to excel
export_df.to_excel('pythonRef3.xlsx', columns=['Updt'], header=False)


