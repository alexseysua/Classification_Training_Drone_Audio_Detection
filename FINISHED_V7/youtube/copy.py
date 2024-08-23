import os
import shutil

# Define the file names
not_file = 'not.txt'
label_file = 'label.csv'

# Read the folder names from not.txt
with open(not_file, 'r') as file:
    folders = file.read().splitlines()

# Get the current working directory
current_directory = os.getcwd()

# Path to the label.csv file
label_path = os.path.join(current_directory, label_file)

# Loop through each folder and copy the label.csv file
for folder in folders:
    folder_path = os.path.join(current_directory, folder)
    if os.path.isdir(folder_path):
        shutil.copy(label_path, folder_path)
        print(f"Copied {label_file} to {folder_path}")
    else:
        print(f"Folder {folder} does not exist in the current directory")
