import ctypes
import os
import subprocess
from pathlib import Path
import shutil

import py_config

def change_background(path: Path):
    # set wallpaper from path
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path), 0)

def install_software(path: Path):
    # call software at the path
    try:
        subprocess.call(path)
    except:
        raise Exception("Cannot call " + str(path))

def copy_file(path: Path, extract_folder: Path):
    # get file name e.g. vscode.zip
    print(path)
    file_name_ext = path.name
    
    # get extract folder and append file name
    # e.g. downloads/vscode.zip
    copy_destination = extract_folder / file_name_ext
    
    # copy from original to new
    shutil.copy(path, copy_destination)

def extract_file(path: Path, extract_folder: Path):
    # get file title for folder e.g. vscode
    file_name = path.stem

    # get extract folder and append folder name
    # e.g. downloads/vscode (folder)
    extract_location = extract_folder / file_name

    # extract to new location
    shutil.unpack_archive(path, extract_location)

def set_path_variable(path: str, pathed_loc: str):
    # e.g. Gtools\pathed /APPEND "M:\Software\lazygit" /USER
    os.system(pathed_loc + ' /APPEND "' + path + '" /USER')

def transform_path(path: str):
    '''Turn strings into path objects'''
    return Path(path)

def posix_to_win_str(path: str):
    '''Turn forward slashes into double backslashes'''
    return path.replace("/", "\\")

WALLPAPER = transform_path(py_config.WALLPAPER)

# needs CLI interaction to add to path so you can't just use Path objects
PATHED_LOC = posix_to_win_str(py_config.PATHED_LOC)
PATH_LINKS = [posix_to_win_str(path) for path in py_config.PATH_LINKS.values()]

INSTALLERS = [transform_path(path) for path in py_config.INSTALLERS.values()]
PORTABLE_GIT = transform_path(py_config.PORTABLE_GIT)

EXTRACT_FOLDER = transform_path(py_config.EXTRACT_FOLDER)
EXTRACTS = [transform_path(path) for path in py_config.EXTRACTS.values()]


def main():
    print("Changing background..")
    change_background(WALLPAPER)
    
    print("Installing Software..")
    # for path in INSTALLERS:
    #     install_software(path)

    copy_file(PORTABLE_GIT, EXTRACT_FOLDER)
    install_software(EXTRACT_FOLDER / PORTABLE_GIT.name)    
    
    print("Copying Archives..")
    for path in EXTRACTS:
        copy_file(path, EXTRACT_FOLDER)
    
    print("Extracting Archives..")
    for path in EXTRACTS:
        extract_file(path, EXTRACT_FOLDER)

    print("Setting PATH Variables..")
    for link in PATH_LINKS:
        set_path_variable(link, PATHED_LOC)
    
    print("Finished!")

if __name__ == "__main__":
    main()