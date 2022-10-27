# UBAT
A repository for files dealing with data from an Underwater Bioluminescence Assessment Tool (UBAT, Sea-Bird Scientific)

### File descriptions
| File name                    | Description  |
|:-----------------------------|:-------------|
| convert_dat_to_csv.py        | converts a UBAT .dat file to a .csv file |
| convert_dat_to_csv_batch.py  | converts all UBAT .dat files in a folder to .csv files |
| get_column_data.py           | saves a specified column of data from a UBAT .dat file into a .csv file |
| raw_counts_batch.py          | concatenates all "60 Hz digitized raw A/D counts" values from a UBAT .dat file into a single row in a .csv file. All files in a specified folder are processed |


### Example: how to use *raw_counts_batch.py*
1. Specify the path to the folder containing data files in your copy of the *raw_counts_batch.py* script, line 18
2. Run the script with python *(the script will first look for .dat files and only process those. If it doesn’t find any .dat files, then it will process ALL the files in that folder. In the latter case, it is important to remove all non-UBAT files from the folder so it doesn’t try to process some random file it can’t handle)*
3. For each UBAT file in the folder, a .csv file will be made and saved in the same folder specified as input in step 1
