# Create a sample CSV File. ( Comma separated Value ) which includes the following fields
# id, name, product, price
# The files can have any content. So you can create any files you like. Just make sure the column names are as above
# Write a python program to 
# - print the 3rd row of csv file
# - only the 2nd column of the csv file.
# - first 3 lines of the csv file.
import csv
# Provide directory url. 
with open('directory_url/csv-files/product.csv', 'r') as file:
    reader = list(csv.reader(file))
# Thid row of csv file
line_count = 0
for x in reader:
    if line_count == 2:
        print("The 3rd row of csv file:")
        print(x)
    line_count += 1
# 2nd column of the csv file.
print("2nd column of the csv file:")
for y in reader:
    print(y[1])
# first 3 lines of the csv file.
line_count = 0
print("First 3 lines of the csv file:")
for z in reader:
    if line_count <= 2:
        print(z)
    line_count += 1