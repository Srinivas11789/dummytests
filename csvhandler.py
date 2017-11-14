import csv,os 
files = os.listdir(".")

fields = []
rows = []

for file in files:
    filename = file
    # CSV Reader
    with open(filename, 'r') as csvfile:

    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = csvreader.next()
    print fields
    print "\n"

    # extracting each data row one by one
    for row in csvreader:
        if "reference" in row[0]:
            rows.append(row)
    
 
