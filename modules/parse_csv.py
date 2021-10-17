# csv files - comma separted value 
# allows us to put plane text file and comma to seprate some data 

import csv

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	for line in csv_reader:
		print(line[0:])   # can also use index to get only emails like print(line[2])


print(dir(csv))