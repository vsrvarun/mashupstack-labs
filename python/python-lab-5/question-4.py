# I have a folder with 20 files in it of different file names. Eg: 01022017_tvm.csv, 01022017_klm.csv, 01022017_ekm.csv, 01022017_sample.csv and so on..  
# The csv files should have the following columns
# id, date, location, car name, model name, seller name, seller address, price
# ( ie. daily sales report of each location of the Benz cars )
# The files can have any content. So you can create any files you like.

# In this filename, 01022017.csv the first 01 represents the date, 02 represents the month ( feb ) and 2017 represents the year.
# _tvm represents the location ie. trivandrum
# Write a python program to  read the existing csv files and create a new consolidated file for all the locations and save as:-
# 01022017_all.csv
# Make sure the line numbers are right and the data is appended correctly.
# While appending the files, ignore the file called as 01022017_sample.csv 

# note: When doing this, please take into consideration the error conditions that can happen and make sure your code handles them all
# Eg:  
# Check for the filetype: only csv files should be considered.
# Ignore files with 0 content
# Make sure files have read permission, and files already exist.
# Make sure the directory is writable
# etc and so on...
import datetime
import os
import re
import csv
from datetime import datetime
try: 
    # Provide directory url.
    os.chdir("directory_url/csv-files")
    files = os.listdir()
except:
    print("Error! Cannot Access Selected Directory")
else:
    # Only csv file with valid format considered
    files_valid = []
    locations = {"tvm": "Trivandrum", "klm": "Kollam", "ekm": "Ernakulam", "clt": "Calicut", "kgq": "Kasaragod"}
    location_code = locations.keys()
    regx_location = "|".join(location_code)
    for file in files:
        pattern = "^[0-9]{8}_[" + regx_location + "]{3}.csv$"
        valid = re.search(pattern, file)
        if valid:
            files_valid.append(file)
    if len(files_valid) == 0:
        print("No valid files present in the directory")
    else:
        consolidated = [['id', 'date', 'location', 'car name', 'model name', 'seller name', 'seller address', 'price']]
        errors = []
        for filename in files_valid:
            try:
                f = open(filename, 'r')
                reader = list(csv.reader(f))
            except:
                print("Unable to read", filename)
            else:
                if len(reader) > 1:
                    line_count = 0
                    for row in reader:
                        if len(row) == 8:
                            if line_count >= 1:
                                # Adding each csv data into a list
                                consolidated.append(row)
                        else:
                            # Creating a list of filename which contain data error
                            errors.append(filename)
                        line_count += 1
            finally:
                f.close()
        # Generating new filename for consolidated file
        filename_date = ''
        for date_str in files_valid[0]:
            if date_str.isdigit():
                filename_date += date_str
        wrt_date = datetime.strptime(filename_date, "%d%m%Y")
        wrt_filename = wrt_date.strftime("%d%m%Y") + "_all.csv"
        # Writing consolidated file into directory
        try:
            f = open(wrt_filename, 'w')
            try:
                writer = csv.writer(f)
                writer.writerows(consolidated)
            except:
                print("Unable to write! Make sure the directory is writable")
            finally:
                f.close()
        except:
            print("Something went wrong while creating", wrt_filename)
        else:
            print("Created a consolidated file", wrt_filename)
            print("Given CSV data not valid on following file(s):")
            for error in errors:
                print(error)