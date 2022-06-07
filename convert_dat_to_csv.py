"""
This script takes converts a UBAT .dat file to a .csv file 

Input
----------
fname     : string
            the path (including the filename with extension) to the .dat file of interest

Output
----------
csv file  : csv
            a .csv file containing the data from the specified .dat file with the appropriate column names  
"""
######################## INPUT ####################################
# Define which file to convert
fname = r"C:\Users\rjaco\Desktop\UBAT\ubat023_20220606113759.dat"
###################################################################

import csv

#Split the path so the filename can be extracted
path_parts = fname.split(sep='\\') 

#Specify the header/column names of the data in the dat file
header = ['UBAT SN','Record Number','Calibration coefficient for HV step','Average Bioluminescence','Pump RPM','System Voltage','Flow RPM','HV step','Reserved','Reserved','60 Hz digitized raw A/D counts from this column on']

with open(fname) as csvfile: #Open the dat file as a csv file
    content = csv.reader(csvfile, delimiter=',') #Read the dat file
    rows = list(content) #Save the content of the dat file in a list

    with open(f"{path_parts[-1][0:-4]}.csv", 'w', newline='') as csvfile2: #Create/open a csv file to save the data in with the same file name as the dat file, but without the .dat extension (using .csv instead)
        writer = csv.writer(csvfile2) #Prepare the csv file
        writer.writerow(header) #Add the header to the csv file

        for i in range(0,len(rows),1): #Loop through each row of the data (the list)
            current_row = rows[i] #Identify the current row
            writer.writerow(current_row) #Save the current row to the csv file
