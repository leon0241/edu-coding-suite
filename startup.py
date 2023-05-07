import ctypes
import os
import subprocess
from pathlib import Path
import shutil

import screeninfo
print()

# config variables
import py_config

def change_background(path: Path):
    """Sets a wallpaper from a path"""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path), 0)

def install_software(path: Path):
    """Runs an installer for a software"""
    
    # call software at the path
    try:
        subprocess.call(path)
    except:
        raise Exception("Cannot call " + str(path))

def copy_file(path: Path, extract_folder: Path):
    """Copies a file from one location to another"""
    
    # get file name e.g. vscode.zip
    try:
        file_name_ext = path.name
        
        # get extract folder and append file name
        # e.g. downloads/vscode.zip
        copy_destination = extract_folder / file_name_ext
        
        # copy from original to new
        shutil.copy(path, copy_destination)
    except:
        raise Exception("Cannot copy " + str(path))

def extract_file(path: Path, extract_folder: Path):
    """Extracts a file using shutil unpack"""
    
    try:
        # get file title for folder e.g. vscode
        file_name = path.stem

        # get extract folder and append folder name
        # e.g. downloads/vscode (folder)
        extract_location = extract_folder / file_name

        # extract to new location
        shutil.unpack_archive(path, extract_location)
    except:
        raise Exception("Cannot extract " + str(path))

def set_path_variable(path: str, pathed_loc: str):
    """Add a local PATH variable using pathed CLI tool"""

    try:
        # e.g. Gtools\pathed /APPEND "M:\Software\lazygit" /USER
        os.system(pathed_loc + ' /APPEND "' + path + '" /USER')
    except:
        raise Exception("Cannot set PATH of " + path)

def remove_stupid_windows_path(pathed_loc):
    '''Delete a dumb windows feature that makes it so u can't run python from CLI'''
    os.system(pathed_loc + ' /USER /REMOVE 00')

def transform_path(path: str):
    """Turn strings into path objects"""

    try:
        return Path(path)
    except:
        raise Exception("Cannot transform file with path " + path)

def posix_to_win_str(path: str):
    """Turn forward slashes into double backslashes"""
    
    try:
        return path.replace("/", "\\")
    except:
        raise Exception("Cannot transform file with path " + path)

# if there are two wallpapers listed then set them individually
if len(py_config.WALLPAPER == 2):
    SINGLE_WALLPAPER = transform_path(py_config.WALLPAPER[0])
    DUAL_WALLPAPER = transform_path(py_config.WALLPAPER[1])
# if there is only one wallpaper then set them both to the same one
else:
    SINGLE_WALLPAPER = transform_path(py_config.WALLPAPER[0])
    DUAL_WALLPAPER = transform_path(py_config.WALLPAPER[0])

# needs CLI interaction to add to path so you can't just use Path objects
PATHED_LOC = posix_to_win_str(py_config.PATHED_LOC)
PATH_LINKS = [posix_to_win_str(path) for path in py_config.PATH_LINKS.values()]

INSTALLERS = [transform_path(path) for path in py_config.INSTALLERS.values()]
PORTABLE_GIT = transform_path(py_config.PORTABLE_GIT)

EXTRACT_FOLDER = transform_path(py_config.EXTRACT_FOLDER)
EXTRACTS = [transform_path(path) for path in py_config.EXTRACTS.values()]

def main():
    print("Changing background..")
    if (len(screeninfo.get_monitors())) == 1:
        change_background(SINGLE_WALLPAPER)
    else:
        change_background(DUAL_WALLPAPER)
    
    print("Installing Software..")
    for path in INSTALLERS:
        install_software(path)

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
    
    remove_stupid_windows_path(PATHED_LOC)
    
    print("Finished!")

if __name__ == "__main__":
    main()