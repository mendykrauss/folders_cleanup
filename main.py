import os

downloads_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
folders_to_skip = {'Images', 'Videos', 'Audios', 'Documents', 'Executables', 'Others', 'Folders'}


def relocate_files(orig_folder, folders, extensions):
    n = 1
    for file in os.listdir(orig_folder):
        file_path = os.path.join(orig_folder, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1]
            for i in range(len(extensions)):
                if file_extension in extensions[i]:
                    os.rename(file_path, os.path.join(orig_folder, folders[i], file))
                    break
            else:
                os.rename(file_path, os.path.join(orig_folder, 'Others', file))
        elif os.path.isdir(file_path) and file not in folders_to_skip:
            os.rename(file_path, os.path.join(orig_folder, 'Folders', file))
        print(f'File {file} moved.')
        print(f'{n} files moved.')
        n += 1
    print('Done!')


def create_specific_extension_folders(orig_folder, folders):
    m = 1
    for f in folders:
        if m == 10:
            break
        for file in os.listdir(os.path.join(orig_folder, f)):
            file_path = os.path.join(orig_folder, f, file)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file)[1]
                specific_folder = os.path.join(orig_folder, f, file_extension[1:])
                if not os.path.exists(specific_folder):
                    os.mkdir(specific_folder)
                os.rename(file_path, os.path.join(specific_folder, file))
                print(f'File {file} moved.')
                print(f'{m} files moved.')
                m += 1
        print(f'Folder {f} done.')
    print('Done!')


folders_dict = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff', '.tif'],
    'Videos': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.vob', '.mng', '.qt', '.mpg', '.mpeg',
               '.3gp', '.3g2'],
    'Audios': ['.mp3', '.wav', '.wma', '.aac', '.flac', '.m4a', '.m4r', '.ogg', '.oga', '.opus', '.ra', '.rm',
               '.wv', '.webm', '.mka', '.mpc', '.aiff', '.aif', '.aifc', '.amr', '.ape', '.awb', '.dts', '.gsm',
               '.m4p', '.m4b', '.m4r', '.mid', '.midi', '.mka', '.mpa', '.mp2', '.mp1', '.mogg', '.oga', '.opus',
               '.ra', '.rm', '.sln', '.tta', '.voc', '.vox', '.w64', '.wma', '.wv', '.8svx'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.rtf', '.odt', '.ods',
                  '.odp', '.odg', '.odf', '.ps', '.eps', '.epub', '.md', '.csv', '.xml', '.json'],
    'Executables': ['.exe', '.msi', '.apk', '.app', '.bat', '.bin', '.cgi', '.pl', '.com', '.gadget', '.jar',
                    '.py', '.wsf', '.dmg', '.iso'],
    'Others': [],
    'Folders': []
}

for folder, extension in folders_dict.items():
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

relocate_files(downloads_folder, folders_dict.keys(), folders_dict.values())
create_specific_extension_folders(downloads_folder, folders_dict.keys())
