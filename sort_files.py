import os
import shutil

path_dir = 'C:\\Users\\speco\\Downloads\\Telegram Desktop'
set_types = set()
if os.path.exists(path_dir):
    os.chdir(path_dir)
    list_files = os.listdir(path=path_dir)
    for file in list_files:
        file_type = str()
        for symbol_ in file[::-1]:
            if symbol_ != '.':
                file_type += symbol_
            else:
                file_type = file_type[::-1].lower()
                break
        set_types.add(file_type)

shutil.copytree(path_dir, 'SORTED_FILES')
os.chdir('SORTED_FILES')
for every_type in set_types:
    os.mkdir(every_type)
for every_file in list_files:
    for path_destination in set_types:
        if every_file.endswith(path_destination) or every_file.endswith(path_destination.upper()):
            shutil.move(every_file, path_destination)
            break
