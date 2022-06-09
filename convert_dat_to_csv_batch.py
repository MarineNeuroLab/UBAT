"""
This script converts all UBAT .dat files in a specified folder to .csv files, and saves those .csv files in the same folder location as the .dat files.

Input
----------
path        : string
              the path to the folder containing .dat files.

Output
----------
csv files   : csv
              a .csv file for each .dat file, containing the data from the .dat file with the appropriate column names. These .csv files are saved in the same folder as the .dat files.  
"""
######################## INPUT ####################################
# Specify the path to the folder containing .dat files to be converted 
folder_path = r"C:\Users\rjaco\Desktop\UBAT"
###################################################################

import pathlib #For dealing with path and filenames
import csv

path = pathlib.Path(folder_path) #Make the path understandable ("Windows Paths" instead of just a string)

dat_files = list(path.glob('*.dat'))
no_files=len(dat_files) #Number of .dat files in the specified folder
print(f"Found {no_files} .dat files") #Print out the number of files found in the folder

for fname in dat_files: #Loop through each .dat file

    with open(f"{fname}") as csvfile: #Open the dat file as a csv file
        content = csv.reader(csvfile, delimiter=',') #Read the dat file
        rows = list(content) #Save the content of the dat file in a list

        #Specify the header/column names to use, depending on whether the the data in the dat file includes date+time columns
        if rows[0][0] == 'UBAT0023': #Check the first column to see if it contains the UBAT serial number
            header = ['UBAT SN','Record Number','Calibration coefficient for HV step','Average Bioluminescence','Pump RPM','System Voltage','Flow RPM','HV step','Reserved','Reserved','60 Hz digitized raw A/D counts from this column on']
        else: #If it does not contain the serial number, then the first columns are date and time columns
            header = ['Date','Time','UBAT SN','Record Number','Calibration coefficient for HV step','Average Bioluminescence','Pump RPM','System Voltage','Flow RPM','HV step','Reserved','Reserved','60 Hz digitized raw A/D counts from this column on']

        with open(f"{folder_path}\\{fname.stem}.csv", 'w', newline='') as csvfile2: #Create/open a csv file to save the data in with the same file name as the dat file, but without the .dat extension (using .csv instead)
            writer = csv.writer(csvfile2) #Prepare to write to the csv file
            writer.writerow(header) #Add the header to the csv file

            for i in range(0,len(rows),1): #Loop through each row of the data (the list)
                current_row = rows[i] #Identify the current row
                writer.writerow(current_row) #Save the current row to the csv file

print(f"Converted {no_files} .dat files to .csv") #Print out the number of files that have been converted