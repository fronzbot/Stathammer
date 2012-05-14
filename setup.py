import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).

ver = 0.04 

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includefiles = ['README.txt', 'CHANGELOG.txt', 'staticon.ico']

GUI2Exe_Target_1 = Executable(
	# what to build
	script = "stathammer.pyw",
	initScript = None,
	base = 'Win32GUI',
	targetDir = r"build",
	targetName = "Stathammer.exe",
	compress = True,
	copyDependentFiles = True,
	appendScriptToExe = False,
	appendScriptToLibrary = False,
	icon = "staticon.ico",
        shortcutName = "Stathammer Shortcut",
        shortcutDir = "ProgramMenuFolder"
	)

setup(
        name = "Stathammer",
        version = str(ver),
        description = "Statistics Simulator for Warhammer 40k",
        author = 'Kevin Fronczak',
        author_email = 'kfronczak@gmail.com',
        options = {'build_exe': {'include_files':includefiles}},
        executables = [Executable("stathammer.pyw", base = base)])

