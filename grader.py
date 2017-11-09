# Mid Term Results Table

# importing csv module
import csv
import re, sys
# csv file name
filename = "results.csv"

# initializing the titles and rows list
fields = []
rows = []
student_grades = {}

# reading csv file
with open(filename, 'r') as csvfile:

    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = csvreader.next()

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # Student NYU id to Grades Dictionary
    for row in rows:
        if "nyu.edu" in row[1]:
            #row[1] = row[1].split("@")[0]
            key = re.search("^(.+?)@nyu.edu",row[1].strip()).group(1)
            student_grades[key] = row[15]

    # get total number of rows
    print("Total no. of students: %d" % (len(student_grades)))
    #print student_grades
    #print "\n"

#print student_grades

target = "grades.csv"

target_fields = []
target_rows = []

with open(target, 'r') as csvfile:

    # creating a csv reader object
    csvreader_target = csv.reader(csvfile)

    # extracting field names through first row
    target_fields = csvreader_target.next()
    target_header1 = csvreader_target.next()
    target_header2 = csvreader_target.next()

    # extracting each data row one by one
    for row in csvreader_target:
        if row[1] is not '':
            if "ID" not in row[1]:
                target_rows.append(row)

    for row in target_rows:
         try:
           row[4] = student_grades[row[1]]
           del student_grades[row[1]]
         except KeyError:
           print row[1],
           pass

    print "\n"
    #print target_rows
    print student_grades

# name of csv file
filename = "upload_grade.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(target_fields)
    csvwriter.writerow(target_header1)
    csvwriter.writerow(target_header2)

    # writing the data rows
    csvwriter.writerows(target_rows)

