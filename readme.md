# `Downloads` Folder Organizer Documentation

This Python script helps organize your default Downloads folder by sorting files into respective folders based on their file extensions.

## Implementation
The script creates if not exist and sorts files into 'Images', 'Videos', 'Audios', 'Documents', 'Executables', 'Others', and 'Folders' directories.

## Usage
Simply run the script and it will automatically organize the files in your 'Downloads' directory according to their extensions.
```
py main.py
```

The `relocate_files` function moves each file in `Downloads` directory into corresponding directory based on file type (according to file extension).
The `create_specific_extension_folders` function then organizes each files within its respective directory ('Images', 'Videos', etc.) into further directories according to their specific file extensions .jpg, .mp4, etc.
Dictionary Mapping
In the script a dictionary (folders_dict) is used to map various file extensions to the respective folders they should be moved into.

## Dictionary Mapping
In the script a dictionary (`folders_dict`) is used to map various file extensions to the respective folders they should be moved into.
```folders_dict = {
'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff', '.tif'],
'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.vob', '.mng', '.qt', '.mpg', '.mpeg',
'.3gp', '.3g2'],
...
```

[#ff0000]
## Caution
This program will sort all the files in the directory where it is run. Use it carefully as the process is not easily reversible. Also, always make sure to backup your files before running the script.
[/#ff0000]

## Troubleshooting
In case of any errors, check whether the file or directory it’s trying to move already exists in the destination location or not. Also, make sure the script has enough permission to access and modify the directory.

## Future Plans
In future updates, we plan to make the sorting process reversible and the classifications more flexible for better customization.