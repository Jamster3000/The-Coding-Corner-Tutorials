from cx_Freeze import setup, Executable
import sys

build_options = {
    "packages": ["os"], #specifys packages to add
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
        script="simple_gui.py",
        target_name="shopApplication.exe",
        base=base,
        icon="icon.ico", #the icon for the exe (optional)
    )
]

# Setup function with MSI options
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
                     "Shop Application",  # Shortcut name
                     "TARGETDIR",  # Target directory
                     "[TARGETDIR]shopApplication.exe",  # Path to EXE
                     None, None, None, None, None, None, "TARGETDIR"),  # Extra params
                    ("StartMenuShortcut",  # Shortcut ID
                     "ProgramMenuFolder",  # Location (Start Menu)
                     "Shop Application",  # Shortcut name
                     "TARGETDIR",  # Target directory
                     "[TARGETDIR]shopApplication.exe",  # Path to EXE
                     None, None, None, None, None, None, "TARGETDIR"),
                ]
            }
        }
    }
)
