__author__ = 'MatthewWork'

"""
identify list of files in directory
reads each file for matching stock code
extract data corresponding to nominated stock code from each file in directory
create file containing stock code history to file.
"""

import os, sys, csv


# set directory
path = "../2014/";
dirs = os.listdir( path );
#set output file
outputFileName = "test.csv"

# open all the input files and search for matching stock code.
ofile = open(outputFileName, 'w', newline='')
writer = csv.writer(ofile, delimiter=',')

for file in dirs:
    print (file);
    ifile  = open(path+file, "rt")
    reader = csv.reader(ifile)
    for row in reader:
        #print ('row=',row)
        #print ('type(row)=', type(row))
        #print('row[0]=',row[0])
        if (row[0]=='AAA'):
            print ('row[0]=AAA, row=', row)
            writer.writerow(row)


    ifile.close()
ofile.close()


