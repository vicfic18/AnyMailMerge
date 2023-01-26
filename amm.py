#!/usr/bin/env python3
import csv

csv_filename = 'test_data.csv'
template_filename = 'template.svg'

def findnreplace(row_data):
    
    template = open(template_filename, 'r')
    svg_data = template.read()

    for i in range():
        #Remember to customise this space according to your need.
        svg_data = svg_data.replace("x_name_x", name)

    new_filename = "out/"+name+".svg"
    
    with open(new_filename, 'w') as outfile:
        outfile.write(svg_data)
        print(name+"File outed")

csvfile = open(csv_filename, 'r')
csvreader = csv.reader(csvfile)

#skips over fields
next(csvreader)

for row in csvreader:
    findnreplace(row)
    #print(row[3])
