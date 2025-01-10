from distutils.core import setup
import py2exe

setup(
    name="Simple GUI",
    version="1.0",
    description="A sample Python application",
    author="Your awesome name",
    options={
        "py2exe": {
            "packages": ["os"],  # Include additional packages
            "bundle_files": 1,  # Bundle everything into one file
            "compressed": True,  # Compress the library archive
        }
    },
    console=[
        {
            "script": "simple_gui.py",  # Main script
            "icon_resources": [(0, "icon.ico")],  # Optional: Add an icon
        }
    ]
)
