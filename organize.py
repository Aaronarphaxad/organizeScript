
import os
import shutil
import glob

# Path to your Downloads folder
downloads_folder = "/Users/your/downloads"

# Dictionary mapping file extensions to folder names
file_types = {
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "TextFiles",
    "mp4": "Videos",
    "avi": "Videos",
    # Add more file extensions and corresponding folder names as needed
}

# Create folders if they don't exist
for folder_name in set(file_types.values()):
    folder_path = os.path.join(downloads_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Organize files
for filename in glob.glob(os.path.join(downloads_folder, "*")):
    if os.path.isfile(filename):
        file_extension = filename.split(".")[-1].lower()
        destination_folder = file_types.get(file_extension, "Other")
        destination_path = os.path.join(downloads_folder, destination_folder)
        shutil.move(filename, destination_path)

print("Files have been organized.")
