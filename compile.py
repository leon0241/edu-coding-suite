import os
import shutil
from pathlib import Path

DIR = Path(os.getcwd())

os.system("PyInstaller startup.py --onefile")
shutil.copy(DIR / "dist" / "startup.exe", DIR / "startup.exe")
os.remove(DIR / "dist" / "startup.exe")