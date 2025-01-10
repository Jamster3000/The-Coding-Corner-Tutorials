from distutils.core import setup
import py2exe

setup(
    name="Shop Application",
    version="1.0",
    description="A sample Python application",
    author="Your awesome name",
    options={
        "py2exe": {
            "packages": ["os"],  # Include additional packages
            "excludes": ["tkinter"],  # Exclude unnecessary modules
            "bundle_files": 1,  # Bundle everything into one file
            "compressed": True,  # Compress the library archive
        }
    },
    console=[
        {
            "script": "shop.py",  # Main script
            "icon_resources": [(0, "icon.ico")],  # Optional: Add an icon
        }
    ],
    #data_files=[("assets", ["assets/file1.txt", "assets/file2.txt"])],  # Include additional files
)
