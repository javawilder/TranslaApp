# -*- coding: utf-8 -*-

# A simple setup script to create an executable using Tkinter. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# SimpleTkApp.py is a very simple type of Tkinter application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
import os
from cx_Freeze import setup, Executable
import certifi
import requests.certs

os.environ['TCL_LIBRARY'] = r'C:\Python33\tcl\tcl8.5'
os.environ['TK_LIBRARY'] = r'C:\Python33\tcl\tk8.5'


include_files = [
    r"'C:\Python33\DLLs\tcl85.dll",
    r'C:\Python33\Python35-32\DLLs\tk85.dll'
]


base = None

#if sys.platform == 'win32':
#    base = 'Win32GUI'

executables = [
    Executable('mainApp.py', base=base)
]

options = {
    'build_exe':
        {
            "include_files":[(requests.certs.where(),'cacert.pem'),'seen.json', 'siteconfig.json', 'appConfig.json','text.json'],
            "includes": ["tkinter","lxml", 'lxml.etree', 'lxml._elementpath','certifi'],
        }

}

setup(
    name = "test1.0",
    version = "1.0",
    description = 'desc of program',
    options=options,
    executables = executables
)