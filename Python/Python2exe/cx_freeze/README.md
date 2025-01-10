This tutorial will go through the basics of converting python code into an exe, which can run on any windows machine without the need for python to be installed - using CX_Freeze library.

Using this library you are also able to generate an installer too 

# How exactly does this work
Python code, when executed converts to `bytecode` 
The obvious issue here is that `.exe` window excutables is made of machine code, not bytecode - bytecode "can" be converted to machine code, but it's incredibly complex and introduces unreliability of the code.

> Neither bytecode or machine code is human readable, it's not something someone typically can understand or write.

**This is what the CX_Freeze library does** rather than converting the bytecode into machine code > instead it just combines the python intepreter into the exe, that way python is**theoretically** on any windows machine you have the python exe on.


.



# cx_freeze
This is another python tool to convert code into exe.

## How does this work?
This works the exact same as pyinstaller by packaging the code, libraries used, and a python interpreter for an exe.

## Install
This is similary installed just like most other python libraries
`pip install cx-freeze`


## Getting Started
CX_freeze uses a seperate python file instead of directly in the terminal.

setup.py
```python
from cx_Freeze import setup, Executable

#The executable and any other options
exe = Executable(script="shop.py", target_name="shop.exe")

setup(
    name="ShopApplication",
    version="1.0",
    description="A simple shopping program",
    executables=[exe]
)
```

Here is a simple example of it to go along with the shop.py code previously mentioned.

- get's the imports it needs
- defines the exe
- Basic metadata and setup for the program.


Once this is done, open a terminal and run the following command

```bash
python setup.py build
```

You may get warnings which do happen, but the result of this command should provide you with a build folder containing `lib` folder for all the packages needed and an exe.

## setup.py options

```python
from cx_Freeze import setup, Executable
import sys

build_options = {
    "packages": ["os"], #specifys packages to add
    "excludes": ["tkinter"], #not include packages or libraries to reduce size
    #"include_files": [("config.json", "config.json"), ("assets/", "assets/")],
    "optimize": 2, #optimize the byte code
}

base = None
if sys.platform == "win32":
    base = "Win32GUI" if "gui_app" in sys.argv else None

#The executable and any other options
#You can list multiple Executable to create
executables = [
    Executable(
        script="shop.py",
        target_name="shopApplication.exe",
        base=base,
        icon="icon.ico", #the icon for the exe (optional)
    )
]

setup(
    name="ShopApplication",
    version="1.0",
    description="A simple shopping program",
    options={"build_eve": build_options},
    executables=executables,
)
```

- The **build_options** are options on what it should include or exclude from the exe.
- **optimize** This can be 0, 1, or 2
    - 0 - no optimization
    - 1 - basic optimization (removes any debug statements)
    - 2 - Additional optimization (removes docstrings).
- **base** - specifies teh type of executable, None is the default for console applications, "win32GUI" for GUI applications, which just stops the console window from showing.

## Creating an installer
Creating an installer for your program is as simple as
```bash
python setup.py bdist_msi
```
You will then find a `dist` directory with an `msi` installer that can install your python exe program on any windows device it runs on. You may find that you have to **still** find where the program is installed, it doesn't add it to the start up menu too, so any program you would normally install, you'd be easy to find and install.

This can be fixed with... debatably some messy setup code.

```python
setup(
    name="Shop Application",
    version="1.0",
    description="A sample Python application",
    executables=executables,
    # Define MSI installer options
    options={
        "bdist_msi": {
            "add_to_path": False,  # Do not add to system PATH
            "data": {
                # Add shortcuts to Start Menu and Desktop
                "Shortcut": [
                    ("DesktopShortcut",  # Shortcut ID
                     "DesktopFolder",  # Location (Desktop)
                     "My Application",  # Shortcut name
                     "TARGETDIR",  # Target directory
                     "[TARGETDIR]MyApp.exe",  # Path to EXE
                     None, None, None, None, None, None, "TARGETDIR"),  # Extra params
                    ("StartMenuShortcut",  # Shortcut ID
                     "ProgramMenuFolder",  # Location (Start Menu)
                     "My Application",  # Shortcut name
                     "TARGETDIR",  # Target directory
                     "[TARGETDIR]shopApplication.exe",  # Path to EXE
                     None, None, None, None, None, None, "TARGETDIR"),
                ]
            }
        }
    }
)
```

You should be able to get the just of this with reading the comments.


## CX_freeze with Tkinter
CX_freeze also works out of the box with tkinter
For as long as you don't exclude tkinter, the above should still apply and work as intended for GUI tkinter