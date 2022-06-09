"""
This script converts a UBAT .dat file to a .csv file, and saves that .csv file in the same location as the .dat file.

Input
----------
fname            : string
                   the name of the .dat file of interest.
fname_folder     : string
                   the path to the .dat file of interest.

Output
----------
csv file         : csv
                   a .csv file containing the data from the specified .dat file with the appropriate column names. This file is saved in the same folder as the .dat file.  
"""
######################## INPUT ####################################
# Specify the name of the file (including the .dat extension) to convert
fname = "ubat023_20220608132407.dat"
# Specify which folder the file is in 
fname_folder = r"C:\Users\rjaco\Desktop\UBAT"
###################################################################

import csv

with open(f"{fname_folder}\\{fname}") as csvfile: #Open the dat file as a csv file
    content = csv.reader(csvfile, delimiter=',') #Read the dat file
    rows = list(content) #Save the content of the dat file in a list

    #Specify the header/column names to use, depending on whether the the data in the dat file includes date+time columns
    if rows[0][0] == 'UBAT0023': #Check the first column to see if it contains the UBAT serial number
        header = ['UBAT SN','Record Number','Calibration coefficient for HV step','Average Bioluminescence','Pump RPM','System Voltage','Flow RPM','HV step','Reserved','Reserved','60 Hz digitized raw A/D counts from this column on']
    else: #If it does not contain the serial number, then the first columns are date and time columns
        header = ['Date','Time','UBAT SN','Record Number','Calibration coefficient for HV step','Average Bioluminescence','Pump RPM','System Voltage','Flow RPM','HV step','Reserved','Reserved','60 Hz digitized raw A/D counts from this column on']

    with open(f"{fname_folder}\\{fname[0:-4]}.csv", 'w', newline='') as csvfile2: #Create/open a csv file to save the data in with the same file name as the dat file, but without the .dat extension (using .csv instead)
        writer = csv.writer(csvfile2) #Prepare to write to the csv file
        writer.writerow(header) #Add the header to the csv file

        for i in range(0,len(rows),1): #Loop through each row of the data (the list)
            current_row = rows[i] #Identify the current row
            writer.writerow(current_row) #Save the current row to the csv file
