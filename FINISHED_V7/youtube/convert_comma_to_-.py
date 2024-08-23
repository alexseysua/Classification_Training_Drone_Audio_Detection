import os

def rename_folders_in_current_dir():
    current_directory = os.getcwd()
    for folder_name in os.listdir(current_directory):
        folder_path = os.path.join(current_directory, folder_name)
        if os.path.isdir(folder_path):
            new_folder_name = folder_name.replace(',', '-')
            new_folder_path = os.path.join(current_directory, new_folder_name)
            if folder_name != new_folder_name:
                os.rename(folder_path, new_folder_path)
                print(f"Renamed: {folder_path} to {new_folder_path}")

rename_folders_in_current_dir()
