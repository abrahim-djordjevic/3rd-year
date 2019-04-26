import csv
with open (‘input file.dat’,’r’) as f_in, open(‘output file.csv, ‘w’) as f_out:
    reader = csv.reader(f_in, delimiter= ” “)
    writer = csv.writer(f_out, delimiter= ”,”)
    writer.writerows(reader) 
