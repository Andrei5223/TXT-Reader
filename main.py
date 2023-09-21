# Import Module
import os
import numpy as np 

class files_txt:
    files[]
    def add_file(file):
        files.ex


# Folder Path
path = "/home/aluno/Documentos/GitHub/TXT-Reader/tests/test archives"

# Change the directory
os.chdir(path)

# Read text File
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

# iterate through all file
for file in os.listdir(path):
    # Create vector of files
    files = np.array()

    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"

        # call read text file function
        read_text_file(file_path)