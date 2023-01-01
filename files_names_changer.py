# This Script can be used to change the names of ALL the files in a folder in Windows.
# It is Usefull to have all your folders neat and organized

import os
import glob

print("----------------------------------")
print("Hi, Lets change the files name !! )


# First well create a list of the files we need to use
files = glob.glob('PATH TO FILES IN THE FOLDER')

# Well sort the files by the creation date parameter (this can be changed based on other parameter)
files.sort(key=os.path.getctime)

# Now we rename the selected files in the list using the previus parameters
for i, file in enumerate(files):
    directory, base = os.path.split(file)
    base, _ = os.path.splitext(base)
    new_name = f'{i+1} FILE NAME_{base}.FILE EXTENSION'
    os.rename(file, os.path.join(directory, new_name))
    
print("----------------------------------")
print("names changed !")
