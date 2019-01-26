from cx_Freeze import setup, Executable
import sys
import os
import matplotlib

os.environ['TCL_LIBRARY'] = "C:\LOCAL_TO_PYTHON\PYTHON35-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\LOCAL_TO_PYTHON\PYTHON35-32\tcl\tk8.6"
base=None

if(sys.platform == "win32"):
	base="Win32GUI"

setup(
	name="Automation Analitics",
	options={"build_exe":{"packages":["numpy", "idna"]}},
	version="1.0",
	author="jeet",
	description="Get your analytics in your fingure TiP",
	executables=[Executable(r"C:\Users\HP\Documents\jeet\varenya_test1.py",
				icon=r"C:\Users\HP\Documents\jeet\results-icon-png-17982-Windows.ico",
				shortcutName="automatic analyse",
				shortcutDir="DesktopFolder")]
	)
