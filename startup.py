import ctypes
import os
import subprocess
from pathlib import Path
import shutil

# Change the background
dir = os.getcwd()
ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(dir, "reimuwide.png") , 0)

# Install software binaries
# flux = Path("M:/Software/installers/flux-setup.exe")
github = Path("M:/Software/installers/github-setup.exe")
obsidian = Path("M:/Software/installers/obsidian-setup.exe")

os.system('GTools\\pathed /APPEND "C:\\Users\\s2202694\\Downloads\\PortableGit\\bin" /USER')
os.system('GTools\\pathed /APPEND "M:\\Software\\lazygit" /USER')
os.system('GTools\\pathed /APPEND "C:\\Users\\s2202694\\Downloads\\python portable" /USER')
os.system('GTools\\pathed /APPEND "C:\\Users\\s2202694\\Downloads\\PortableGit\\bin" /USER')

# def add_to_path(path):
#     os.system('GTools\\pathed /APPEND "' + path + '" /USER')

# def run_file(path):
#     subprocess.call(path)

# def copy_file(base_path, destination_path):
#     shutil.copy(base_path, destination_path)

# def extract_file(base_path, extracted_path):
#     shutil.unpack_archive(base_path, extracted_path)


installers = [github, obsidian]
for installer in installers:
    subprocess.call(installer)

# set paths and copy vscode to C drive
vscode_location = Path("M:/Software/VSCode Portable.zip")
vscode_destination = Path("C:/Users/s2202694/Downloads/VSCode Portable.zip")
vscode_extract = Path("C:/Users/s2202694/Downloads/VSCode Portable2")
shutil.copy(vscode_location, vscode_destination)

# set paths and copy python to C drive
python_location = Path("M:/Software/python portable.zip")
python_destination = Path("C:/Users/s2202694/Downloads/python portable.zip")
python_extract = Path("C:/Users/s2202694/Downloads/python portable2")
shutil.copy(python_location, python_destination)

# extract python and vscode
shutil.unpack_archive(vscode_destination, vscode_extract)
shutil.unpack_archive(python_destination, python_extracT)