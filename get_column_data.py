"""
This script saves a specified column of data from a UBAT .dat file into a .csv file

Input
----------
fname     : string
            the path (including the filename with extension) to the .dat file of interest
           
column    : int
            the number of the column to extract from the .dat file specified in fname

Output
----------
csv file  : csv
            a .csv file containing the data from the specified column  
"""
############################# INPUT ##############################
# Define which file to use
fname = r"C:\Users\rjaco\Desktop\UBAT\ubat023_20220606113759.dat"
# Define which column to use (count starts at 1, not 0)
column = 4
##################################################################

import csv
import numpy as np

path_parts=fname.split(sep='\\') #Split the path so the filename can be extracted
vals=[] #Create a list to save values in

with open(fname) as csv_file: #Open the dat file
    content = csv.reader(csv_file, delimiter=',') #Read the dat file
    rows=list(content) #Save the content of the dat file in a list
    for i in range(0,len(rows),1): #Loop through each row of the list
        current_row=rows[i] #Identify the current row
        val = current_row[column-1] #Identify the value in the specified column (subtracting 1 to make column index match python's 0-indexing)
        vals.append(float(val)) #Save the saved value in a list

# Save the list of values to a .csv file with the same name as the .dat file and specifying which column the data is from
np.savetxt(f"{path_parts[-1][0:-4]}_column{column}.csv",vals,delimiter="",fmt='% s')