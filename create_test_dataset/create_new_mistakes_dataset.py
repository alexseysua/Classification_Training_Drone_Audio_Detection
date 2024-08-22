import os
import shutil

# Define paths to the files
false_negatives_file = '../Create_Dataset_and_train/all_wind_without_pitch/outputs/misclassified_samples/false_negatives.txt'
false_positives_file = '../Create_Dataset_and_train/all_wind_without_pitch/outputs/misclassified_samples/false_positives.txt'

# Define the destination directory
mistakes_dir = '../FINISHED_V7/mistakes/'

# Ensure the destination directory exists
os.makedirs(mistakes_dir, exist_ok=True)


# Function to find the next available index for a new mistake folder
def get_next_index(mistakes_dir):
    existing_folders = [d for d in os.listdir(mistakes_dir) if os.path.isdir(os.path.join(mistakes_dir, d))]
    indices = [int(folder.split('_')[-1]) for folder in existing_folders if folder.startswith('mistakes_')]
    return max(indices) + 1 if indices else 1


# Function to copy the target subfolder (e.g., Recording_08-43-15-315795_chunk_239) into the mistakes_<index> folder
def copy_mistake_folder(file_path, dst_base_dir):
    src_folder = os.path.dirname(file_path)  # Get the parent directory of the mfcc.csv file
    folder_name = os.path.basename(src_folder)  # Get the folder name (e.g., Recording_08-43-15-315795_chunk_239)
    dst_folder = os.path.join(dst_base_dir, folder_name)

    if not os.path.exists(dst_folder):
        shutil.copytree(src_folder, dst_folder)
    return dst_folder


# Function to process the paths in the text files
def process_mistakes(file_path, dst_base_dir):
    with open(file_path, 'r') as file:
        paths = [line.split(',')[0].strip() for line in file.readlines()]
    for path in paths:
        copy_mistake_folder(path, dst_base_dir)


# Start with the next available index for the new mistakes folder
next_index = get_next_index(mistakes_dir)
dst_base_dir = os.path.join(mistakes_dir, f'mistakes_{next_index}')
os.makedirs(dst_base_dir, exist_ok=True)

# Process both false negatives and false positives, copying their folders to the same mistakes_<index> directory
process_mistakes(false_negatives_file, dst_base_dir)
process_mistakes(false_positives_file, dst_base_dir)

print(f"All misclassified samples have been copied to {dst_base_dir}.")
