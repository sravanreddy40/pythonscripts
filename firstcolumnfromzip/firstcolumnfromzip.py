from zipfile import ZipFile
import os

dir_path = 'mydirectorypath'
#Enter the extension of the files inside the zip file
file_ext = '.txt'
#Enter the output file with file extension
output_file='ofile.csv'

file_names=(os.listdir(dir_path))

for filename in file_names:
    if '.zip' in filename:

        with ZipFile(dir_path+filename,'r') as zipObj:
            zipObj.extractall()

new_file_names = (os.listdir(dir_path))

of = open(dir_path+output_file,'w+')

for filename in new_file_names:
    if file_ext in filename:
        f = open(dir_path+filename,'r')
        for line in f:
            of.write(line.split(",")[0])
            of.write("\n")
        f.close()

of.close()
