"""
This script takes the "60 Hz digitized raw A/D counts" values from a UBAT .dat file, concatenating them all into a single row
(i.e. creating one continuus row of all the values in their chronological order), and repeats this process for each .dat file in the specified folder.
The output files are saved in the same folder location as the .dat files.

Input
----------
path        : string
              the path to the folder containing (preferably .dat) files.

Output
----------
csv files   : csv
              a .csv file for each .dat file, containing the "60 Hz digitized raw A/D counts" data from the .dat file. These .csv files are saved in the same folder as the .dat files.  
"""
######################## INPUT ####################################
# Specify the path to the folder containing (preferably .dat) files to be converted 
folder_path = r"C:\Users\rjaco\Desktop\UBAT2"
###################################################################

import pathlib #For dealing with path and filenames
import csv

path = pathlib.Path(folder_path) #Make the path understandable ("Windows Paths" instead of just a string)

# Look for .dat files in the folder
files_found = list(path.glob('*.dat'))
if len(files_found) == 0: #If there are no .dat files, make a list of all files in the folder and print a warning message
    print("")
    print("*** WARNING ***")
    print("No .dat files were found in the specified folder. All files, regardless of extension, are processed. If you haven't done so already, REMOVE all non-UBAT files from the folder and then re-run the code")
    print("")
    files_found = list(path.glob('*'))
    no_files=len(files_found) #Number of files found in the specified folder
    print(f"Found {no_files} files") #Print out the number of files found in the folder
else:
    no_files=len(files_found) #Number of .dat files found in the specified folder
    print(f"Found {no_files} .dat files") #Print out the number of files found in the folder


for fname in files_found: #Loop through each file

    with open(f"{fname}") as csvfile: #Open the dat file as a csv file
        content = csv.reader(csvfile, delimiter=',') #Read the dat file
        rows = list(content) #Save the content of the dat file in a list
        full_row=[] #Create an empty list to save values in

        #Determine whether the the data in the dat file includes date+time columns to determine the appropriate column index to use
        if rows[0][0] == 'UBAT0023': #Check the first column to see if it contains the UBAT serial number
            column_start = 10
        else: #If it does not contain the serial number, then the first columns are date and time columns and so the values to keep start in a later column
            column_start = 12

        with open(f"{folder_path}\\{fname.stem}.csv", 'w', newline='') as csvfile2: #Create/open a csv file to save the data in with the same file name as the dat file, but without the .dat extension (using .csv instead)
            writer = csv.writer(csvfile2) #Prepare to write to the csv file

            for i in range(0,len(rows),1): #Loop through each row of the data (the list)
                current_row = rows[i] #Identify the current row
                full_row.extend(current_row[column_start:]) #Save/concatenate the current row, starting at the appropriate column, to the list
                
            writer.writerow(full_row) #Save all the concatenated rows to the csv file

print(f"Converted {no_files} files to .csv") #Print out the number of files that have been converted