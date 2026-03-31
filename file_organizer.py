#!/usr/bin/env python3
"""
Process flow file-organizer:
1. Input Folder file path to Organize
2. Find file types to organize. 
3. Move to folders
3. Send a summary of how files are organized (via email)
"""

from pathlib import Path
from datetime import date
import shutil

def get_file_path():

    home_dir = Path('~').expanduser()
    organize_folder = input('\nEnter Folder Path to Organize? ')
    full_path = home_dir.joinpath(organize_folder.strip())
    if full_path.exists():
        return full_path
    else: 
        return None

def organize_files(directory):
    print(f'\nOrganizing files in {directory}...\n')
    home_dir = Path('~').expanduser()

    dirs_list = [item for item in directory.iterdir() if item.is_dir()]
    files_list = [item for item in directory.iterdir() if item.is_file()]

    text_types = [ {'foldername': 'Excel Files', 'extension': ['.csv', '.xlsx'] },
                    {'foldername': 'PDF Files', 'extension': ['.pdf'] },
                    {'foldername': 'Document Files', 'extension': ['.docx'] },
                    {'foldername': 'Plain Text Files', 'extension': ['.txt'] },
                    {'foldername': 'Powerpoint Files', 'extension': ['.ppt', '.pptx'] },
                    {'foldername': 'HTML Files', 'extension': ['.html'] },
                ]
    
    image_types = [ {'foldername': 'JPEG Files', 'extension': ['.jpg', '.jpeg'] },
                   {'foldername': 'PNG Files', 'extension': ['.png'] },
                   {'foldername': 'GIF Files', 'extension': ['.gif'] },
                   {'foldername': 'HEIC Files', 'extension': ['.heic'] },
                ]

    video_types = [ {'foldername': 'MOV files', 'extension': ['.mov'] },
                   {'foldername': 'MP4 files', 'extension': ['.mp4'] },
                   {'foldername': 'MOV files', 'extension': ['.mov'] }, 
                ]
    
    audio_types = [ {'foldername': 'MP3 files', 'extension': ['.mp3']} ]
    installer_types = [ {'foldername': 'DMG files', 'extension': ['.dmg']} ]
    filetypes_list = [text_types, image_types, video_types, audio_types, installer_types ]

    today = date.today().strftime('%m%d%Y')
    
    dest_foldername = Path(str(directory) + '/' + 'Files Organized - '+ today)
    if not dest_foldername.exists():
        dest_foldername.mkdir()

    try:
        print(len(files_list))
        countmoved = 0
        notmoved = 0
        for items in files_list:
            file_moved = False
            for types in filetypes_list:
                for ext in types:
                    extlist = ext.get('extension')
                    if items.suffix.lower() in extlist:

                        folder = ext.get('foldername')
                        destination = Path(str(dest_foldername)+'/'+folder)
                        print(destination)
                        if not destination.exists():
                            destination.mkdir()
                            print('Destination created')

                        check_file = Path(str(destination)+'/'+str(items.name))
                        if destination.is_dir():
                            if not check_file.is_file():
                                shutil.move(src=items, dst=destination)
                                print(f'Moving this file: {items.name} in {destination}')
                            else:
                                print(f'File already exists in {destination}')
                        file_moved = True
                        countmoved += 1
                        break
                if file_moved: break
            if not file_moved :
                print(f'This file is not moved: {items.name}')
                notmoved += 0
    except Exception as e:
        print(e)

if __name__ == '__main__':

    full_path = get_file_path()
    if full_path is not None: organize_files(full_path)

