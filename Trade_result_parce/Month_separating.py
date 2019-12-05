# Open and modify files built-in functions
import os.path

def file_separater (file):
    """
    description:
    This script use a pattern to separate one file into few new files with determinated confitions.
    file - is a source file
    """
    source_file = open(file,"r")
    header = source_file.readline() # write in first line in each new separated file
    counter = 0
    print(header, end='')
    buffer = source_file.readline() #buffer for comparator
    file_name = str(buffer.split(',')[3][:7] + '.csv') #variable for separated file name
    print(buffer.split(',')[3][:7])
    print(file_name)
    
    for line in source_file:
        if line.split(',')[3][:7] == buffer.split(',')[3][:7]:
            print(line, end='')
        elif line.split(',')[3][:7] != buffer.split(',')[3][:7]:
            buffer = line
    source_file.close() # close source_file
    
    
file_separater('head100_traderes.csv')